# Class defining a discord chat user

import ast
import aiLib
import pickle
import settings
from collections import deque
from aiLib import *
import discord
import character


# Function that takes a string 'name', a discord object 'client' (which can also be a string containing the id of the
# discord user), and an optional string 'message' and returns a user object.
def new(name, message=None):
    print("Creating user...")

    # If a message is provided, add it to the chat log
    if message is not None:
        return User(name, message)

    # If no message is provided, create a User object with an empty chat log
    return User(name)


# Takes a character object 'c' and loads the data from the save file
def load(u):
    name = ""

    # Verify if 'c' is a Character object or a string. Sets the name variable accordingly.
    if type(u) is User:
        name = u.get_name().replace(" ", "_")
    elif type(u) is str:
        name = u.replace(" ", "_")
    else:
        raise TypeError("Invalid type for attribute (Must be User or String)")

    # Try to load the character from the save file
    try:
        with open("save/user/" + name.lower() + ".user", "rb") as f:
            return pickle.load(f)
    except Exception as e:
        print("Error loading user object: " + str(e))
        exit(0)


class User:
    # Constructor
    def __init__(self, name, message=None):
        self.name = name
        if type(message) is str:
            self.chat_log = deque([{"role": "system", "content": message}])
        elif type(message) is dict:
            self.chat_log = deque([message])
        else:
            self.chat_log = deque()

    # ---------------------------------------------

    # Getters and Setters

    def get_name(self):
        return self.name

    def get_chat_log(self):
        return self.chat_log

    # ---------------------------------------------

    def set_name(self, name):
        self.name = name

    def set_chat_log(self, conversation):
        self.chat_log = conversation

    # ---------------------------------------------

    # Value is a chat call ({'role': 'system', 'content': 'string'})
    def append_chat_log(self, value):
        if len(self.get_chat_log()) >= settings.q_len:
            self.chat_log.popleft()
            self.chat_log.append(value)
        else:
            self.chat_log.append(value)

    # String representation of the object
    def __str__(self):
        return "--------\nName: " + self.name + "\n\nPersonality: \nNone" + "\n\nChat Log: " + \
            str(self.chat_log) + "\n--------\n"

    # TODO: Add a function to make each user that talks to the bot to have their own character object

    # Save function - Saves user object to a .user file
    def save(self):
        pickle.dump(self, open("save/user/" + (self.name.replace(" ", "_")).lower() + ".user", "wb"))
        if settings.debug:
            print("Saved user to file: " + (self.name.replace(" ", "_")).lower() + ".user")

        # Start a conversation with another character or user. msg is a string or chatcompletion dict.

    def talk_to(self, c, msg=None, return_type=deque):
        temp_chat = deque([])

        # Filetering #

        # If msg is a string, convert it to a chatcompletion dict. If it is a chatcompletion dict, do nothing.
        if type(msg) == str:
            msg = {"role": "user", "content": msg}
        elif type(msg) != dict:
            raise TypeError("Function talk_to() for " + self.get_name() +
                            " Error: Invalid message type. Type must be string or dictionary.")

        # Check to see if 'c' is a character object. If not, raise an error.
        if type(c) != character.Character:
            raise TypeError("Invalid type. Type must be a character.")

        # End Filtering #

        # Function body #

        # Building the prompt
        # Append personality of the character to the chat log.
        temp_chat.append({"role": "system", "content": c.get_personality()})
        # Append the final instructions to the chat log.
        temp_chat.append({"role": "system", "content": (
                "Your task is to make up a response that you think this character would say to the following "
                "conversation. The next message is from the user. Output your response as "
                + c.get_name() + " would say it. "
        )})
        # Append the message from the user to the chat log.
        self.append_chat_log({"role": "user", "content": msg["content"]})

        # Debug
        if settings.debug:
            print("Talking to character...")

        # Combine the chat logs of the two characters
        temp_chat += combine_chat_log(self, c)

        if settings.debug:
            print("Temp chat: " + str(temp_chat))

        # Return the chat log as a deque by default, or as a string or list if specified
        c.append_chat_log({"role": "user", "content": generate(temp_chat, str)})

        return c.get_chat_log()





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
