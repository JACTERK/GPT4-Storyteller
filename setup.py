import os
import discord
import aiLib
import settings
import time
import asyncio
import random
from dotenv import load_dotenv
import character

# TODO: Allow user to make changes and edit character objects
# TODO: allow user to add keys in the command line to make it easier to get through first time startup

load_dotenv()


# Environment checker
def check_env_file():
    print("\n\nChecking environment variables...")

    # Checks if the .env file exists
    if not os.path.exists(".env"):
        print("ERROR: .env file not found. Creating .env file...")

        # Creates .env file
        with open(".env", "w") as f:
            f.write("DISCORD_TOKEN=\n")
            f.write("OPENAI_API_KEY=")
            f.close()
        print("Created .env file. Please fill in the required variables and restart the bot.")
        exit()

    # Checks if the 'DISCORD_TOKEN' variable is set in the .env file
    if os.getenv("DISCORD_TOKEN") is None:
        print("ERROR: Discord API token not found in .env file.")
        exit()

    # Checks if the 'OPENAI_API_KEY' variable is set in the .env file
    if os.getenv("OPENAI_API_KEY") is None:
        print("ERROR: OpenAI API key not found in .env file.")
        exit()

    # Checks if both the 'DISCORD_TOKEN' and 'OPENAI_API_KEY' variables are set in the .env file
    if os.getenv("DISCORD_TOKEN") is not None and os.getenv("OPENAI_API_KEY") is not None:
        print("All variables found in .env file.")

    return


# Character creator
def create_character():
    print("\n-------------------------\nCharacter Creation Wizard\n-------------------------\n")
    print("This wizard will guide you through the process of creating a character.\n")
    print("You will be asked to enter a name and description for your character.\nIf you leave the name field"
          "blank, the name arguement will be automatically generated.\nIf you leave the description field blank, "
          "the description arguement will be automatically generated.\n"
          "Press q to quit at any time.\n")

    # Get character name from user input
    character_name = input("Please enter a name for your character "
                           "(Enter a name or leave blank to create a random character: ")

    if character_name == 'q':
        return

    # Get character description from user input
    character_description = input("Please enter a description for your character: "
                                  "(Enter a description or leave blank to create a random description: ")

    if character_description == 'q':
        return

    # Create character object
    tempCharacter = character.new(character_name, character_description)

    # Print character object
    print("Character created. Details below: ")
    print(tempCharacter)

    # Save character object
    s = input("Would you like to save your character? (y/n): ").lower()
    if 'y' in s:
        # Save character object
        tempCharacter.save()

        # Update/set character name in settings
        settings.update_variable("trigger_name", ('"' + str(tempCharacter.get_name()) + '"'))
        print("Character saved.")

    elif 'n' in s:
        print("Character not saved.")

    return


# Character loader
def load_character():
    # Checks if any save file(s) exists
    does_save_exist = False
    for i in os.listdir("save/character"):
        if ".character" in i:
            does_save_exist = True

    if not does_save_exist:
        print("Error: No .character files found. Please create a new character.")
        return

    # Below is run if save file(s) exist
    character_file_names = os.listdir("save/character")
    temp_name_list = []
    c_passed = False

    print("\n\nSelect one of the following characters:\n")

    # Append only .character file names to list and format them (remove .character and replace _ with spaces)
    for i in character_file_names:
        if ".character" in i:
            temp_name_list.append(i.replace(".character", "").replace("_", " ").upper())

    # Print list to allow user to select character
    for i in range(len(temp_name_list)):
        if len(temp_name_list[i]) > 0:
            print("[" + str(i + 1) + "] [" + temp_name_list[i] + "]")

    # Loops user input until a valid option is selected from the menu.
    while not c_passed:
        c_choice = input("\nSelection: ")

        if 'q' in c_choice.lower():
            return

        # Checks if input is numeric
        if c_choice.isnumeric():
            c_choice = int(c_choice)
            passed = False

            # Tries to load character from file.
            # Passes when character is loaded.
            if c_choice <= len(temp_name_list) or c_choice <= 0:
                print("Trying to load " + temp_name_list[c_choice - 1] + "...")
                try:
                    # Load character from file
                    temp_character = character.load(temp_name_list[c_choice - 1].replace(" ", "_").lower())
                    print("Successfully loaded " + temp_character.get_name() + "!")

                    # Update/set character name in settings
                    settings.update_variable("trigger_name", ('"' + str(temp_character.get_name()) + '"'))
                    c_passed = True

                    return

                except Exception as e:
                    print("Error: " + str(e))
                    c_passed = False

            else:
                print("Invalid input. Please try again.")

        else:
            print("Invalid input. Please try again.")


# Bot launcher
def launch_bot():
    print("Launching bot...")


# Main Function

# Loops user input until a valid option is selected from the menu.
print("-----------------\nStoryteller Setup\n-----------------")
print("It is recommended to run all these commands \nbefore starting the bot.\n")
passed = False

while not passed:
    print("\n\nSelect one of the following options: \n")

    print("[1] Check .env file ")
    print("[2] Create Character ")
    print("[3] Load Character ")
    print("[4] Launch Bot ")
    print("[5] Exit ")

    choice = input("\nEnter the number of the option you would like to select: ")

    # Checks if input is numeric
    if choice.isnumeric():
        choice = int(choice)
        passed = False

        # Selector for the menu options
        match choice:
            case 1:
                check_env_file()
            case 2:
                create_character()
            case 3:
                load_character()
            case 4:
                launch_bot()
            case 5:
                print("Exiting...")
                exit()
            case _:
                print("Invalid input. Please try again.")

    else:
        print("Invalid input. Please try again.")
