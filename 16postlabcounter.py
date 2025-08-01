from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class CounterApp(App):
    def build(self):
        self.counter = 0

        layout = BoxLayout(orientation='vertical')

        self.label = Label(
            text=f"Counter: {self.counter}",
            font_size=40,
            color=(1, 1, 1, 1)
        )

        self.button = Button(
            text="Increment",
            size_hint=(1, 0.2),
            font_size=24,
            background_color=(0.3, 0.3, 0.3, 1),
            color=(1, 1, 1, 1)
        )
        self.button.bind(on_press=self.increment_counter)

        layout.add_widget(self.label)
        layout.add_widget(self.button)

        # Set background color to black
        from kivy.core.window import Window
        Window.clearcolor = (0, 0, 0, 1)

        return layout

    def increment_counter(self, instance):
        self.counter += 1
        self.label.text = f"Counter: {self.counter}"

if __name__ == "__main__":
    CounterApp().run()
