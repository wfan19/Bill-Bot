import discord
import asyncio
import time
import random
from discord.ext import commands

bot = commands.Bot(command_prefix = "`")


@bot.command(pass_context = True, name = 'ping')
async def ping(ctx):
    t1 = time.perf_counter()
    msg1 = await bot.say("Pong! :ping_pong:")
    t2 = time.perf_counter()
    await bot.edit_message(msg1, f"Pong! :ping_pong:\nIt took me **{round((t2 - t1)*1000)}ms** to respond.")
    print ((t2 - t1)*1000)

"""
@bot.listen()
async def on_message(message):
    if message.author.id == "405190503970111488":
        #print ("I should be saying potato stuff")
        if(random.uniform(0,1) < 0.5):
            await bot.send_message(message.channel, "HighRTT土豆，烂到发臭!")
        else:
            await bot.send_message(message.channel, "HighRTT这个厦门猴子，写个代码都不会")

    if message.author.id == "444188992468942858":
        await bot.send_message(message.channel, "Jimbot more like TrashBot amirite bois")
"""

@bot.command(pass_context = True)
async def roll(ctx, faces: int):
    numb = random.randint(1, faces)
    out = f"You rolled a **{numb}**! Play again?"
    await bot.say(out)

@bot.command(pass_context = True,
             aliases=['7']
             )
async def seven(ctx, bet: str):
    #bet is betting under, at, or above
    #val is the amount you're betting
    #game betting on if result will be over or under 7
    await bot.say(":game_die:Rolling...:game_die:")
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    await asyncio.sleep(1.5)
    m1 = await bot.say(f"I rolled a {d1} and a {d2}, which adds up to a {d1 + d2}")
    m2 = ""
    if d1+d2 == 7 and bet == 'seven':
        m2 = "Congratulations! Here's **quadruple** your original bet. Play again?"
    elif (d1+d2 > 7 and bet == "under") or (d1+d2 < 7 and bet == "over"): #Checks if you're wrong
        m2 = "Sorry, but you were wrong. Play again?"
    elif (d1 + d2 < 7 and bet == "under") or (d1 + d2 > 7 and bet == "over"):  #Checks if you're right
        m2 = "You were right! Here's double your original bet. Play again?"
    await bot.edit_message(m1, f"I rolled a {d1} and a {d2}, which adds up to a {d1 + d2}\n{m2}")


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.run('NDQ0NzIwNzk2ODI1Mjg4NzA0.DdgKuw._DfF3XRmzNkfsqPcqYKVPOvRCd4')