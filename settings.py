# Made with <3 by Jacob Terkuc


# --------------------- Basic Config --------------------- #

# Debug mode (Prints extra information to console)
debug = True

# Trigger name (Name that will trigger the bot in discord)
trigger_name = "Keanu Reeves"


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

# Character object storage directory
character_dir = "save/character"
character_extension = ".character"


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
