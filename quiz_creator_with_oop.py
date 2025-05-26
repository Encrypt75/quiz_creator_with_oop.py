import json
import os
import random

#main class
class QuizProgram:
    def __init__(self):
        self.filename = "json_text.json"
        self.comments = [
            "wow you are great",
            "how do you know that one?",
            "you are bright",
            "are you trying to ace it?",
            "nice!",
            "is it just me? or are you killing it"
        ]

    #error handling
    def valid_input(self, correct_letter):
        valid_input_for_choices = ["a", "b", "c", "d"]
        while True:
            select = input(correct_letter).lower()
            if select in valid_input_for_choices:
                return select
            else:
                print("Invalid input, try again")

    #loads data from a json file
    def file_load(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                try:
                    quiz_data = json.load(file)
                    if isinstance(quiz_data, list):
                        return quiz_data
                except json.JSONDecodeError:
                    pass
        return []

    def data_saver(self, data_format):
        #open a json file to store the data
        with open(self.filename, "w") as file:
            json.dump(data_format, file, indent=4)
    
    #adding questions to the quiz
    def add_questions(self):
        quiz_data = self.file_load()

        while True:
            questions = input(f"\nEnter question: ").strip()
            options = [input(f"Enter option {choice}: ") for choice in ["a", "b", "c", "d"]]
            correct_answers = self.valid_input("Enter correct answer: ").lower()

            data_format = {
                "question": questions,
                "option": options,
                "correct_answer": correct_answers
            }

            quiz_data.append(data_format)

            try_again = input("add another question? (y/n): ").lower()
            if try_again in ["n", "no"]:
                break

        self.data_saver(quiz_data)

    def main_quiz(self):
        quiz_data = self.file_load()
        if not quiz_data:
            print("No questions was saved yet")
            return

        qstns_available = len(quiz_data)

        while True:
            try:
                qstns_cnt = int(input(f"How many questions will you take? (1 to {qstns_available}): "))
                if 1 <= qstns_cnt <= qstns_available:
                    break
                else:
                    print(f"Please enter a number between 1 and {qstns_available}.")
            except ValueError:
                print("Please enter a valid number.")

        random.shuffle(quiz_data)
        selected_questions = quiz_data[:qstns_cnt]
        init_score = 0

        for quiz in selected_questions:
            print(f"\n{quiz['question']}")
            for letter, opt in zip(["a", "b", "c", "d"], quiz["option"]):
                print(f"{letter}. {opt}")

            answer = self.valid_input("your answer: ").lower()
            if answer == quiz["correct_answer"]:
                print(f"correct, {random.choice(self.comments)}")
                init_score += 1
            else:
                print(f"Incorrect. The correct answer was: {quiz['correct_answer']}")

        if init_score == qstns_cnt:
            print(f"PERFECT!\nscore: {init_score}/{qstns_cnt}")
        elif init_score >= 0.75 * qstns_cnt:
            print(f"CONGRATS!\nscore: {init_score}/{qstns_cnt}")
        else:
            print(f"you did great, try again next time\nscore: {init_score}/{qstns_cnt}")

if __name__ == "__main__":
    quiz = QuizProgram()
    quiz.add_questions()
    quiz.main_quiz()