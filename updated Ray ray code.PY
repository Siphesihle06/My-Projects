import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

# Quiz data: questions and corresponding answers
quiz_data = [
    {"question": "Ray ray ndinanto yam jikelele ngqu?", "answer": "yinja"},
    {"question": "Ray ray ndinabantu bam bathwele iiqhiya ezibomvu?", "answer": "yimicinga yematshisi"},
    {"question": "Ray ray ndinanto yam ifika kqala?", "answer": "ngamehlo"}
]

# Define the LoadingScreen
class LoadingScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()

        # Background image
        self.background = Image(source=r"C:\Users\Siphesihle\Music\Screenshot (539).png", allow_stretch=True, keep_ratio=False)
        layout.add_widget(self.background)

        # Play button
        play_button = Button(
            text="Qala Umdlalo",  # Play in English
            size_hint=(0.3, 0.1),
            pos_hint={"center_x": 0.5, "center_y": 0.2},
            font_size=24,
            on_press=self.start_quiz,
            background_color=(0, 0, 1, 1),  # Blue background (RGBA)
            color=(1, 1, 1, 1)  # White text (RGBA)
        )
        layout.add_widget(play_button)
        self.add_widget(layout)

    def start_quiz(self, instance):
        self.manager.current = "quiz"  # Switch to quiz screen


# Define the QuizScreen
class QuizScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.current_question_index = 0
        self.score = 0

        # Main layout
        self.layout = FloatLayout()

        # Background image
        self.background = Image(source=r"C:\Users\Siphesihle\Downloads\RAY RAY.png", allow_stretch=True, keep_ratio=False)
        self.layout.add_widget(self.background)

        # Content layout
        self.content_layout = BoxLayout(orientation='vertical', padding=10, spacing=10, size_hint=(.9, .8), pos_hint={'center_x': .5, 'center_y': .5})

        # Question button (used to display the question)
        self.question_button = Button(
            text=quiz_data[self.current_question_index]["question"],
            font_size=24,
            size_hint=(1, None),
            height=60,
            background_color=(0, 0, 1, 1),  # Blue background
            color=(1, 1, 1, 1)  # White text
        )
        self.content_layout.add_widget(self.question_button)

        # Answer input
        self.answer_input = TextInput(
            hint_text='Enter your answer',
            multiline=False,
            font_size=20,
            size_hint=(1, None),
            height=40
        )
        self.content_layout.add_widget(self.answer_input)

        # Submit button
        self.submit_button = Button(
            text="Submit",
            font_size=24,
            on_press=self.check_answer,
            size_hint=(1, None),
            height=50
        )
        self.content_layout.add_widget(self.submit_button)

        # Start again button
        self.start_again_button = Button(
            text="Start Again",
            font_size=24,
            on_press=self.start_again,
            size_hint=(0.3, None),
            height=50,
            pos_hint={"center_x": 0.5, "center_y": 0.1},
            background_color=(0, 0, 1, 1),  # Blue background
            color=(1, 1, 1, 1)  # White text
        )
        self.start_again_button.opacity = 0  # Initially hidden
        self.content_layout.add_widget(self.start_again_button)

        self.layout.add_widget(self.content_layout)
        self.add_widget(self.layout)

    def check_answer(self, instance):
        user_answer = self.answer_input.text.lower().strip()
        correct_answer = quiz_data[self.current_question_index]["answer"].lower()

        if user_answer == correct_answer:
            self.score += 1
            self.show_popup("Correct!", "Your answer is correct.")
        else:
            self.show_popup("Incorrect!", f"Sorry, the correct answer is: {correct_answer}")

        self.answer_input.text = ''
        self.current_question_index += 1

        if self.current_question_index < len(quiz_data):
            # Update the question text
            self.question_button.text = quiz_data[self.current_question_index]["question"]
        else:
            # Quiz finished
            self.show_popup("Quiz Finished!", f"Your final score is {self.score}/{len(quiz_data)}")
            self.question_button.text = "Quiz Finished!"
            self.submit_button.disabled = True
            self.start_again_button.opacity = 1  # Show the start again button

    def start_again(self, instance):
        # Reset quiz variables
        self.current_question_index = 0
        self.score = 0

        # Reset UI elements
        self.question_button.text = quiz_data[self.current_question_index]["question"]
        self.submit_button.disabled = False
        self.start_again_button.opacity = 0  # Hide the start again button
        self.answer_input.text = ''

    def show_popup(self, title, message):
        popup_content = BoxLayout(orientation='vertical', padding=10)
        popup_content.add_widget(Label(text=message, font_size=20))
        close_button = Button(text="Close", size_hint_y=None, height=40, on_press=lambda *args: popup.dismiss())
        popup_content.add_widget(close_button)

        popup = Popup(title=title, content=popup_content, size_hint=(0.75, 0.5))
        popup.open()


# Main app class
class QuizApp(App):
    def build(self):
        Window.size = (200, 300)
        sm = ScreenManager()
        sm.add_widget(LoadingScreen(name="loading"))
        sm.add_widget(QuizScreen(name="quiz"))
        return sm


if __name__ == '__main__':
    QuizApp().run()
