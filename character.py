# Class defining a character in the game

# Function Descriptions:
# new(name, desc, manual_mode) - Function that takes 3 paramters, a name, a description, and a manual mode boolean. If
# manual mode is true, then the user will be prompted to manually input a character. If manual mode is false, then the
# user will be prompted to input a name and a description, and the program will generate a character based on the input.

# get_description_from_wikipedia(name) - Function that takes a string 'name' and returns a string containing the
# description of the wikipedia page of the character with the name 'name'. Returns None if the wikipedia page does not
# exist.

# load(character(string)) - Function that takes a string 'character' and returns a character object of the same name.
# Returns None if the character does not exist.

# combine_chat_log(c1, c2) - Function that takes two character objects 'c1' and 'c2' and returns a deque containing
# the chat logs of both characters combined and sorted.

# -- Inside Class Character --

# talk_to(self, c) - Function that takes a character object 'c' and returns a string containing the response of the
# character to the character 'c'.

# save(self) - Function that saves the character object to a file. The file name is the name of the character with
# spaces replaced with '_'.

import ast

import aiLib
from aiLib import *
import pickle
import settings
import wikipediaapi
from user import User
import userlist
from collections import deque

character_details = "[NAME(String), PERSONALITY(string)]"
character_gen_prompt = (
        "You are tasked to make up a character in a real life style game." +
        "Output your response as a python list, with the list laid out like: " + str(character_details) + "An " +
        "example of a character that you could create is: ['John', 'John is a farmer who lives in Centretown. " +
        "He loves nature, and frequently likes going on walks through nature. He is kind and responds to other " +
        "characters in a kind and relaxed tone.']. " +
        "As additional context, NAME is the name of the character, PERSONALITY is a description of the character, " +
        "and can be anything, as long as it details at least 100 words about the character's personality, as well as " +
        "detailing how the character speaks to others. Additionally, DO NOT USE APOSTROPHES IN YOUR RESPONSE. "
)


# TODO: Add autosaving function (idk save like every 5 minutes or something)

# Function that takes 3 paramters, a name, a description, and a manual mode boolean. If manual mode is true, then
# the user will be prompted to manually input a character. If manual mode is false, then the user will be prompted
# to input a name and a description, and the program will generate a character based on the input.

#
def new(name="", desc="", manual_mode=False):
    temp_prompt = character_gen_prompt

    # If the name has more than 5 words, assume that the user has provided a description instead of a name
    if len(name.split(" ")) >= 5:
        desc = name
        name = ""

    # Automatic generation mode (Third parameter is False)
    if not manual_mode:
        # If no name or description is provided, generate a random character
        # Name: NO
        # Description: NO
        if desc == "" and name == "":
            name = generate("Output the name of a random famous person. The output "
                            "should only be the name of the person. An example of a "
                            "valid response is: 'John Smith'.")
            if desc is not None:
                desc = get_description_from_wikipedia(name)
                print("Creating a random character...")
                temp_prompt += "The character will begenerated with the name " + name + \
                               " and have a personality based on the following decription: " + desc

        # If a name is provided, but no description, generate a character with the provided name and a random
        # Name: YES
        # Description: NO
        elif desc == "" and name != "":
            desc = get_description_from_wikipedia(name)
            if desc is not None:
                print("Creating a character with the name " + name + " and a wikipedia based personality... ")
                temp_prompt += ("The character will be generated with the name " + name + ". The character will " +
                                "have a personality based on the following description: " + desc)

            else:
                print("Creating a character with the name " + name + "...")
                temp_prompt += ("The character will be generated with the name " + name + ". The character will " +
                                "have a randomly generated personality. ")

        # If a description is provided, but no name, generate a character with the provided description and a random
        # Name: NO
        # Description: YES
        elif desc != "" and name == "":
            print("Creating a character with a " + desc + " personality...")
            temp_prompt += ("The character will be generated with a random name. The character will have a " +
                            "personality based on " + desc + ". ")

        # If both a name and a description is provided, generate a character with the provided name and description
        # Name: YES
        # Description: YES
        else:
            print("Creating a character with the name " + name + " and a " + desc + " personality...")
            temp_prompt += ("The character will be generated with the name " + name + ". The character will " +
                            "have a personality based on " + desc + ". ")

        # Parse the API output into a list [name, personality]
        x = ast.literal_eval(generate([{"role": "system", "content": temp_prompt}], 'string'))

        if settings.debug:
            print(x)

        return Character(x[0], x[1])

    # Manual generation mode (Third parameter is True)
    else:
        print("Creating a character with manual input...")
        return Character(name, desc)


