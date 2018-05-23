import discord
from discord.ext import commands
import time

class generalCog:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ping')
    async def ping(self, ctx):
        t1 = time.perf_counter()
        msg1 = await ctx.send("Pong! :ping_pong:")
        t2 = time.perf_counter()
        await msg1.edit(content=msg1.content + f'\nIt took me **{round((t2 - t1)*1000)}ms** to respond.')
        print((t2 - t1) * 1000)
        print(ctx)

def setup(bot):
    bot.add_cog(generalCog(bot))