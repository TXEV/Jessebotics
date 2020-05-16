import discord
import json
import os

from discord.ext import commands
from discord.ext.commands import has_permissions

config = None # no value set until config.json is read
all_cogs = None # no value set until all cogs are loaded

with open("private/config.json") as json_file:
    config = json.load(json_file)

client = commands.Bot(command_prefix = "!")

for filename in os.listdir('./cogs'):
    if filename.endswith(".py"):
        all_cogs = filename[:-3]
        client.load_extension(f"cogs.{filename[:-3]}")

#
# Events
#
@client.event
async def on_ready():
    print("Hello World!")

#
# Commands
#
@client.command()
async def reload(ctx):
    """Reloads all commands and updates bot."""
    for extension in all_cogs:
        client.unload_extension(f"cogs.{extension}")
        client.load_extension(f"cogs.{extension}")

    print("Reloaded all commands")

client.run(config["token"])
