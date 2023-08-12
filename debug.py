import aiLib
import character
import settings
#import server
from collections import deque
import time
import os
import discord


def t1():
    p = aiLib.generate([{"role": "system", "content": "hello"}])
    print(p)
    return


def t2():
    a = {"role": "user", "content": "hello"}
    b = {"role": "system", "content": "hello"}

    c = [a, b]

    print(c)


def t3():
    a = {"role": "user", "content": "hello"}
    b = {"role": "system", "content": "hello"}

    John = character.new("John", "Make him a nice ice cream shop owner with a dark side...")
    print(John.get_name())


def t4():
    a = {"role": "user", "content": "hello"}
    b = {"role": "system", "content": "hello"}

    u = userlist.Userlist()

    u.add_user(user.new("Phil", 123456))

    u.add_user(user.new("Dan", 123458, "asdasdasd"))

    print(u.get_user_list_as_string())


def t5():
    # s = (character.generate_character_from_wikipedia("Keanu Reeves"))

    t = character.new("Keanu Reeves", "Keanu reeves is a farmer", True)
    u = character.new("John", "John is a farmer", True)

    t.append_chat_log({"role": "user", "content": "what is your name, and what do you do?"})
    u.append_chat_log({"role": "system", "content": "You are a farmer named john."})

    t.append_chat_log({"role": "user", "content": "what is your time?"})

    # print(t)

    # v = t.talk_to(t)
    # print(v)

    # t.save()

    # z = character.load("Keanu_Reeves")

    # print(z.get_name())

    x = character.combine_chat_log(t, u)

    print(t.get_chat_log()[0]["content"])

    s = [{"role": "system", "content": "hello"}, {"role": "user", "content": "hello2"}]

    d = deque[{"role": "system", "content": "hello3"}]

    print(list(d) + s)


def t6():
    print("t6")
    t = character.new("Keanu Reeves", "Keanu reeves is a farmer", True)
    u = character.new("John", "John is a farmer", True)

    t.append_chat_log({"role": "user", "content": "what is your name, and what do you do?"})
    u.append_chat_log({"role": "user", "content": "You are a farmer named john."})

    # Test function

    p1 = ("You are tasked in coming up with a response that you think " + t.get_name() +
          " would say. For reference, " + t.get_name() + " is described in the following way: " + t.get_personality() +
          ". You can use that description to assist in responding like " + t.get_name() + " accurately. " +
          "What would you say as a response to the following conversation with " + u.get_name() + "? For reference, " +
          u.get_name() + " is described in the following way: " + u.get_personality() + ".")

    temp_prompt = [{"role": "system", "content": p1}]

    temp_prompt += (character.combine_chat_log(t, u))

    print(temp_prompt)

    print(aiLib.generate(temp_prompt, str))


def t7():
    print("t7")
    h = "1"

    if h.isnumeric():
        print("h is numeric")


def t8():
    # Define Discord client
    intents = discord.Intents.default()
    intents.message_content = True

    discord_client = discord.Client(intents=intents)

    myUser = user.new("Jacob", discord_client)
    myCharacter = character.new("Post_Malone")

    print(myUser)
    print(myCharacter)

    n = "Hey!"

    # myUser.append_chat_log({"role": "user", "content": n})

    # Calls talk_to function in character.py - returns a string and updates chatlog
    print(myUser.talk_to(myCharacter, msg=n))

    print(myCharacter.get_chat_log())
    print(myUser.get_chat_log())




# Make the program loop. make a tui too.
def t9():
    print("t9")
    option = input("Would you like to create a new character? (y/n): ").lower()
    if 'y' in option:
        print("Yes")


    elif 'n' in option:
        print("No")

        does_save_exist = False

        # Checks if any save file(s) exists
        for i in os.listdir("save/character"):
            if ".character" in i:
                does_save_exist = True

        if does_save_exist:
            print()

        else:
            print("Error: No .character files found. Please create a new character.")


def t10():
    print("t10")
    print(len(1023123))



t10()
