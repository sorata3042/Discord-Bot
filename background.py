import discord
from discord.ext import commands, tasks
from itertools import cycle

class Background(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def test1(self, ctx):
        print ("TEST SUCCESSFUL")
        await ctx.send("TEST SUCCESSFUL")

def setup(client):
    client.add_cog(Background(client))
