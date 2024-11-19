import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.metrics import dp  # For scaling on different screen sizes
from random import shuffle

# Expanded Quiz Data: questions and multiple choice answers
quiz_data = [
    # Chapter 1: What economics is all about
    {
        "question": "What is economics primarily concerned with?",
        "choices": ["A) Buying and selling stocks", "B) Making as much money as possible", "C) The use of scarce resources to satisfy unlimited wants", "D) Creating wealth for individuals"],
        "answer": "C"
    },
    {
        "question": "Which of the following best defines 'scarcity' in economics?",
        "choices": ["A) Unlimited resources", "B) Limited wants", "C) Limited resources to meet unlimited wants", "D) Economic downturns"],
        "answer": "C"
    },
    {
        "question": "Which of the following is an opportunity cost?",
        "choices": ["A) Money spent", "B) A forgone alternative", "C) Revenue lost", "D) Productive resources"],
        "answer": "B"
    },
    # Chapter 2: Economic systems
    {
        "question": "Which economic system allows for private ownership of resources?",
        "choices": ["A) Traditional economy", "B) Command economy", "C) Market economy", "D) Mixed economy"],
        "answer": "C"
    },
    {
        "question": "A command economy is characterized by:",
        "choices": ["A) Free markets", "B) Government control over resources", "C) Price mechanism", "D) Consumer choice"],
        "answer": "B"
    },
    # Chapter 4: Demand, supply, and prices
    {
        "question": "What happens when the demand for a good increases and supply remains constant?",
        "choices": ["A) The price decreases", "B) The price increases", "C) Supply increases", "D) The price remains constant"],
        "answer": "B"
    },
    {
        "question": "In a market, if the price is set below the equilibrium price, it will lead to:",
        "choices": ["A) A surplus", "B) A shortage", "C) Increased demand", "D) Decreased supply"],
        "answer": "B"
    },
    # Chapter 5: Demand and supply in action
    {
        "question": "A simultaneous increase in both demand and supply will most likely:",
        "choices": ["A) Increase price but reduce quantity", "B) Increase quantity but leave price uncertain", "C) Decrease both price and quantity", "D) Leave both price and quantity unchanged"],
        "answer": "B"
    },
    {
        "question": "Which of the following can shift the demand curve?",
        "choices": ["A) Changes in income", "B) Price of the good", "C) Changes in technology", "D) Number of sellers"],
        "answer": "A"
    },
    # Chapter 6: Elasticity
    {
        "question": "If the price elasticity of demand is greater than 1, the good is considered:",
        "choices": ["A) Perfectly elastic", "B) Elastic", "C) Inelastic", "D) Unit elastic"],
        "answer": "B"
    },
    {
        "question": "What happens when demand for a product is perfectly inelastic?",
        "choices": ["A) Quantity demanded stays the same regardless of price changes", "B) Price stays constant", "C) Quantity demanded changes significantly with price", "D) Demand disappears"],
        "answer": "A"
    },
    # Chapter 9: Production and cost
    {
        "question": "In the short run, which cost cannot be changed?",
        "choices": ["A) Fixed cost", "B) Variable cost", "C) Marginal cost", "D) Total cost"],
        "answer": "A"
    },
    {
        "question": "In the long run, all costs are:",
        "choices": ["A) Variable", "B) Fixed", "C) Marginal", "D) Sunk"],
        "answer": "A"
    },
    # Chapter 10: Market structures and perfect competition
    {
        "question": "Which market structure has many firms selling identical products?",
        "choices": ["A) Monopoly", "B) Oligopoly", "C) Monopolistic competition", "D) Perfect competition"],
        "answer": "D"
    },
    {
        "question": "A monopoly is a market structure where:",
        "choices": ["A) Many firms sell differentiated products", "B) One firm controls the entire market", "C) Firms compete by lowering prices", "D) Firms have no market power"],
        "answer": "B"
    },
    # Chapter 13: Measuring the performance of the economy
    {
        "question": "What does GDP measure?",
        "choices": ["A) Total income of individuals", "B) Total spending in the economy", "C) Total value of all final goods and services produced", "D) The wealth of a nation"],
        "answer": "C"
    },
    {
        "question": "What is the difference between real GDP and nominal GDP?",
        "choices": ["A) Real GDP includes inflation, nominal GDP does not", "B) Nominal GDP includes inflation, real GDP is adjusted for inflation", "C) Real GDP is higher than nominal GDP", "D) Nominal GDP is higher than real GDP"],
        "answer": "B"
    },
    # Chapter 14: The monetary sector
    {
        "question": "What is one of the key functions of money?",
        "choices": ["A) It is a factor of production", "B) It serves as a store of value", "C) It increases economic growth", "D) It ensures price stability"],
        "answer": "B"
    },
    {
        "question": "Which institution is responsible for controlling the money supply in South Africa?",
        "choices": ["A) Commercial Banks", "B) The South African Reserve Bank", "C) The Treasury", "D) Parliament"],
        "answer": "B"
    },
    # Chapter 16: The foreign sector
    {
        "question": "Which of the following best describes why countries trade?",
        "choices": ["A) To limit domestic competition", "B) To exploit other nations' resources", "C) To achieve greater specialization and efficiency", "D) To avoid producing goods"],
        "answer": "C"
    },
    {
        "question": "What is the effect of a depreciation of a country’s currency?",
        "choices": ["A) Imports become cheaper", "B) Exports become more expensive", "C) Exports become cheaper", "D) Exports are unaffected"],
        "answer": "C"
    },
    # Chapter 20: Inflation
    {
        "question": "What is inflation?",
        "choices": ["A) A decrease in the value of money", "B) An increase in the price level of goods and services", "C) A rise in interest rates", "D) A period of rapid economic growth"],
        "answer": "B"
    },
    {
        "question": "Which type of inflation is caused by rising costs of production?",
        "choices": ["A) Demand-pull inflation", "B) Cost-push inflation", "C) Structural inflation", "D) Hyperinflation"],
        "answer": "B"
    },
    # Chapter 21: Unemployment
    {
        "question": "Which type of unemployment is caused by economic recessions?",
        "choices": ["A) Frictional unemployment", "B) Structural unemployment", "C) Cyclical unemployment", "D) Seasonal unemployment"],
        "answer": "C"
    },
    {
        "question": "Which of the following can reduce structural unemployment?",
        "choices": ["A) Technological advances", "B) Training and education programs", "C) Reducing interest rates", "D) Increasing exports"],
        "answer": "B"
    }
]

