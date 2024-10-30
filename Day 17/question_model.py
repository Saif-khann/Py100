# question_model.py defines the Question class, representing a quiz question.

class Question:
    """A class to represent a single quiz question with text and answer."""

    def __init__(self, q_text, q_answer):
        # Stores the question text and the correct answer
        self.text = q_text
        self.answer = q_answer
