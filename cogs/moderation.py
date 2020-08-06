import discord
import random

from discord.ext import commands
from discord.ext.commands import has_permissions

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    #!clear <amount>: deletes a specified amount of messages in a text channel
    @commands.command()
    @has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=1):
        """Clears chat messages
        Parameters
        ------------
        amount [optional]: Your question that needs an answer. Removes last 1 chat message by default
        """
        amount += 1
        await ctx.channel.purge(limit = amount)
        await ctx.send(f"deleted {amount} messages")

    @clear.error
    async def clear_error(self, error, ctx):
        if isinstance(error, PermissionError):
            await ctx.send("You don't have permission to do that!")

def setup(client):
    client.add_cog(Moderation(client))