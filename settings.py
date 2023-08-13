# Made with <3 by Jacob Terkuc

# ----------------- First Time Setup ---------------------- #

# Change this value to 'True' if you have already configured the bot.
setup = True

# --------------------- Basic Config --------------------- #

# Debug mode (Prints extra information to console)
debug = True

# Trigger name (Name that will trigger the bot in discord)
trigger_name = "Keanu Reeves"

<<<<<<< HEAD
prompt = ""
default_response = "Sorry, I don't understand."

default_prompt = "Your name is " + trigger_name + ". You are a kind person who responds to questions in a " + \
                 "friendly, smart, and polite manner. You like to call people 'buddy' and 'pal'." \
                 "You like to lie about most things you talk about, and become angry and defensive when people try" \
                 " to push back on you. "
=======
>>>>>>> remove_userlist_py

# ---------------------- Bot Config ---------------------- #

# Queue length (Number of messages that will be queued)
q_len = 3

# Minimum/maximum time between messages (in seconds, [min, max])
time_to_wait = [0, 1]

# Typing speed multiplier (The lower the number, the slower the bot will type)
t_speed_multiplier = 0.5


# ------------ Descriptiopn Generation Config ------------ #

# Description generation length (in characters)
# Will cost around $0.03 to generate a single description at 1200 characters.
desc_gen_len = 1200

# Default wikipedia scrape length (in characters)
wiki_scrape_len = 2000

# Wikipedia Long Generation (Warning: Setting to True will consume a lot of credits)
wiki_gen_long = False


# ------------------ Directory Settings ------------------ #
# Server object storage directory
server_dir = "save/server"
server_extension = ".server"

<<<<<<< HEAD
# True: Generate images
# False: Disable image generation

generate_images = False

# -------------------------------------------------------- #

debug_mode = True
=======
# Character object storage directory
character_dir = "save/character"
character_extension = ".character"
>>>>>>> remove_userlist_py


# ------------------- Helper Functions ------------------- #
# Function that takes the name of a variable, and changes the variable at the line that starts with the variable name in
# settings.py to the value of the variable 'value'
def update_variable(variable, value):
    # Open settings.py in read mode
    with open("settings.py", "r") as file:
        # Read all lines from settings.py
        lines = file.readlines()
        # Iterate through each line
        for i in range(len(lines)):
            # Check if the line starts with the variable name
            if lines[i].startswith(variable):
                # If it does, replace the line with the variable name and the value
                lines[i] = variable + " = " + value + "\n"
    # Open settings.py in write mode
    with open("settings.py", "w") as file:
        # Write all lines to settings.py
        file.writelines(lines)
    print("Prompt updated. ")


<<<<<<< HEAD
# Function that is used to generate a prompt using GPT 4. Function takes the string 'trigger_name' from settings.py
# and a list of strings 'list', and returns a string 'prompt'
# list = [adj1, adj2, adj3, adj4, desc1, truth]
#         [0],  [1],  [2],  [3],  [4],   [5]
def promptGenerator():
    # Prompts user in terminal to enter the trigger name
    templist = []
    t_name = input("Enter the trigger name (default: john): ")
    if t_name != "":
        update_variable("trigger_name", ("'" + t_name + "'"))
    else:
        update_variable("trigger_name", "'john'")

    # Asks user if they want to use default prompt, or generate a new one
    t_prompt = input("Use default prompt? (y/n) (default: y): ")
    if t_prompt == "n":
        # Asks the user if they want to use the prompt builder, or enter the prompt manually.
        # User wants to use prompt builder
        if input("Use prompt builder? (y/n) (default: n): ") == "y":
            print("Answer the following prompts: ")
            templist.append(input("You are a _____ person: "))

            for i in range(1, 3):
                templist.append(input("You respond to questions in a _____ manner (" + str(i) + "/3): "))

            templist.append(input("You like to _____: "))

            # Asks user if they want to lie or tell the truth
            if input("Do you want to lie or tell the truth? (l/t): ") == "l":
                templist.append(True)
            else:
                templist.append(False)

        else:
            # User wants to enter prompt manually
            update_variable("prompt", ("'" + (input("Enter prompt: ")) + "'"))

    # User wants to generate a new prompt
    else:
        update_variable("prompt", "'" + default_prompt + "'")
        exit()

    # String 'p' used to store string to get passed into gpt-4
    p = "Your name is " + trigger_name + ". You are a " + templist[0] + \
        " person who responds to questions in a " + templist[1] + ", " + templist[2] + ", and " + \
        templist[3] + " manner. You like to " + templist[4] + ". You "

    # Checks if list[5] is True
    if templist[5]:
        p += "like to lie about most things you talk about, and become angry and defensive when people try to push " \
             "back on you."
    else:
        p += "tell the truth and are respectful to people you meet."

    # Updates the prompt in settings.py
    update_variable("prompt", ("'" + p + "'"))
    exit()
=======
# TODO: Remove this function
# Function that takes the name of a variable, and returns the value of the variable at the line that starts with the
# variable name in settings.py
def get_value(variable):
    # Open settings.py in read mode
    with open("settings.py", "r") as file:
        # Read all lines from settings.py
        lines = file.readlines()
        # Iterate through each line
        for i in range(len(lines)):
            # Check if the line starts with the variable name
            if lines[i].startswith(variable):
                # If it does, replace the line with the variable name and the value
                return lines[i].split(" = ")[1].replace("\n", "")
>>>>>>> remove_userlist_py
