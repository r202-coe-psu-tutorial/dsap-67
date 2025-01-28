from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label


class HelloApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical")
        username_layout = BoxLayout(orientation="horizontal")
        password_layout = BoxLayout(orientation="horizontal")

        label_username = Label(text="Username:")
        self.username = TextInput(hint_text="Username")

        label_password = Label(text="Password:")
        self.password = TextInput(hint_text="Password", password=True)

        submit_button = Button(text="Submit")
        submit_button.bind(on_press=self.check_credentials)

        self.result_label = Label(text="Result will be shown here.")

        username_layout.add_widget(label_username)
        username_layout.add_widget(self.username)

        password_layout.add_widget(label_password)
        password_layout.add_widget(self.password)

        layout.add_widget(username_layout)
        layout.add_widget(password_layout)
        layout.add_widget(submit_button)
        layout.add_widget(self.result_label)

        return layout

    def check_credentials(self, instance):
        if self.username.text == "admin" and self.password.text == "admin":
            self.result_label.text = "Login successful!"
        else:
            self.result_label.text = "Invalid username or password."


if __name__ == "__main__":
    HelloApp().run()
