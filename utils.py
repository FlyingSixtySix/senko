import openai
import tomllib


with open('config.toml', 'rb') as file:
    config = tomllib.load(file)

openai.api_key = config['openai']['key']
command_guilds = config['discord']['ids']['guilds']
