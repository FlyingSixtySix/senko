from discord.ext import bridge, commands
import discord
from discord import option
import random

from concurrent.futures import ThreadPoolExecutor

from utils import command_guilds


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    def _roll_dice(self, sides: int):
        return str(random.randint(1, sides))

    @bridge.bridge_command(guild_ids=command_guilds, description='Rolls dice')
    @option(name='dice', description='Number of dice to roll')
    @option(name='sides', description='Number of sides on each die')
    async def roll(self, ctx: bridge.BridgeContext, dice: int = 1, sides: int = 999):
        if dice < 1:
            return await ctx.respond('You cannot roll less than 1 die.')
        if sides < 2:
            return await ctx.respond('You cannot roll a die with less than 2 sides.')
        if dice > 2000:
            return await ctx.respond('You cannot roll more than 2000 die at once.')
        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(self._roll_dice, sides) for _ in range(dice)]

            rolls = [future.result() for future in futures]
        response = 'You rolled: **' + '**, **'.join(rolls) + '**'
        if len(response) > 2000:
            response = response[:1996] + ' ...'
        await ctx.respond(response)

    @commands.command(description='Says something as the bot')
    async def sudo(self, ctx: commands.Context, *, message: str):
        await ctx.send(message)


def setup(bot):
    bot.add_cog(Fun(bot))
