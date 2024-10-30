'''
🥇(Py100: 100 Days of Python Challenge)
Author: Saif
-----------------------------------
Day 17: Quiz Game Project with OOP Principles
-----------------------------------
Description: 
This project is a simple quiz game built using OOP concepts. The user answers True/False questions
pulled from a dataset. The game checks each answer, tracks the score, and displays it at the end.

main.py initializes the question list, creates a QuizBrain instance, and runs the quiz loop.
question_model.py defines the Question class, storing text and answer for each question.
quiz_brain.py defines QuizBrain, which controls the quiz flow, handles question prompts, and scoring.
data.py contains question data in dictionary format, which is used to populate the question bank.
-----------------------------------
'''

# main.py initializes and starts the quiz game using question data and OOP classes.

from question_model import Question  # Imports the Question class for question object creation
from data import question_data       # Imports the question data
from quiz_brain import QuizBrain     # Imports the QuizBrain class to manage quiz functionality

# Create question bank by iterating over the data and generating Question objects
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Initialize the quiz with the question bank
quiz = QuizBrain(question_bank)

# Loop through questions as long as there are more to answer
while quiz.still_has_questions():
    quiz.next_question()

# Display the final score when the quiz ends
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
