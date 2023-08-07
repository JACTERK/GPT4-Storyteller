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
        "Output your response as a python list, with the list laid out like: " + str(character_details) + ". An " +
        "example of a character that you could create is: ['John', 'John is a farmer who lives in Centretown. " +
        "He loves nature, and frequently likes going on walks through nature. He is kind and responds to other " +
        "characters in a kind and relaxed tone.']. " +
        "As additional context, NAME is the name of the character, PERSONALITY is a description of the character, " +
        "and can be anything, as well as " +
        "detailing how the character speaks to others. This is important, as the character will be responding to " +
        "other characters in the game, and the personality will be used to determine how the character responds to " +
        "other characters. The output will be passed into a python eval() function, so make sure that the output is " +
        "a valid python list. Make sure that you only use single quotes in your response, as double quotes will " +
        "cause an error. Make sure you keep the PERSONALITY string to around " + str(settings.desc_gen_len) +
        " charaters.")


# TODO: Add autosaving function (idk save like every 5 minutes or something)

# Function that takes 3 paramters, a name, a description, and a manual mode boolean. If manual mode is true, then
# the user will be prompted to manually input a character. If manual mode is false, then the user will be prompted
# to input a name and a description, and the program will generate a character based on the input.

# TODO: Change name and desc defaults to None, and change the rest of the code to match. Also swap name and desc in
# each of the if statements
# TODO: Fix the character generation fail bug (handle ' and " in the input)
def new(name="", desc="", manual_mode=False, regen=False):
    temp_prompt = character_gen_prompt

    # Checks if a save file exists for the character
    if (name != "" and (os.path.isfile("save/character/" + name.replace(" ", "_").lower() + ".character"))
            and not regen):
        print("Loading character from save file...")
        return load(name)

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
            print("Creating a random character...")

            name = generate_name()
            desc = get_description_from_wikipedia(name)

            if desc is not None:
                temp_prompt += "The character will begenerated with the name " + name + \
                               " and have a personality based on the following decription: " + desc

        # If a name is provided, but no description, generate a character with the provided name and a random
        # Name: YES
        # Description: NO
        elif desc == "" and name != "":
            print("Creating a character with the name " + name + " and a generated personality... ")

            desc = get_description_from_wikipedia(name)
            if desc is not None:
                temp_prompt += ("The character will be generated with the name " + name + ". The character will " +
                                "have a personality based on the following description: " + desc)

            else:
                temp_prompt += ("The character will be generated with the name " + name + ". The character will " +
                                "have a randomly generated personality. ")

        # If a description is provided, but no name, generate a character with the provided description and random name
        # Name: NO
        # Description: YES
        elif desc != "" and name == "":
            print("Creating a character with a random name and " + desc + " personality...")

            name = generate_name()
            temp_prompt += ("The character will be generated with the name " + name + ". The character will have a " +
                            "personality based on " + desc + ". ")

        # If both a name and a description is provided, generate a character with the provided name and description
        # Name: YES
        # Description: YES
        else:
            print("Creating a character with the name " + name + " and a " + desc + " personality...")
            temp_prompt += ("The character will be generated with the name " + name + ". The character will " +
                            "have a personality based on " + desc + ". ")

        # Parse the API output into a list [name, personality]
        parsed_output = ast.literal_eval(generate([{"role": "system", "content": temp_prompt}]))

        if settings.debug:
            print(parsed_output)

        return Character(parsed_output[0], parsed_output[1])

    # Manual generation mode (Third parameter is True)
    else:
        print("Creating a character with manual input...")
        return Character(name, desc)


def generate_name():
    return generate("Output the name of a random famous person. The output "
                    "should only be the name of the person. An example of a "
                    "valid response is: 'John Smith'.", return_type=str)


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


# TODO: Combine load and new functions, they do the same thing.
# Takes a character object 'c' and loads the data from the save file
def load(c):
    # Verify if 'c' is a Character object or a string. Sets the name variable accordingly.
    if type(c) is Character:
        name = c.get_name().replace(" ", "_").lower()
    elif type(c) is str:
        name = c.replace(" ", "_").lower()
    else:
        raise TypeError("Invalid type for attribute (Must be Character or String)")

    # Try to load the character from the save file
    try:
        with open("save/character/" + name.lower() + ".character", "rb") as f:
            return pickle.load(f)
    except Exception as e:
        print("Error loading character object: " + str(e))
        exit(0)


class Character:
    # Constructor

    def __init__(self, name, personality):
        self.name = name.replace("_", " ")
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

    # Value is a chat call ({'role': 'system', 'content': 'string'}), string, or a list of chat calls.
    def append_chat_log(self, value):
        if len(self.get_chat_log()) >= settings.q_len:
            self.chat_log.popleft()

        if type(value) == dict:
            self.chat_log.append(value)
        elif type(value) == str:
            self.chat_log.append({'role': 'system', 'content': value})
        elif type(value) == list:
            for i in value:
                self.chat_log.append(i)
        else:
            raise TypeError("Invalid chat log value type. Type must be string or dictionary.")

    # ---------------------------------------------

    # String representation of the object
    # Print the name, personality, and chat log of the character with deque brackets removed
    def __str__(self):
        return "--------\nName: " + self.name + "\n\nPersonality: \n" + self.personality + "\n\nChat Log: " + \
            str(self.get_chat_log()) + "\n--------\n"

    # TODO: Add a function to make each user that talks to the bot to have their own character object






    def save(self):
        pickle.dump(self, open("save/character/" + (self.name.replace(" ", "_")).lower() + ".character", "wb"))
        if settings.debug:
            print("Saved character to file: " + (self.name.replace(" ", "_")).lower() + ".character")
