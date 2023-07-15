# Class defining a discord chat user

import ast
import aiLib
import pickle
import settings


# Function that takes an integer 'num', and an optional string 'desc' and returns a list of 'num' character.
# If 'desc' is not provided, it will default to creating 'num' random character of type 'race'.
# If 'num' is not provided, the function will default to creating and returning a single character object.
def new(name, discord_id, message=None):
    print("Creating user...")

    if message is not None:
        return User(name, discord_id, message)
    else:
        return User(name, discord_id)


class User:
    # Constructor

    def __init__(self, name, discord_id, message=None):
        self.name = name
        self.discord_id = discord_id
        if message is None:
            self.chat_log = []
        else:
            if type(message) is str:
                self.chat_log = [{"role": "system", "content": message}]
            else:
                self.chat_log = [message]

    # ---------------------------------------------

    # Getters and Setters

    def get_name(self):
        return self.name

    def get_discord_id(self):
        return self.discord_id

    def get_chat_log(self):
        return self.chat_log

    # ---------------------------------------------

    def set_name(self, name):
        self.name = name

    def set_discord_id(self, discord_id):
        self.discord_id = discord_id

    def set_chat_log(self, conversation):
        self.chat_log = conversation

    # ---------------------------------------------

    # Value is a chat call ({'role': 'system', 'content': 'string'})
    def append_chat_log(self, value):
        self.chat_log.append(value)

    # String representation of the object
    def __str__(self):
        return "Name: " + self.name + ", Discord ID: " + str(self.discord_id) + ", Chat Log: " + str(self.chat_log)

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
