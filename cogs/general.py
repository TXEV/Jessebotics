import discord
import requests
import random
import os
import json

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

    #!ping: returns bot latency
    @commands.command()
    async def ping(self, ctx):
        """Returns the bot's latency
        """
        await ctx.send(f"Pong! {round(self.client.latency * 1000)}ms")

    #!weather: retrieve current weather data
    @commands.command()
    async def weather(self, ctx, area="Surrey, CA", unit="celsius"):
        """Retrieves current weather
         Parameters
        ------------
        area [optional]: The city (default to Surrey, CA)
        unit [optional]: The unit to display the temperature in (default to celsius)
        """

        if not(unit == "celsius") and not(unit == "c") and not(unit == "fahrenheit") and not(unit == "f") and not(unit == "kelvin") and not(unit == "k"):
            await ctx.send(f"cannot display temperature as {unit}")
            return

        r = None
        success = None
        data = None

        def format_weather_message(f_area, f_temp, f_unit, f_weather):
            return f"Current Weather Forecast:\n{f_area}: {f_temp}{f_unit}\n{f_weather}"

        try:
            r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={area}&appid=" + os.environ["openweathermapkey"])
            success = True
            data = json.loads(r.text)
        except:
            await ctx.send("Failed to retrieve weather data")
        
        if success == True:
            temp_k = int(round(data["main"]["temp"]))
            temp_c = int(round(temp_k - 273.15))
            temp_f = int(round(temp_k * 9 / 5 - 459.67))
            current_weather = data["weather"]["0"]["main"]
            current_area = data["name"] + " " + data["sys"]["country"]

            if unit == "celsius" or unit == "c":
                await ctx.send(format_weather_message(current_area, temp_c, "ºC", current_weather))
            elif unit == "fahrenheit" or unit == "f":
                await ctx.send(format_weather_message(current_area, temp_f, "ºF", current_weather))
            else:
                await ctx.send(format_weather_message(current_area, temp_k, "ºK", current_weather))

def setup(client):
    client.add_cog(General(client))
