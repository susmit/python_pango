# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder

Builder.load_string('''
<display>:
    cols: 2
    Label:
        text:"Welcome to Kivy!"
    Label:
        text:"മലയാളം".decode('utf-8')
    Label:
        text:"हिन्दी".decode('utf-8')
    Label:
        text:"ଓଡ଼ିଆ".decode('utf-8')
    Label:
        text:"தமிழ்".decode('utf-8')
    Label:
        text:"हिन्दी".decode('utf-8')
	''')

class display(GridLayout):
	pass

class TextApp(App):
	def build(self):
		return display()

if __name__ == "__main__":
	TextApp().run()