# Function that gets a description of a person or character from wikipedia and return it as a string.
def get_description_from_wikipedia(name=""):
    # Wikipedia object with a custom user agent
    wiki = wikipediaapi.Wikipedia('character_bot', 'en')

    # Try to get the wikipedia page of the character
    page = wiki.page(name)

    # If the page exists, get the text from the page
    if page.exists():
        t = (page.text.replace('\n', ' '))

        # Returns the entire wikipedia page
        if settings.wiki_gen_long:
            return t
        # Returns the first 2000 characters of the wikipedia page
        else:
            return t[0:2000]
    else:
        print("Character not found")
        return None


# Takes a character object 'c' and loads the data from the save file
def load(c):
    name = ""

    # Verify if 'c' is a Character object or a string. Sets the name variable accordingly.
    if type(c) is Character:
        name = c.get_name().replace(" ", "_")
    elif type(c) is str:
        name = c.replace(" ", "_")
    else:
        raise TypeError("Invalid type for attribute (Must be Character or String)")

    # Try to load the character from the save file
    try:
        with open("save/character/" + name + ".character", "rb") as f:
            return pickle.load(f)
    except Exception as e:
        print("Error loading character: " + str(e))
        exit(0)


# Takes two character objects 's' and 'c' and combines their chat logs into a single chat log.
# The number of loops is based on the length of the first passed in character's chat log. Empty chat log idx's are
# filled with empty chat log entries. Returns a deque of chat log entries.
def combine_chat_log(s, c, return_type=deque):
    combined_chat_log = deque([])

    for i in range(len(s.get_chat_log())):
        # Append 'self' chat at index 'i' to combined_chat_log
        try:
            combined_chat_log.append(s.get_chat_log()[i])
        except IndexError:
            combined_chat_log.append({"role": "system", "content": ""})

        # Append 'c' chat at index 'i' to combined_chat_log
        try:
            combined_chat_log.append(c.get_chat_log()[i])
        except IndexError:
            combined_chat_log.append({"role": "system", "content": ""})

    if return_type == deque or return_type == str or return_type == list:
        return return_type(combined_chat_log)
    else:
        raise TypeError("Invalid return type (Must be deque or str)")


class Character:
    # Constructor

    def __init__(self, name, personality):
        self.name = name
        self.personality = personality
        self.chat_log = deque([])

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

    # Value is a chat call ({'role': 'system', 'content': 'string'})
    def append_chat_log(self, value):
        if len(self.get_chat_log()) >= settings.q_len:
            self.chat_log.popleft()

        if type(value) == dict:
            self.chat_log.append(value)
        elif type(value) == str:
            self.chat_log.append({'role': 'system', 'content': value})
        else:
            raise TypeError("Invalid chat log value type. Type must be string or dictionary.")

    # ---------------------------------------------

    # String representation of the object
    # Print the name, personality, and chat log of the character with deque brackets removed
    def __str__(self):
        return "Name: " + self.name + ", Personality: " + self.personality + "\nFull chat log: " + \
            str(self.chat_log)[6:len(str(self.chat_log)) - 1]

    # TODO: Add a function to make each user that talks to the bot to have their own character object

    # Start a conversation with another character or user
    def talk_to(self, c):
        n = 0
        # Check to see if 'c' is a character or a user
        if self == c:
            raise AttributeError("Cannot talk to self.")

        if type(c) == Character:
            if settings.debug:
                print("Talking to character...")
            # Combine the chat logs of the two characters
            temp_chat = combine_chat_log(self, c)






        elif type(c) == User:
            if settings.debug:
                print("Talking to user...")

        # If 'c' is neither a character nor a user, exit the program
        else:
            raise TypeError("Invalid type. Type must be a character or a user.")

        # Check to see which chat log is longer

        if len(self.chat_log) >= len(c.chat_log):
            n = len(self.chat_log)
        else:
            n = c.chat_log

        for i in self.chat_log:
            print()

        return n

    def save(self):
        pickle.dump(self, open("save/character/" + self.name.replace(" ", "_") + ".character", "wb"))
        if settings.debug:
            print("Saved character to file: " + self.name.replace(" ", "_") + ".character")
