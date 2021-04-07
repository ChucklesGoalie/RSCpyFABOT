import discord
from discord.ext import commands, tasks
import random


class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong!\nThe bot took {round(commands.Bot.latency * 1000)}ms to respond.')


    @commands.command(aliases=['8Ball', '8ball'])
    async def _8ball(self, ctx, *, question):
        responses = ['It is certain',
                    'You may rely on it',
                    'Yes definitely',
                    'Ask again Later',
                    'Concentrate and ask again',
                    'Cannot predict now',
                    'No',
                    'Dont count on it',
                    'Very doubtful']
        embed = discord.Embed(
            colour = discord.Colour.purple())
        embed.set_author(name='This is 8Ball, Let this bot decide on Yes or no questions for you!')
        embed.add_field(name=(f'{question}'), value=(f'{random.choice(responses)}'), inline=False)
        await ctx.send(embed=embed)


    @commands.command(aliases=['CoinToss', 'Coin_Toss'])
    async def cointoss(self, ctx, *, question):
        lst = question.split(", ")
        embed = discord.Embed(
            colour = discord.Colour.purple())
        embed.set_author(name='Help : list of commands available')
        embed.add_field(name='Values (Heads) (Tails):', value=(f'{question}\n'), inline=False)
        embed.add_field(name='Answer:', value=(f'{random.choice(lst)}'), inline=False)
        await ctx.send(embed=embed)
