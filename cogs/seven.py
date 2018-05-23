import discord
from discord.ext import commands
import random
import asyncio

class sevenCog:
    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command = True,
                        aliases = ['7'])
    async def seven(self, ctx):
            """
            llist of subcommands:
                seven bet - params: bet val, under/over/at
                seven help - no params
            """
            print(ctx)
            await self.problem.callback(self,ctx)

    @seven.command()
    @commands.has_permissions(embed_links = True)
    async def problem(self, ctx):
            outEmbed = discord.Embed()
            outEmbed.color = discord.Color.dark_grey()
            outEmbed.title = "How to play:"
            outEmbed.description = "The game's simple. Two dice will be rolled, and their sum taken. You will try to bet if the sum will be over, at, or under 7. "
            outEmbed.add_field(name = "That's great, how do I join?",
                                              value = "Use command ``seven bet <bet>` to play the game.\nReplace `<bet>` with \"over\" to bet over 7, \"at\" for at 7, and \"under\" for under 7")
            outEmbed.add_field(name = "How much money do I win?",
                                              value = "If you win and your bet wasn't **\"at seven\"**, you'll get **double** your bet back. If you win and your bet was **\"at seven\"**, you will get **four times** your bet back")

            await ctx.send(embed = outEmbed)
            print('problem')

    global m2
    m2 = ""

    @seven.command()
    async def roll(self,ctx, bet: str):
            # bet is betting under, at, or above
            # val is the amount you're betting
            # game betting on if result will be over or under 7
            m1 = await ctx.send(":game_die:Rolling...:game_die:")
            d1 = random.randint(1, 6)
            d2 = random.randint(1, 6)
            await asyncio.sleep(1.5)

            if d1 + d2 == 7 and bet == 'seven':
                m2 = "Congratulations! Here's **quadruple** your original bet. Play again?"
            elif (d1 + d2 < 7 and bet == "under") or (d1 + d2 > 7 and bet == "over"):  # Checks if you're right
                m2 = "You were right! Here's double your original bet. Play again?"
            else: #if you're wrong:
                m2 = "Sorry, but you were wrong. Play again?"

            m3 = await m1.edit(content = m1.content + f"\nI rolled a {d1} and a {d2}, which adds up to a {d1 + d2}\n" + m2)

def setup(bot):
    bot.add_cog(sevenCog(bot))
