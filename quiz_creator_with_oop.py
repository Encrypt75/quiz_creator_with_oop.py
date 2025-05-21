import json
import os

#create class
class QuizCreator:
    def __init__(self):
        pass
    
    #loads data from a json file
    def file_load():
        if os.path.exists("json_text.json"):
            with open("json_text.json", "r") as file:
                try:
                    quiz_data = json.load(file)
                    if isinstance(quiz_data, list):
                        return quiz_data
                except json.JSONDecodeError:
                        pass
        return [] 