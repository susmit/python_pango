#!/usr/bin/python
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.button import Button

class TestApp(App):
    def build(self):
        return Button(text='விகடகவி'.decode('utf-8'),font_name='Uni Ila.Sundaram-01.ttf',font_size=50)

TestApp().run()
