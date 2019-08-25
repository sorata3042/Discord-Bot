import discord, os, sys, random
from discord.ext import commands

class Pictures(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def mocha(self, ctx):
        mocha_images = []
        for filename in os.listdir("./Mocha"):
            mocha_images.append(filename)
        await ctx.send("Mocha")
        chosen_image = random.choice(mocha_images)
        await ctx.send(file=discord.File("./Mocha/" + chosen_image))

    @commands.command()
    async def billy(self, ctx):

        billy_images = []
        for filename in os.listdir("./Billy"):
                billy_images.append(filename)
        await ctx.send("Billy")
        chosen_image = random.choice(billy_images)
        await ctx.send(file=discord.File("./Billy/" + chosen_image))

def setup(client):
    client.add_cog(Pictures(client))
