# server.py - Server class

from collections import deque
import os
import pickle
import settings


def new(server_name, server_id):
    # Checkers
    if type(server_name) != str:
        raise AttributeError("Error creating Server object: Invalid 'server_name' type " +
                             str(type(server_name)).split(" ")[1][:-1])

    if len(server_name) > 0:
        raise AttributeError("Error creating Server object: server_name is empty")

    # Verify if 'server_id' is an integer. Return if not.
    if type(server_id) != int:
        raise AttributeError("Error creating Server object: Invalid 'server_id' type " +
                             str(type(server_id)).split(" ")[1][:-1])

    if server_id is None:
        raise AttributeError("Error creating Server object: server_id is empty")

    return Server(server_name, server_id)


# Loads a server 's' from a file
def load(s):
    # Verify if 's' is an object or a string. Return if neither.
    match s:
        case Server():
            name = s.get_server_name().replace(" ", "_").lower()
        case str():
            name = s.replace(" ", "_").lower()
        case _:
            raise AttributeError("Error loading Server object: Invalid type " + str(type(s)).split(" ")[1][:-1])

    # Try to load the character from the save file
    try:
        with open("save/character/" + name.lower() + ".character", "rb") as f:
            return pickle.load(f)
    except Exception as e:
        print("Error loading character object: " + str(e))
        exit(0)


# Server class
class Server:
    # Class definition
    def __init__(self, server_name, server_id):
        self.server_name = server_name
        self.server_id = server_id
        self.chat_log = deque([])

    # ----------------------------------------

    # Getters

    def get_server_name(self):
        return self.server_name

    def get_server_id(self):
        return self.server_id

    def get_chat_log(self):
        return self.chat_log

    # Setters

    def set_server_name(self, server_name):
        self.server_name = server_name

    def set_server_id(self, server_id):
        self.server_id = server_id

    def set_chat_log(self, chat_log):
        self.chat_log = chat_log

    # ----------------------------------------

    def __str__(self):
        return "Server object: " + self.get_server_name() + " (" + str(self.get_server_id()) + ")"

    # Methods

    def append_chat_log(self, message):
        # Pop oldest message if queue is full
        if len(self.chat_log) >= settings.q_len:
            self.chat_log.popleft()

        # Append new message
        if type(message) == dict:
            self.chat_log.append(message)
        elif type(message) == str:
            self.chat_log.append({'role': 'system', 'content': message})
        elif type(message) == list:
            for i in message:
                self.chat_log.append(i)
        else:
            raise TypeError("Invalid chat log message type. Type must be string or dictionary.")

        self.chat_log.append(message)

    def save(self):
        pickle.dump(self, open(str(settings.server_dir) + (self.get_server_name().replace(" ", "_")).lower() +
                                str(settings.server_extension), "wb"))
        if settings.debug:
            print("Saved character to file: " + (self.get_server_name().replace(" ", "_")).lower() +
                  settings.server_extension)
