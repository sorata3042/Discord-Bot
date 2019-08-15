import discord
import time
from discord.ext import commands

#first cog, clears up clutter in main file
class test(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def test(self, ctx):
        print ("TEST SUCCESSFUL")
        time.sleep(0.5)
        await ctx.send("TEST SUCCESSFUL")

    @commands.command()
    async def ping(self, ctx):
        time.sleep(0.5)
        print ("PONG")
        await ctx.send(f"PONG {round(self.client.latency *1000)} ms")

def setup(client):
    client.add_cog(test(client))
