#import kivy
<<<<<<< HEAD
#from gitdb import *
=======
>>>>>>> FETCH_HEAD
from git import *
from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.properties import ObjectProperty  # @UnresolvedImport


class MainView(TabbedPanel):
    lblLabel = ObjectProperty(None)
    
    repo = Repo("/Users/mtrier/Development/git-python")
    assert repo.bare == False

    def btnTestClick(self):
        self.lblLabel.text = "--- Geandert! ---"
    pass

class StackAdminApp(App):
    def build(self):
        return MainView()

if __name__ == '__main__':
    StackAdminApp().run()