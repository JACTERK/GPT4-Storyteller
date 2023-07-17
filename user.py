# Class defining a discord chat user

import ast
import aiLib
import pickle
import settings
from collections import deque
import discord


# Function that takes a string 'name', a discord object 'client' (which can also be a string containing the id of the
# discord user), and an optional string 'message' and returns a user object.
def new(name, client, message=None):
    print("Creating user...")

    # Verify the client is a discord client object
    if client is discord.Client:

        # If a message is provided, add it to the chat log
        if message is not None:
            return User(name, client, message)

        # If no message is provided, create a User object with an empty chat log
        return User(name, client)

    raise("Error: client " + client + " is not a discord client object.")


class User:
    # Constructor
    def __init__(self, name, user_client, message=None):
        self.name = name
        self.user_client = user_client
        if type(message) is str:
            self.chat_log = deque([{"role": "system", "content": message}])
        elif type(message) is dict:
            self.chat_log = deque([message])
        else:
            self.chat_log = deque([])

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
