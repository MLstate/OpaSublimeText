import os
import sublime, sublime_plugin
import sys
import task, subprocess, signal

basename_exe = "opa_build"

if sys.platform.startswith('win'):
	exe_name = basename_exe+".js"
else:
	exe_name = basename_exe+".exe"

launched = {}
locations = {}

def prog_name(prog):
	if sys.platform.startswith('win'):
		return prog+".exe"
	else:
		return prog

def location(program):
	if not (program in locations):
		for path in os.environ["PATH"].split(os.pathsep):
			pfile = os.path.join(path, program)
			if os.path.isfile(pfile):
				locations[program] = path
				return path
		raise Exception(program,'Not found')
	else:
		return locations[program]

def taskid(self,dirname,exe):
	return dirname
	#return str(self.view.id())

def kill(self,dirname,exe):
	id = taskid(self,dirname,exe)
	print "Killing task" , id
	if not(id in launched):
		print "Nothing to do"
		return
	t = launched.pop(id)
	if hasattr(t,"proc"): 
		pid = t.proc.proc.pid
	else:
		pid = None
	if pid==None:
		print "Nothing to do (No pid)"
		return
	if t.proc.proc.returncode!=None:
		print "Nothing to do (Already returned)"
		return
	print "Killing pid" , pid
	if sys.platform.startswith('win'):
		si = subprocess.STARTUPINFO()
		si.dwFlags = subprocess.STARTF_USESHOWWINDOW
		si.wShowindow = subprocess.SW_HIDE
		subprocess.call(['taskkill','/F', '/T', '/PID', str(pid)],startupinfo=si)
	else:
		os.killpg(pid, signal.SIGKILL)
	
def launch(self,dirname,exe):
	exe = os.path.join(dirname,exe)
	command = exe+" -p 2000"
	env = os.environ.copy()
	working_dir = dirname
	if sys.platform.startswith('win'):
		node = prog_name("node")
		node_path = os.path.join(os.getenv("APPDATA"),"npm","node_modules")
		env["NODE_PATH"] = node_path
		command = node+ " " + command
	else:
		command =  command
	t = task.Task(self.view.window())
	id = taskid(self,dirname,exe)
	launched[id] = t
	t.run(cmd=[command],working_dir=dirname,env=env)
	launched[id] = t
	print "Has launched", t.proc.proc.pid

def output(view,str):
	print str
	selection_was_at_end = (len(view.sel()) == 1 and view.sel()[0] == sublime.Region(view.size()))
	view.set_read_only(False)
	edit = view.begin_edit()
	view.insert(edit, view.size(), str)
	if selection_was_at_end:
		view.show(view.size())
	view.end_edit(edit)
	view.set_read_only(True)

class runOpaBuildCommand(sublime_plugin.TextCommand):
	def run(self, view):
		panel = self.view.window().get_output_panel("exec")
		dirname = os.path.dirname(self.view.file_name())
		exe = exe_name
		output(panel, "Will build & run "+exe)
		output(panel,"\nCompiling ...")
		self.view.window().run_command('build')
		output(panel,"done\n")
		output(panel,"\nStoping previous launch ...")
		kill(self,dirname,exe)
		output(panel,"done\n")
		output(panel,"Launching ...")
		launch(self,dirname,exe)
		#output(panel,"The application has started\n")


class stopRunOpaBuildCommand(sublime_plugin.TextCommand):
	def run(self, view):
		dirname = os.path.dirname(self.view.file_name())
		print "Will kill", exe_name
		kill(self,dirname,exe_name)
