import os
import sublime, sublime_plugin
import sys

basename_exe = "opa_build"
exe = basename_exe+".exe"

def kill(self,dirname,exe):
	if sys.platform.startswith('win'):
		self.view.window().run_command('exec', {'cmd': ["tskill "+os.path.splitext(exe)[0]], 'working_dir':dirname, 'shell':True} )
	else:
		self.view.window().run_command('exec', {'cmd': ["killall "+exe], 'working_dir':dirname, 'shell':True} )

def launch(self,dirname,exe):
	exe = os.path.join(dirname,exe)
	if sys.platform.startswith('win'):
		node_path = os.path.join(os.getenv("APPDATA"),"npm","node_modules")
		os.environ["NODE_PATH"] = node_path
		self.view.window().run_command('exec', {'cmd': ["node "+exe+" -p 2000"], 'working_dir':dirname, 'shell':True} )
	else:
		self.view.window().run_command('exec', {'cmd': [exe+" -p 2000"], 'working_dir':dirname, 'shell':True} )

class RunOpaBuildCommand(sublime_plugin.TextCommand):
	def run(self, view):
		dirname = os.path.dirname(self.view.file_name())
		print "Will build & run", exe
		self.view.window().run_command('build')
		kill(self,dirname,exe)
		launch(self,dirname,exe)

class StopRunOpaBuildCommand(sublime_plugin.TextCommand):
	def run(self, view):
		dirname = os.path.dirname(self.view.file_name())
		print "Will kill", exe
		kill(self,dirname,exe)

#class CheckProjectCommand(sublime_plugin.WindowCommand):
#	def run(self, edit):
#		#get filename
		#for root, dirs, files in os.walk("."):
#			print "ROOT " , root
#	     	print "dirs " , dirs
#	     	print "files ", files
	    # 	[dirs.remove(dir) for dir in dirs if dir in dirs_to_ignore]
	    # 	paths = dirs
	    # 	paths.extend(files)
	    # 	for path in paths:
	    #     	print "path = $path"
	    #     	print "fullpath = $full_path"
    	#     	full_path = os.path.join(root, path)	
     #    return


