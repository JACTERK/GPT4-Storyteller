import aiLib
import character
import user
import settings
import userlist
import requests
from collections import deque
import time


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

    time.sleep(1)

    # print(t)

    # v = t.talk_to(t)
    # print(v)

    t.save()

    z = character.load("Keanu_Reeves")

    print(z.get_name())


t5()
