import discord
from discord.ext import commands, tasks
import random
import time
from cogs import Games, CheckIn

client = commands.Bot(command_prefix = "?")

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('Predicting your questions'))
    client.add_cog(Games(client))
    client.add_cog(CheckIn(client))
    print("RSCpyBOT is currently running")

@client.event
async def on_command_error(ctx, error):
    user : discord.Member
    await ctx.send(f'Error. ({error})')
    print(f'[{user.guild}]', f'{time.strftime(("[%d/%m/%Y, %I:%M:%S %p ET]"))}', error)


#We delete default help command
client.remove_command('help')
#Embeded help with list and details of commands
@client.command(pass_context=True)
async def help(ctx):

    embed = discord.Embed(
        colour = discord.Colour.purple())
    embed.set_author(name='Help : list of commands available')
    embed.add_field(name='cointoss', value='Flip a coin and see where it lands', inline=False)
    embed.add_field(name='8ball', value='Ask 8Ball a yes or know question and let it decide for you!', inline=False)
    await ctx.send(embed=embed)



client.run('NzQyNzc5MDg1OTE0Mzc0MzQ2.XzLE7g.FwibJ4Sh4YxVWb2bSmWaiopBGKs')
