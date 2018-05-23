import discord
from discord.ext import commands

import sys, traceback

def getPrefix(bot, message):
    prefixes = ['`']

    if not message.guild:
        return "?"
