import json
import os

#main class
class QuizProgram:
    def __init__(self):
        self.filname = "json_text.json"

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

    def add_questions(self):
        quiz_data = self.file_load()