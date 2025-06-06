import json
import os
import random
from colorama import init, Fore, Style

init()

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
            questions = input(Fore.YELLOW + Style.BRIGHT + f"\nEnter question: " + Style.RESET_ALL)
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
            print(Fore.BLUE + Style.BRIGHT + f"\n{quiz['question']}" + Style.RESET_ALL)
            for letter, opt in zip(["a", "b", "c", "d"], quiz["option"]):
                print(Fore.YELLOW + f"{letter}. {opt}" + Style.RESET_ALL)

            answer = self.valid_input("your answer: ").lower()
            if answer == quiz["correct_answer"]:
                print(Fore.GREEN + Style.BRIGHT + f"correct, {random.choice(self.comments)}" + Style.RESET_ALL)
                init_score += 1
            else:
                print(Fore.RED + Style.BRIGHT + f"Incorrect. The correct answer was: {quiz['correct_answer']}" + Style.RESET_ALL)

        if init_score == qstns_cnt:
            print(f"PERFECT!\nscore: {init_score}/{qstns_cnt}")
        elif init_score >= 0.75 * qstns_cnt:
            print(f"CONGRATS!\nscore: {init_score}/{qstns_cnt}")
        else:
            print(f"you did great, try again next time\nscore: {init_score}/{qstns_cnt}")

    #calling the functions for main program
    def main_program(self):
        while True:
            choice = self.valid_input(
                Fore.MAGENTA + "\nProgram Menu:\na.) add questions\nb.) take a quiz\nc.) exit program\n=> " + Style.RESET_ALL).lower().strip()

            if choice == "a":
                self.add_questions()
            elif choice == "b":
                self.main_quiz()
            elif choice == "c":
                print("exiting...")
                break
            else:
                print("invalid, try again")

if __name__ == "__main__":
    quiz = QuizProgram()
    quiz.main_program()