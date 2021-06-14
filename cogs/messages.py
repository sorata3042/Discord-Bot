#Steven Chau

import discord
from discord.ext import commands

class Messages(commands.Cog):
    def __init__(self, client):
        self.client = client

    #aliases are alternate commands that can be used to trigger this function
    @commands.command(aliases=["hi", "greetings", "yo"])
    async def hello(self, ctx):
        await ctx.send("GREETINGS.")

    #deletes part of the chat history
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount = 10):
        await ctx.channel.purge(limit = amount)


    @commands.command()
    async def yah(self, ctx):
        await ctx.send("YEET")

    @commands.command()
    async def yee(self, ctx):
        await ctx.send("haw")

#Was causing the bot to perfrom tasks twice will troubleshoot
"""    @commands.Cog.listener()
    async def on_message(self, message):
        banned_words = ["fuck", "shit", "kys"]
        for word in banned_words:
            if message.content.count(word) > 0:
                print("BANNED WORD STATED")
                await message.channel.purge(limit=1)
        await self.client.process_commands(message)"""

def setup(client):
    client.add_cog(Messages(client))
