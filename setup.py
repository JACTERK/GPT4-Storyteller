import os
import discord
import aiLib
import settings
import time
import asyncio
import random
from dotenv import load_dotenv

load_dotenv()

# First time setup
if True:
    # Changes the value of the line that starts with 'setup = ' to 'True'
    settings.update_variable("setup", "True")
    print("Running first time setup...")

    # Checks if the .env file exists
    if not os.path.exists(".env"):
        print("ERROR: .env file not found. Creating .env file...")
        settings.setup = False

        # Creates .env file
        with open(".env", "w") as f:
            f.write("DISCORD_TOKEN=\n")
            f.write("OPENAI_API_KEY=\n")
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
        print("All variables found in .env file. Continuing...")

    # Asks the user what model they would like to use (default is 'gpt-4') and sets the 'model' variable in settings.py
    model = input("What model would you like to use? Available models are [gpt-4, gpt-3.5-turbo, davinci] (default: "
                  "gpt-3.5-turbo): ").lower()
    if model == "gpt-4" or model == "gpt-3.5-turbo" or model == "davinci":
        settings.update_variable("model_gen", ("'" + model + "'"))
        print("Model set to '" + model + "'.")
    else:
        settings.update_variable("model_gen", "'gpt-3.5-turbo'")
        print("ERROR: Invalid model name. gpt-3.5-turbo will be used in place of '" + model + "'.")

    # Asks the user if they would like to enable image generation
    img_gen = input("Would you like to enable image generation? (y/n) (default: n): ")
    # Yes:
    if img_gen == "y":
        settings.update_variable("generate_images", "True")
        print("Image generation enabled.")
    # No:
    else:
        settings.update_variable("generate_images", "False")
        print("Image generation disabled.")

    settings.promptGenerator()
