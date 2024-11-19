from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.uix.relativelayout import RelativeLayout
import random

class UQIKELELOMANANI(App):
    def build(self):
        # Use RelativeLayout to manage overlapping widgets like the background image
        self.layout = RelativeLayout()

        # Add background image (Adjust the path to your image file here)
        self.bg_image = Image(source= r"C:\Users\Siphesihle\Downloads\DALL·E 2024-10-05 12.08.47 - A visually appealing background image with a playful theme for a guessing game. The image should feature the text 'Umdlalo wokuQikelelo Amanani' promi.webp", allow_stretch=True, keep_ratio=False)
        self.layout.add_widget(self.bg_image)

        # Create a vertical layout for content (input, buttons, etc.)
        self.content_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.layout.add_widget(self.content_layout)

        # Instructions
        self.instructions = Label(text="Qikelela inani endilicingayo phakathi kwesinye neKhulu.", color=(1, 1, 1, 1))
        self.content_layout.add_widget(self.instructions)

        # Text input for user's guess
        self.guess_input = TextInput(hint_text="Faka uQikelelo lwakho", multiline=False)
        self.content_layout.add_widget(self.guess_input)

        # Status label to display feedback
        self.status_label = Label(text="", color=(1, 1, 1, 1))
        self.content_layout.add_widget(self.status_label)

        # Button to submit guess
        self.submit_button = Button(text="Masibone unentlahla engakanani", on_press=self.check_guess)
        self.content_layout.add_widget(self.submit_button)

        # Button to start the game
        self.start_button = Button(text="Qalela phantsi", on_press=self.start_game)
        self.content_layout.add_widget(self.start_button)

        # Initialize the game state
        self.start_game()

        return self.layout

    def start_game(self, *args):
        """ Initialize a new game """
        self.TargetNumber = random.randint(1, 100)
        self.Guesses = 0
        self.guess_input.text = ""
        self.guess_input.disabled = False
        self.submit_button.disabled = False
        self.status_label.text = "Masibone ukuba intlahla yakho ingakanani na! qikelela elinani ndicinga ngalo."

    def check_guess(self, instance):
        """ Check the user's guess """
        try:
            UserNumber = int(self.guess_input.text)
            self.Guesses += 1
            if UserNumber < self.TargetNumber:
                self.status_label.text = 'Uyabanda! inani olichazileyo lingaphantsi kwelinani ndilicingayo.'
            elif UserNumber > self.TargetNumber:
                self.status_label.text = 'Uyabanda! inani olichazileyo lingaphezulu kwelinani ndilicingayo.'
            else:
                self.show_popup(f'Halala! uchanu cwethe lilo elinani bendilicinga {self.TargetNumber}', f'uQikelele u {self.TargetNumber} ngamatyeli angama {self.Guesses}')
                self.guess_input.disabled = True
                self.submit_button.disabled = True
        except ValueError:
            self.show_popup('Invalid Input', 'Please enter a valid integer.')

    def show_popup(self, title, message):
        """ Show a popup message """
        popup_layout = BoxLayout(orientation='vertical', padding=10)
        popup_label = Label(text=message)
        close_button = Button(text='Close', on_press=lambda x: popup.dismiss())

        popup_layout.add_widget(popup_label)
        popup_layout.add_widget(close_button)

        popup = Popup(title=title, content=popup_layout, size_hint=(None, None), size=(300, 200))
        popup.open()

# Run the Kivy App
if __name__ == "__main__":
    UQIKELELOMANANI().run()