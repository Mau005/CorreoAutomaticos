from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
Builder.load_file("kvlengs/main.kv")

class Inicio(MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.name = "inicio"


class Correo(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.inicio = Inicio()
        self.manejador = ScreenManager()
        self.manejador.add_widget(self.inicio)

    def build(self):
        return self.manejador

if __name__ == "__main__":
    Correo().run()