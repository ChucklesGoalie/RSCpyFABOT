import discord
from discord.ext import commands, tasks
import json
import time
from datetime import datetime as dt

from pathlib import Path

class CheckIn(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def ci_test(self, ctx):
        await ctx.send("This Cog works")

    @commands.command(aliases=["ci"])
    async def CheckIn(self, ctx):
        author = ctx.author
        user = discord.Member
        fa =  discord.utils.get(ctx.guild.roles, name="fa")
        amateur =  discord.utils.get(ctx.guild.roles, name="amateur")
        contender =  discord.utils.get(ctx.guild.roles, name="contender")
        prospect =  discord.utils.get(ctx.guild.roles, name="prospect")
        challenger = discord.utils.get(ctx.guild.roles, name="challenger")
        minor =  discord.utils.get(ctx.guild.roles, name="minor")
        major =  discord.utils.get(ctx.guild.roles, name="major")
        elite = discord.utils.get(ctx.guild.roles, name="elite")
        master = discord.utils.get(ctx.guild.roles, name="master")
        premier = discord.utils.get(ctx.guild.roles, name="premier")
        data = json.dumps({str(author) : dt.isoformat(dt.utcnow())+"+00:00"})
        filename=None

        if not fa:
            await ctx.send("You are not an FA")
            return

        if amateur:
            filename="amateurCI.json"
            
        if contender:
            filename="contenderCI.json"

        if prospect:
            filename="prospectCI.json"

        if challenger:
            filename="challengerCI.json"
            
        if minor:
            filename="minorCI.json"
            
        if major:
            filename="majorCI.json"
            
        if  elite:
            filename="eliteCI.json"
            
        if master:
            filename="masterCI.json"
            
        if premier:
            filename="premierCI.json"

        existing_CI = json.loads(Path(filename).read_text())
        
        if existing_CI.get(str(author)):
            existing_CI(str)

        Path(filename).write_text(data)
        await ctx.send("You are checked in!")
        return






