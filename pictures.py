import discord, os, sys, random
from discord.ext import commands

class Pictures(commands.Cog):
    def __init__(self, client):
        self.client = client

    #the following commands send images from a designated folder
    @commands.command()
    async def mocha(self, ctx):
        mocha_images = []
        for filename in os.listdir("./Mocha"):
            mocha_images.append(filename)
        #chooses a random image from multiple in the folder
        chosen_image = random.choice(mocha_images)
        await ctx.send("Mocha \n", file=discord.File("./Mocha/" + chosen_image))

    @commands.command()
    async def billy(self, ctx):
        billy_images = []
        for filename in os.listdir("./Billy"):
                billy_images.append(filename)
        chosen_image = random.choice(billy_images)
        await ctx.send("Billy \n", file=discord.File("./Billy/" + chosen_image))

def setup(client):
    client.add_cog(Pictures(client))
