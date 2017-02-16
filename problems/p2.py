from kivy.app import App
from kivy.lang import Builder

kv = """
GridLayout:
    cols: 1
    Label:
        font_name: 'NotoEmoji-Regular.ttf'
        text: '\U0001F600'
    TextInput:
        font_name: 'NotoEmoji-Regular.ttf'
        text: '\U0001F600'
"""


class TestApp(App):
    def build(self):
        return Builder.load_string(kv)

if __name__ == '__main__':
    TestApp().run()
