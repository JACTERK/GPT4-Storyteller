# Class defining a character in the game

import ast
import aiLib
import pickle
import settings


# Function that takes an integer 'num', and an optional string 'desc' and returns a list of 'num' character.
# If 'desc' is not provided, it will default to creating 'num' random character of type 'race'.
# If 'num' is not provided, the function will default to creating and returning a single character object.
def new(desc=""):
    print("Creating character...")

    # If no description is provided, generate a random character
    if desc == "":
        x = ast.literal_eval(
            aiLib.generate([{"role": "system", "content": settings.get_character_gen_prompt()}]))

    # If a description is provided, generate a character based on the description
    else:
        x = ast.literal_eval(
            aiLib.generate([{"role": "system", "content": desc}]))

    print(x)

    return Character(x[0], x[1])


class Character:
    # Constructor

    def __init__(self, name, personality):
        self.name = name
        self.personality = personality
        self.chat_log = []

    # ---------------------------------------------

    # Getters and Setters

    def get_name(self):
        return self.name

    def get_personality(self):
        return self.personality

    def get_chat_log(self):
        return self.chat_log

    # ---------------------------------------------

    def set_name(self, name):
        self.name = name

    def set_personality(self, personality):
        self.personality = personality

    def set_chat_log(self, conversation):
        self.chat_log = conversation

    # ---------------------------------------------

    # Key is a character, value is a chat call ({'role': 'system', 'content': 'string'})
    def append_chat_log(self, value):
        self.chat_log.append(value)

    # ---------------------------------------------

    # String representation of the object
    def __str__(self):
        return "Name: " + self.name + ", Personality: " + self.personality

    # TODO: Add a function to make each user that talks to the bot to have their own character object


'''
    # Start a conversation with another character
    def talk_to(self, c):
        print("conv start with : " + c.get_name())
        temp_msg = ""

        # Checks to see if the conversation has already been started, if not append the personality of both characters
        if len(self.chat_log[c]) == 0:
            self.add_to_chat_log(c, {'role': 'system', 'content': self.get_personality()})
            c.add_to_chat_log(self, {'role': 'system', 'content': c.get_personality()})

        # If it has, call the OpenAI API to generate a response
        else:
            # temp_msg is a string
            temp_msg = aiLib.generate(self.chat_log[c])
'''
