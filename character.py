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

    return Character(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7])


class Character:
    # Constructor

    def __init__(self, name, role, personality, health, attack, defense, inventory, location):
        self.name = name
        self.role = role
        self.personality = personality
        self.oai_personality = {"role": "system", "content": personality}
        self.health = health
        self.attack = attack
        self.defense = defense
        self.inventory = inventory
        self.location = location
        self.chat_log = {}

    # Getters and Setters

    def get_name(self):
        return self.name

    def get_role(self):
        return self.role

    def get_personality(self):
        return self.personality

    def get_health(self):
        return self.health

    def get_attack(self):
        return self.attack

    def get_defense(self):
        return self.defense

    def get_inventory(self):
        return self.inventory

    def get_location(self):
        return self.location

    def get_chat_log(self):
        return self.chat_log

    def set_name(self, name):
        self.name = name

    def set_role(self, role):
        self.role = role

    def set_personality(self, personality):
        self.personality = personality

    def set_health(self, health):
        self.health = health

    def set_attack(self, attack):
        self.attack = attack

    def set_defense(self, defense):
        self.defense = defense

    def set_inventory(self, inventory):
        self.inventory = inventory

    def set_location(self, location):
        self.location = location

    def set_chat_log(self, conversation):
        self.chat_log = conversation

    # Key is a character, value is a chat call ({'role': 'system', 'content': 'string'})
    def add_to_chat_log(self, key, value):
        self.chat_log[key].append(value)

    # String representation of the object
    def __str__(self):
        return "Entity: " + self.name + ", Role: " + self.role + ", Personality: " + self.personality + ", Health: " + str(
            self.health) + ", Attack: " + str(self.attack) + ", Defense: " + str(self.defense) + ", Inventory: " + str(
            self.inventory) + ", Location: " + str(self.location)

    # TODO: Add a function to make each user that talks to the bot to have their own character object


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
