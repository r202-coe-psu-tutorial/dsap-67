from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.lang import Builder

# Builder.load_file("hello.kv")


class HelloApp(App):
    def build(self):
        return HelloLayout()


class HelloLayout(BoxLayout):
    def check_credentials(self):
        username = self.ids.username.text
        password = self.ids.password.text
        if username == "admin" and password == "admin":
            self.ids.result_label.text = "Login successful!"
        else:
            self.ids.result_label.text = "Invalid username or password."


if __name__ == "__main__":
    HelloApp().run()
