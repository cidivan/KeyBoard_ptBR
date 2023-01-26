#!/usr/bin/python
# -*- coding: utf-8 -*-
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.popup import Popup
from kivymd.uix.button import MDFillRoundFlatButton
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.label import Label

Window.size = (650,700)

class BoxKeyBoard(MDBoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    def about(self, *args):

        boxabout = MDBoxLayout(orientation='vertical')
        pop = Popup(title='About', content=boxabout, size_hint=(None, None), size=(400, 300))

        imagem = Image(source='information.png')
        label = Label(text='Versão: 0.01\n do sistema')
        btn = MDFillRoundFlatButton(text='OK', on_press= pop.dismiss)

        boxabout.add_widget(imagem)
        boxabout.add_widget(label)
        boxabout.add_widget(btn)


        pop.open()

    def additem(self):
        texto = ItemsInput(text=str(self.ids.input.text))
        self.ids.item.add_widget(texto)
        self.ids.input.text=''
    def clear(self):
        self.ids.input.text=''

class ItemsInput(MDBoxLayout):
    def __init__(self, text='', **kwargs):
        super().__init__(**kwargs)
        self.ids.label.text = text

# construtor
class KeyboardMD(MDApp):
    title = "MDKeyboard_0_01_beta"
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return BoxKeyBoard()
        
if __name__ == '__main__':
    KeyboardMD().run()
