#!/usr/bin/env python2
#-*- coding: utf-8 -*-

from kivy.app import App
from kivy.lang import Builder

root = Builder.load_string(u'''
Label:
    text: u"😉"
    font_size: '64pt'
    font_name: "/usr/share/fonts/noto/NotoEmoji-Regular.ttf"
''')


class Label(App):
    def build(self):
        return root

if __name__ == '__main__':
    Label().run()
