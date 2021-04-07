import discord
from discord.ext import commands, tasks



class CheckIn(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(aliases=["ci"])
    async def CheckIn(self, ctx):
        user : discord.Member
        fa = await discord.utils.get(ctx.guild.role, name="fa")
        amateur = await discord.utils.get(ctx.guild.role, name="amateur")
        contender = await discord.utils.get(ctx.guild.role, name="contender")
        prospect = await discord.utils.get(ctx.guild.role, name="prospect")
        challenger = await discord.utils.get(ctx.guild.role, name="challenger")
        minor = await discord.utils.get(ctx.guild.role, name="minor")
        major = await discord.utils.get(ctx.guild.role, name="major")
        elite = await discord.utils.get(ctx.guild.role, name="elite")
        master = await discord.utils.get(ctx.guild.role, name="master")
        premier = await discord.utils.get(ctx.guild.role, name="premier")

        if fa is amateur:

        if fa is contender:

        if fa is prospect:

        if fa is challenger:

        if fa is minor:
        
        if fa is major:

        if fa is elite:
        











