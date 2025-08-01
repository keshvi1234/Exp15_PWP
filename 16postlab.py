from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button

class TextInputApp(App):
    def build(self):
        # Main layout
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        # Text input field
        self.text_input = TextInput(hint_text='Type something here...', multiline=False, font_size=20)
        self.layout.add_widget(self.text_input)

        # Button to display input
        submit_button = Button(text='Display Text', font_size=20, size_hint=(1, 0.5))
        submit_button.bind(on_press=self.display_text)
        self.layout.add_widget(submit_button)

        # Label to display output
        self.output_label = Label(text='', font_size=24)
        self.layout.add_widget(self.output_label)

        return self.layout

    def display_text(self, instance):
        # Display the text entered in the input field
        entered_text = self.text_input.text
        self.output_label.text = f"You typed: {entered_text}"

# Run the app
if __name__ == '__main__':
    TextInputApp().run()
