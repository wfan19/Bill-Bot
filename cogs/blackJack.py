import discord
from discord.ext import commands
import asyncio
import random

class blackJackCog:
    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command= True,
                  aliases = ['bj'])
    async def bj(self,ctx):
        print(ctx)
        await self.problem.callback(self, ctx)

    @bj.commands
    @commands._has_permissions(embed_links = True)
    async def problem(self, ctx):
        outEmbed = discord.Embed()
        outEmbed.color = discord.Color.dark_red()
        outEmbed.title = "How to play Blackjack"
        outEmbed.description = \
            "~~Seriously? You don't know how to play Blackjack?" \
            "\nBlackjack is a casino classic."



    @bj.command()
    async def start(self,ctx):
        global deck, dealerHand, hand
        deck = [((i % 13) + 1) for i in range(52)] #creates deck of 1-13 x 4
        dealerHand = []
        await ctx.send("Dealing...")
        await asyncio.sleep(1.5)
        hand = [self.deal() for i in range(2)]
        await ctx.send(f'Your hand is:{(",".join(hand))}')

    def deal(self,):
        return deck.remove(random.randint(0,len(deck)-1))




def setup(bot):
            bot.add_cog(blackJackCog(bot))






