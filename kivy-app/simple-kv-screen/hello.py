from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.screenmanager import FadeTransition

Builder.load_file("hello.kv")


class HelloApp(App):
    def build(self):
        return ScreenManagement(transition=FadeTransition())


class ScreenManagement(ScreenManager):
    pass


class LoginScreen(Screen):
    def check_credentials(self):
        username = self.ids.username.text
        password = self.ids.password.text
        if username == "admin" and password == "admin":
            self.manager.current = "home"
        else:
            self.ids.result_label.text = "Invalid username or password."


class HomeScreen(Screen):
    pass


if __name__ == "__main__":
    HelloApp().run()