class QuizApp(App):
    def build(self):
        # Main layout with background image
        layout = FloatLayout()

        # Add the background image (use relative path or full path as per device)
        self.background = Image(source='/storage/emulated/0/Download/RAY_RAY.png', allow_stretch=True, keep_ratio=False)
        layout.add_widget(self.background)

        # Content layout
        self.content_layout = BoxLayout(orientation='vertical', padding=10, spacing=10, size_hint=(.9, .8), pos_hint={'center_x': .5, 'center_y': .5})
        
        self.current_question_index = 0
        self.score = 0

        # Display first question
        self.question_label = Label(text=quiz_data[self.current_question_index]["question"], font_size=24, color=[0, 0, 0, 1])  # Black text color
        self.content_layout.add_widget(self.question_label)

        # Create buttons for multiple-choice answers
        self.answer_buttons = []
        for choice in quiz_data[self.current_question_index]["choices"]:
            btn = Button(text=choice, font_size=20, on_press=self.check_answer, size_hint=(1, None), height=dp(50))
            self.answer_buttons.append(btn)
            self.content_layout.add_widget(btn)

        # Add the content layout on top of the background
        layout.add_widget(self.content_layout)

        return layout

    def check_answer(self, instance):
        if instance.text.startswith(quiz_data[self.current_question_index]["answer"]):
            self.score += 1
        
        self.current_question_index += 1

        if self.current_question_index < len(quiz_data):
            self.update_question()
        else:
            self.show_score()

    def update_question(self):
        self.question_label.text = quiz_data[self.current_question_index]["question"]
        for i, choice in enumerate(quiz_data[self.current_question_index]["choices"]):
            self.answer_buttons[i].text = choice

    def show_score(self):
        score_popup = Popup(title='Score', content=Label(text=f'Your score: {self.score}/{len(quiz_data)}'), size_hint=(None, None), size=(400, 400))
        score_popup.open()

if __name__ == '__main__':
    QuizApp().run()
