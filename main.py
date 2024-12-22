from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen

# Home screen class
class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        button = Button(text="Click Here to Go to Second Page")
        button.bind(on_press=self.go_to_second_page)
        self.add_widget(button)

    def go_to_second_page(self, instance):
        # Switch to the second screen
        self.manager.current = "second"

# Second screen class
class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super(SecondScreen, self).__init__(**kwargs)
        button = Button(text="Go Back to Home Page")
        button.bind(on_press=self.go_to_home_page)
        self.add_widget(button)

    def go_to_home_page(self, instance):
        # Switch back to the home screen
        self.manager.current = "home"

# Main app class
class MyApp(App):
    def build(self):
        sm = ScreenManager()
        # Add both screens to the ScreenManager
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(SecondScreen(name="second"))
        return sm

if __name__ == "__main__":
    MyApp().run()
