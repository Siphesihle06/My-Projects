import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window

# Quiz data: questions and corresponding answers
quiz_data = [
    {
        "question": "Ray ray ndinanto yam jikelele ngqu?",
        "answer": "yinja"
    },
    {
        "question": "Ray ray ndinabantu bam bathwele iiqhiya ezibomvu?",
        "answer": "yimicinga yematshisi"
    },
    {
        "question": "Ray ray ndinanto yam ifika kqala?",
        "answer": "ngamehlo"
    }
]

class QuizApp(App):
    def build(self):
        # Set the app window size (optional)
        Window.size = (400, 600)

        # Main layout with background image
        layout = FloatLayout()

        # Add the background image with a question mark
        self.background = Image(source= r"C:\Users\Siphesihle\Downloads\RAY RAY.png", allow_stretch=True, keep_ratio=False)
        layout.add_widget(self.background)

        # Content layout
        self.content_layout = BoxLayout(orientation='vertical', padding=10, spacing=10, size_hint=(.9, .8), pos_hint={'center_x': .5, 'center_y': .5})
        
        self.current_question_index = 0
        self.score = 0

        # Display first question
        self.question_label = Label(text=quiz_data[self.current_question_index]["question"], font_size=24, color=[1, 1, 1, 1])  # White text color
        self.content_layout.add_widget(self.question_label)

        # Text input for user's answer
        self.answer_input = TextInput(hint_text='Enter your answer', multiline=False, font_size=20, size_hint=(1, None), height=40)
        self.content_layout.add_widget(self.answer_input)

        # Submit button
        self.submit_button = Button(text="Submit", font_size=24, on_press=self.check_answer, size_hint=(1, None), height=50)
        self.content_layout.add_widget(self.submit_button)

        # Add the content layout on top of the background
        layout.add_widget(self.content_layout)

        return layout

    def check_answer(self, instance):
        # Get user input and check against the correct answer
        user_answer = self.answer_input.text.lower().strip()
        correct_answer = quiz_data[self.current_question_index]["answer"].lower()

        if user_answer == correct_answer:
            self.show_popup("Correct!", "Your answer is correct.")
            self.score += 1
        else:
            self.show_popup("Incorrect!", f"Sorry, the correct answer is: {correct_answer}")

        # Clear the text input for the next question
        self.answer_input.text = ''

        # Move to the next question
        self.current_question_index += 1
        if self.current_question_index < len(quiz_data):
            self.question_label.text = quiz_data[self.current_question_index]["question"]
        else:
            # If quiz is finished, show final score
            self.show_popup("Quiz Finished!", f"Your final score is {self.score}/{len(quiz_data)}")
            self.question_label.text = "Quiz Finished!"
            self.submit_button.disabled = True

    def show_popup(self, title, message):
        popup_content = BoxLayout(orientation='vertical', padding=10)
        popup_content.add_widget(Label(text=message, font_size=20))
        close_button = Button(text="Close", size_hint_y=None, height=40, on_press=lambda *args: popup.dismiss())
        popup_content.add_widget(close_button)

        popup = Popup(title=title, content=popup_content, size_hint=(0.75, 0.5))
        popup.open()

if __name__ == '__main__':
    QuizApp().run()
