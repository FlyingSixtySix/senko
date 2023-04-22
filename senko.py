from discord.ext import bridge
from discord import Intents
import os

from utils import config

intents = Intents.default()
intents.guild_messages = True
intents.message_content = True
bot = bridge.Bot(command_prefix=config['discord']['prefix'], intents=intents)
bot.config = config

for f in os.listdir('cogs'):
    if f.endswith('.py'):
        bot.load_extension(f'cogs.{f[:-3]}')

bot.run(config['discord']['token'])
