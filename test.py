import discord
from discord.ext import commands

#first cog, clears up clutter in main file
class Tests(commands.Cog):
    def __init__(self, client):
        self.client = client

    #helps with troubleshooting
    @commands.command()
    async def test(self, ctx):
        print ("TEST SUCCESSFUL")
        await ctx.send("TEST SUCCESSFUL")

    #helps determine lag
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"PONG {round(self.client.latency *1000)} ms")



def setup(client):
    client.add_cog(Tests(client))
