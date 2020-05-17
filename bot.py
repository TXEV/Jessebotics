import discord
import json
import os

from discord.ext import commands

client = commands.Bot(command_prefix = "!")
app_version = "2020.05.17.0"

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
async def version(ctx):
    '''displays the bot's version'''
    await ctx.send(app_version)

client.run(os.environ["token"])
