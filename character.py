# Class defining a character in the game

import ast
from aiLib import *
import pickle
import settings
import wikipediaapi

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


# Function that takes 3 paramters, a name, a description, and a manual mode boolean. If manual mode is true, then
# the user will be prompted to manually input a character. If manual mode is false, then the user will be prompted
# to input a name and a description, and the program will generate a character based on the input.

#
def new(name="", desc="", manual_mode=False):
    print("Creating character...")
    temp_prompt = character_gen_prompt

    # If the name has more than 5 words, assume that the user has provided a description instead of a name
    if len(name.split(" ")) >= 5:
        desc = name
        name = ""

    # Automatic generation mode
    if not manual_mode:
        # If no name or description is provided, generate a random character
        if desc == "" and name == "":
            print("Creating a random character...")
            temp_prompt += "The character will be randomly generated with a random personality and a random name. "

        # If a name is provided, but no description, generate a character with the provided name and a random
        elif desc == "" and name != "":
            p = generate_character_from_wikipedia(name)
            if p is not None:
                print("Creating a character with the name " + name + " and a wikipedia based personality... ")
                temp_prompt += ("The character will be generated with the name " + name + ". The character will " +
                                "have a personality based on " + p + ". ")

            else:
                print("Creating a character with the name " + name + "...")
                temp_prompt += ("The character will be generated with the name " + name + ". The character will " +
                                "have a randomly generated personality. ")

        # If a description is provided, but no name, generate a character with the provided description and a random
        elif desc != "" and name == "":
            print("Creating a character with a " + desc + " personality...")
            temp_prompt += ("The character will be generated with a random name. The character will have a " +
                            "personality based on " + desc + ". ")

        # If both a name and a description is provided, generate a character with the provided name and description
        else:
            print("Creating a character with the name " + name + " and a " + desc + " personality...")
            temp_prompt += ("The character will be generated with the name " + name + ". The character will " +
                            "have a personality based on " + desc + ". ")

    # Manual generation mode
    else:
        print("Creating a character with manual input...")
        temp_prompt += desc

    # Parse the API output into a list [name, personality]
    x = ast.literal_eval(generate([{"role": "system", "content": temp_prompt}], 'string'))

    if settings.debug:
        print(x)

    return Character(x[0], x[1])


def generate_character_from_wikipedia(name=""):
    wiki = wikipediaapi.Wikipedia('character_bot', 'en')
    page = wiki.page(name)

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



class Character:
    # Constructor

    def __init__(self, name, personality):
        self.name = name
        self.personality = personality
        self.chat_log = [{'role': 'system', 'content': "Respond to questions in the following manner: " + personality}]

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
