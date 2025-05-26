import json
import os

#main class
class QuizProgram:
    def __init__(self):
        self.filename = "json_text.json"
        
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

if __name__ == "__main__":
    quiz = QuizProgram()
    quiz.add_questions()