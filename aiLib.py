# Made with <3 by Jacob Terkuc

import os
import openai
import settings
import time
import asyncio
from dotenv import load_dotenv
from datetime import datetime

# Load Discord and OpenAI API keys
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
openai.api_key = os.getenv("OPENAI_API_KEY")


# Function to generate response
def generate_message(prompt):
    # Debug
    if settings.debug_mode:
        print(prompt)

    # Generate Response using Chat API
    response = openai.ChatCompletion.create(model=settings.model_gen, messages=prompt)

    # Return response
    return response


# Function to generate an image from a prompt
def generate_image(imagedict):
    # Generate image
    try:
        url = openai.Image.create(prompt=imagedict["prompt"], n=1, size="1024x1024")

        imagedict["url"] = url["data"][0]["url"]

        print("Image generated: " + url)

        imagedict["pass"] = True

    except Exception as e:
        print(f"Image Gen Failed: {e}")
        imagedict["pass"] = False

    return imagedict


# Takes a list q_q and a string message, and adds the new message to the beginning of the queue.
def enqueue(q_q, message):
    # If q_q length is greater than or equal to the value configured in settings, pop the first index.
    if len(q_q) >= settings.q_len:
        q_q.popleft()

    # Append new message onto the end of q_q
    q_q.append(message)

    return q_q


# Takes two lists q_h (user) and q_b (bot) and generates the prompt to be passed onto API
def promptBuilder(q_u, q_b):
    # Prompt builder for GPT 3
    if settings.model_gen == "davinci":
        print("GPT 3 (Davinci) being used.")

        prompt = settings.prompt + "\n"

        # Loop for each message in the user queue
        for x in range(len(q_u)):
            prompt += "\nUser: "
            prompt += q_u[x]
            prompt += "\n" + settings.trigger_name + ": "
            prompt += q_b[x - 1]

        # Add final prompt
        prompt += "\n\nUser: "
        prompt += q_u[(len(q_u) - 1)]

        prompt += "\n\n" + settings.trigger_name + ": "

        return prompt

    # Prompt builder for GPT 4
    if settings.model_gen == "gpt-4":
        print("GPT 4 being used.")

        prompt = [{"role": "system", "content": settings.prompt}]

        # Loop for each message in the user queue
        for x in range(len(q_u) - 1):
            prompt.append({"role": "user", "content": q_u[x]})
            prompt.append({"role": "assistant", "content": q_b[x]})

        # Add final prompt
        prompt.append({"role": "user", "content": q_u[len(q_u) - 1]})

        return prompt


def log_gen(log_data):
    file_name = 'logfile.log'

    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    formatted_data = f'{current_time} - {log_data}'

    with open(file_name, 'a') as log_file:
        log_file.write(formatted_data + '\n')
    return


def generate_typetime(message):
    return len(message) / settings.t_speed_multiplier
