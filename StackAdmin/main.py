#!/usr/bin/env python
#import kivy
from git import *
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.factory import Factory
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.storage.jsonstore import JsonStore
from kivy.properties import ObjectProperty  # @UnresolvedImport

import os
store = JsonStore('stackadmin_config.json')

class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)

class MainView(TabbedPanel):
    #repo = Repo("/Users/Markus Schmieder/Documents/GitHub/StackAdmin_Rep")
    #assert repo.bare == False

    def btnTestClick(self):
        self.ids.lblLabel.text = "--- Geandert! ---"

    # Button um Einstellungen zu speichern
    def btnConfigSave(self):
        store.put('localGit', path=self.ids.txtLocalPath.text)
        store.put('user', forename=self.ids.txtForename.text, lastname=self.ids.txtLastname.text)
        popup = Popup(title='Erfolg', content=Label(text='Einstellungen wurden gespeichert!'), size_hint=(None, None), size=(400, 400))
        popup.open()

    # Ab hier beginnt der FolderOpen-Dialog...
    def dismiss_popup(self):
        self._popup.dismiss()
        
    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Waehle lokales GIT-Verzeichnis", content=content, size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path):
        verzeichnis = ""
        verzeichnis = os.path.normpath(path)
        if verzeichnis != "":
            self.ids.txtLocalPath.text = verzeichnis
        self.dismiss_popup()
        
    # "Konstruktor":
    def on_size(self, *args):
        if store.exists('user'):
            self.ids.txtForename.text = store.get('user')['forename']
            self.ids.txtLastname.text = store.get('user')['lastname']
    
        if store.exists('localGit'):
            self.ids.txtLocalPath.text = store.get('localGit')['path']

class StackAdminApp(App):
    def build(self):
        return MainView()

Factory.register('Root', cls=MainView)
Factory.register('LoadDialog', cls=LoadDialog)

if __name__ == '__main__':
    StackAdminApp().run()