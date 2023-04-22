from discord.ext import commands
import discord

from utils import config, command_guilds


class Meta(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Logged in as {self.bot.user} ({self.bot.user.id})')
        activity = discord.Activity(type=discord.ActivityType[config['discord']['activity']['type']], name=config['discord']['activity']['name'])
        await self.bot.change_presence(activity=activity)

    @commands.slash_command(guild_ids=command_guilds)
    async def ping(self, ctx):
        await ctx.respond('https://tenor.com/view/cat-pong-catpong-cats-funny-gif-4777918')


def setup(bot):
    bot.add_cog(Meta(bot))
