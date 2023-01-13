import json
import re  # Regex or regular expression
import random_responses
import speech_recognition
import pyttsx3 as tts

import sys
import threading
import tkinter as tk

import speech_recognition
import pyttsx3 as tts

#from neuralintents import GenericAssistant

class Assistant:

    def __init__(self) -> None:
        self.recognizer = speech_recognition.Recognizer()
        self.speaker = tts.init()
        self.speaker.setProperty("rate",150)

        #self.assistant = GenericAssistant("intents.json", intent_methods={"file": self.creat_file})
        #self.assistant.train_model()

        self.root = tk.Tk()
        self.label = tk.Label(text="aa", font=("Arial", 120, "bold"))
        self.label.pack()

        self.response_data = self.load_json("/home/yuxiang/code/2023/AutoPlow_NLP_ChatBot/Python_Native_Chatbot/bot.json")


        threading.Thread(target=self.run_assistant).start()

        self.root.mainloop()

        # Load JSON data
    def load_json(file):
        with open(file) as bot_responses:
            print(f"Loaded '{file}' successfully!")
            return json.load(bot_responses)

    def get_response(input_string, response_data):
        split_message = re.split(r'\s+|[,;?!.-]\s*', input_string.lower())
        score_list = []

        # Check all the responses
        for response in response_data:
            response_score = 0
            required_score = 0
            required_words = response["required_words"]

            # Check if there are any required words
            if required_words:
                for word in split_message:
                    if word in required_words:
                        required_score += 1

            # Amount of required words should match the required score
            if required_score == len(required_words):
                # print(required_score == len(required_words))
                # Check each word the user has typed
                for word in split_message:
                    # If the word is in the response, add to the score
                    if word in response["user_input"]:
                        response_score += 1

            # Add score to list
            score_list.append(response_score)
            # Debugging: Find the best phrase
            # print(response_score, response["user_input"])

        # Find the best response and return it if they're not all 0
        best_response = max(score_list)
        response_index = score_list.index(best_response)

        # Check if input is empty
        if input_string == "":
            return "Please type something so we can chat :("

        # If there is no good response, return a random one.
        if best_response != 0:
            bot_output = response_data[response_index]
            if bot_output["response_type"] == "action":
                # robotic arm integration
                print("----------")
                
            return bot_output["bot_response"]

        return random_responses.random_string()

    def run_assistnant(self):
        while True:
            # Store JSON data
            try:
                with speech_recognition.Microphone() as mic:
                    self.recognizer.adjust_for_ambient_nois(mic, duration = 0.2)
                    audio = self.recognizer.listen(mic)

                    text = self.recognizer.recognize_google(audio)
                    text = text.lower()

                    if "hey mac" in text:
                        self.label.config(fg="red")
                        audio = self.recognizer.listen(mic)
                        text = self.recognizer.recognize_google(audio)
                        text = text.lower()
                        if text == "stop":
                            self.speaker.say("Bye")
                            self.speaker.runAndWait()
                            self.speaker.stop()
                            self.root.destroy()
                            sys.exit()
                        else:
                            if text is not None:
                                response = self.get_response(text, self.response_data)
                                print("Bot:", response)
                                #response = self.assistant.request()
                                if response is not None:
                                    self.speaker.say(response)
                                    self.speaker.runAndWait()
                            self.label.config(fg="black")
            except:
                self.label.config(fg="black")
                continue


Assistant()






