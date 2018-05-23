import discord
from discord.ext import commands
import os.path

import sys, traceback

def getPrefix(bot, message):
    prefixes = ['`']

    if not message.guild:
        return "?"
    return commands.when_mentioned_or(*prefixes)(bot, message)

#list of cogs files

bot = commands.Bot(commands_prefix = getPrefix, description = 'Bill\'s gambling bot') #bot creation

for ext in os.listdir('Bill Bot/cogs'):
    if not ext.startswith(('_', '.')):
        bot.load_extension('Bill Bot.cogs.' + ext[:-3])  # Remove '.py'


@bot.event()
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.run('NDQ0NzIwNzk2ODI1Mjg4NzA0.DdgKuw._DfF3XRmzNkfsqPcqYKVPOvRCd4', bot = True, reconnect = True)
