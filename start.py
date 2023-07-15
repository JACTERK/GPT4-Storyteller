# Made with <3 by Jacob Terkuc

import os
import discord
from aiLib import *
import settings
import time
import asyncio
import random
from dotenv import load_dotenv

# Load Discord API Key
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# Define Discord client
intents = discord.Intents.default()
intents.message_content = True

discord_client = discord.Client(intents=intents)

# Queues used to manage memory
queue_user = [""]
queue_bot = [""]

# TODO: Pass message into chatgpt and use the fucntion generator to call the discord api
'''
So the idea is basically, you should be able to create new bots inside of discord, allow the user to base it off a real 
person (who's data will be gathered from wikipedia) and the bot will respond to messages in the same way that the person
would. each bot running in the script will be appended by its name in square brackets, and will respond to the specific 
user who was talking to it. 
'''


# Message indicating if the bot is connected to Discord servers
@discord_client.event
async def on_ready():
    print(
        f"{discord_client.user} has connected to Discord servers. Use keyword ["
        + settings.trigger_name
        + "] to trigger. "
    )


'''
# Message event
@discord_client.event
async def on_message(message):
    # Load queues
    global queue_user
    global queue_bot

    # Don't respond to self
    if message.author == discord_client.user:
        return

    # Don't respond to other bots
    if message.author.bot:
        return

    # Detects for words "imagine" or "draw", as well as the trigger name and generates an image
    elif (
            settings.trigger_name in message.content.lower()
            and ("imagine " or "draw ") in message.content.lower()
    ):

        # Create image generation dictionary to store data
        imageDict = {"pass": False, "prompt": message.content.split("imagine")[1], "url": ""}

        # Send to OpenAI
        imageDict = aiLib.generate_image(imageDict)

        if imageDict["pass"]:
            await message.channel.send("Ok, here is your picture.")
            await message.channel.send(imageDict["url"])
            return
        elif not imageDict["pass"]:
            await message.channel.send("I can't draw that, sorry.")

    # Generates message when trigger word is detected
    elif settings.trigger_name in message.content.lower():
        msg = message.content

        # Enqueue new user message
        enqueue(queue_user, msg)

        print("Generating new message")

        # Determine Response requires a completed prompt to be passed into it to work properly. This builds the
        # prompt then passes it into the function.
        resp = generate_message(promptBuilder(queue_user, queue_bot))

        print("Done!")

        # Enqueue new bot response
        enqueue(queue_bot, resp["choices"][0]["message"]["content"])

        # Checks to see if the message has any text, and if it does, it will send it to the server after waiting a
        # specified amount of time.
        if len(resp) > 1:
            await asyncio.sleep(
                random.randrange(settings.time_to_wait_min, settings.time_to_wait_max)
            )

            print("Sending message to channel...")

            async with message.channel.typing():
                await asyncio.sleep(generate_typetime(resp))

            await message.channel.send(resp["choices"][0]["message"]["content"] + " ")

            print("Done!")

        # If nothing is generated, send default response.
        else:
            await message.channel.send(settings.default_response)

        return
'''


@discord_client.event
async def on_message(message):
    return


print("Starting bot...")

# Run discord bot instance
discord_client.run(DISCORD_TOKEN)
