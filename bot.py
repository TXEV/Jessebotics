import discord
import json
import os

from discord.ext import commands

client = commands.Bot(command_prefix = "!")

for filename in os.listdir('./cogs'):
    if filename.endswith(".py"):
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
async def reload(ctx, extension):
    """Reloads a section of the commands and updates bot."""
    client.unload_extension(f"cogs.{extension}")
    client.load_extension(f"cogs.{extension}")

    print("Reloaded all commands")

client.run(process.env.token)
