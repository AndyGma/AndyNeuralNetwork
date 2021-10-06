from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class AndyGmaApp(MDApp):
    def build(self):
        return MDLabel(text="Dear Andrew, This is your Neural Network", halign="center")


AndyGmaApp().run()