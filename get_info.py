from   discord.ext import commands
import discord

from prettytable import PrettyTable as PT
from tqdm        import tqdm
from rich        import inspect

import json











# Loads the config
with open('config.json') as f:
    config:dict = json.load(f)




intents = discord.Intents.default()
intents.members = True
bot     = commands.Bot(intents=intents)






@bot.event
async def on_ready():
    table = PT()
    table.field_names = ['Name', 'Count', 'Owner']

    count = 0
    # Get info of all the guilds
    async for guild in bot.fetch_guilds():
        count += 1
        # for some reason, fetch_guild does not give back the member count
        actual_guild = bot.get_guild(guild.id)
        table.add_row([ str(actual_guild.name) , actual_guild.member_count , str(actual_guild.owner) ])

    table.sortby      = 'Count'
    table.reversesort = True
    print(table)
    print(f'\nTotal: {count} servers')
    
    await bot.close()







bot.run(config['token'])




