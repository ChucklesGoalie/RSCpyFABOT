from .games import Games
from .fa import CheckIn


def setup(bot):
    bot.add_cog(CheckIn(bot))
    bot.add_cog(Games(bot))