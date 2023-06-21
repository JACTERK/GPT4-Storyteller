import os
import discord
import aiLib
import settings
from dotenv import load_dotenv
import asyncio


def testA():
    q_u = []
    q_b = []

    q_u = aiLib.enqueue(q_u, "hello")
    q_b = aiLib.enqueue(q_b, "i am a bot")

    q_u = aiLib.enqueue(q_u, "oh ok")
    q_b = aiLib.enqueue(q_b, "i am a bot yes")

    q_u = aiLib.enqueue(q_u, "2213")
    q_b = aiLib.enqueue(q_b, "gdfgdf")

    q_u = aiLib.enqueue(q_u, "6565")
    q_b = aiLib.enqueue(q_b, "sadasdasd")

    prompt = aiLib.promptBuilder(q_u, q_b)

    # print(prompt)

    return


def testB():
    s = "a cool thing"
    b = s.split("cool")[1]

    print(b)


async def testC():
    timer = aiLib.ResettableTimer(settings.q_expire)
    await asyncio.gather(
        asyncio.sleep(3),
        timer.reset(),
        asyncio.sleep(5),
        timer.stop()
    )



s = "a red car that is falling off a cliff with the hollywood sign behind it."

#print(aiLib.generate_Image(s))

# testA()
#testB()


