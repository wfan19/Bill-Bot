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

bot = commands.Bot(command_prefix = getPrefix, description = 'Bill\'s gambling bot') #bot creation

"""
#Derek's fancy cog finder
for ext in os.listdir('Bill Bot/cogs'):
    if not ext.startswith(('_', '.')):
        bot.load_extension('Bill Bot.cogs.' + ext[:-3])  # Remove '.py'
"""

initial_extensions = ['cogs.general',
                                 'cogs.seven']

#Eviee way of loading cogs (More manual)
if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.run(Key, bot = True, reconnect = True)
