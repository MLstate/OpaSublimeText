import sublime
import sublime_plugin
import webbrowser

class gotoOpaDocCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        word = self.view.substr(self.view.word(self.view.sel()[0].begin()))
        for region in self.view.sel():
            docapi = 'http://doc.opalang.org/api'
            docapisearch = 'http://doc.opalang.org/search?q='
            #docapisearch = 'http://doc.opalang.org/#!/search/'
            if not region.empty():
                phrase = self.view.substr(region)
                webbrowser.open_new_tab(docapisearch + phrase)
            else:
                webbrowser.open_new_tab(docapi)