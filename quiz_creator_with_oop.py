import json
import os
from colorama import init, Fore, Style

init()

#create class
class QuizCreator:
    def __init__(self, file_load):
        self.file_load = file_load
    
    #loads data from a json file
    def file_load(self):
        if os.path.exists("json_text.json"):
            with open("json_text.json", "r") as file:
                try:
                    quiz_data = json.load(file)
                    if isinstance(quiz_data, list):
                        return quiz_data
                except json.JSONDecodeError:
                        pass
        return [] 
    
    def data_saver(self, data_format):
        #open a json file to store the data
        with open("json_text.json", "w") as file:
            json.dump(data_format, file, indent=4)

    def add_questions(self):
        #callout file_load()
        quiz_data = self.file_load()

        #where the loop begins
        while True: 
            #ask user for inputs like question, options, and correct answer
            questions = input(Fore.YELLOW + Style.BRIGHT + f"\nEnter question: " + Style.RESET_ALL)
            options = [input(f"Enter option {choice}: ") for choice in ["a", "b", "c", "d"]]
            correct_answers = valid_input(f"Enter correct answer: ").lower()

            #creates dictionary for users' input
            data_format = {
                "question": questions,
                "option": options, 
                "correct_answer": correct_answers
            }

            #then appends the input to the list
            quiz_data.append(data_format)

            try_again = input("add another question? (y/n): ").lower()
            if try_again == "n" or try_again == "no":
                break
                
        data_saver(quiz_data)