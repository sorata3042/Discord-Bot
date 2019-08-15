import discord, youtube_dl
from discord.ext import commands
from discord.utils import get

class Audio(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def join(self, ctx):
        global voice
        channel = ctx.message.author.voice.channel
        voice = get (self.client.voice_clients, guild = ctx.guild)

        await ctx.send (f"The bot has joined the channel: {channel}")
        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()

    @commands.command(pass_context=True)
    async def leave(self, ctx):
        channel = ctx.message.author.voice.channel
        voice = get (self.client.voice_clients, guild = ctx.guild)

        if voice and voice.is_connected():
            await voice.disconnect()
            print (f"The bot has left the channel: {channel}")
            await ctx.send(f"Left {channel}")
        else:
            print (f"Unable to perform action")
            await ctx.send(f"The bot is unable to leave {channel}")

    @commands.command(pass_context=True)
    async def play(self, ctx, url):
        pass


def setup(client):
    client.add_cog(Audio(client))
