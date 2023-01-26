#!/usr/bin/python
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.size=(500,700)

class BoxKeyBoard(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    def additem(self):
        texto = ItemsInput(text=str(self.ids.input.text))
        self.ids.item.add_widget(texto)
        self.ids.input.text=''
        
    def clear(self):
       self.ids.input.text=''
       
class ItemsInput(BoxLayout):
    def __init__(self, text='', **kwargs):
        super().__init__(**kwargs)
        self.ids.label.text = text

# construtor
class MainKeyboard(App):
    title = "Keyboard - 0.01_beta"
    def build(self):
        return BoxKeyBoard()

MainKeyboard().run()
