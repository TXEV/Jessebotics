import discord
import random

from discord.ext import commands
from discord.ext.commands import has_permissions

class General(commands.Cog):
    def __init__(self, client):
        self.client = client

    #!8ball <question>: answers your questions
    @commands.command(name="8ball")
    async def _8ball(self, ctx, *, question = None):
        """Answers your questions.
        Parameters
        ------------
        question [required]: Your question that needs an answer
        """
        if question == None:
            await ctx.send("Please ask a question")
        else:
            responses = [
                "It is certain.",
                "It is decidedly so.",
                "Without a doubt.",
                "Yes - definitely.",
                "You may rely on it.",
                "As I see it, yes.",
                "Most likely.",
                "Outlook good.",
                "Yes.",
                "Signs point to yes.",
                "Reply hazy, try again.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Very doubtful."
            ]
            await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}")

    #!clear <amount>: deletes a specified amount of messages in a text channel
    @commands.command()
    @has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=5):
        """Clears chat messages
        Parameters
        ------------
        amount [optional]: Your question that needs an answer. Removes last 5 chat messages by default
        """
        amount += 1
        await ctx.channel.purge(limit = amount)
        await ctx.send(f"deleted {amount} messages")

    @clear.error
    async def clear_error(self, error, ctx):
        if isinstance(error, PermissionError):
            await ctx.send("You don't have permission to do that!")

    #!ping: returns bot latency
    @commands.command()
    async def ping(self, ctx):
        """Returns the bot's latency
        """
        await ctx.send(f"Pong! {round(self.client.latency * 1000)}ms")

def setup(client):
    client.add_cog(General(client))
