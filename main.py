import discord
import asyncio
import time
from discord.ext import commands

bot = commands.Bot(command_prefix = "`")

"""""
@bot.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == Server.get_member(405190503970111488):
        await bot.say("HighRTT土豆，烂到发臭")
"""""

@bot.command(pass_context = True, name = 'ping')
async def ping(ctx):
    t1 = time.perf_counter()
    msg1 = await bot.say("Pong! :ping_pong:")
    t2 = time.perf_counter()
    await bot.edit_message(msg1, f"Pong! :ping_pong:\nIt took me **{round((t2 - t1)*1000)}ms** to respond.")
    print ((t2 - t1)*1000)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.run('NDQ0NzIwNzk2ODI1Mjg4NzA0.DdgKuw._DfF3XRmzNkfsqPcqYKVPOvRCd4')