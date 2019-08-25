import discord, youtube_dl, os
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
    async def play(self, ctx, *, url):
        song = os.path.isfile("song.mp3")
        try:
            if song:
                os.remove("song.mp3")
                print ("Removed old song file")
        except PermissionError:
            await ctx.send ("Error: Music Playing")

        await ctx.send ("Queuing the song")

        voice = get (self.client.voice_clients, guild=ctx.guild)

        ydl_opts = {
        "default_search": "auto",
        "format": "bestaudio/best",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
            }],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            print("Downloading mp3 file")
            ydl.download([url])

        for filename in os.listdir("./"):
            if filename.endswith(".mp3"):
                song_name = filename
                os.rename(filename, "song.mp3")

        source = discord.FFmpegPCMAudio("song.mp3")
        voice.play(source, after = lambda e: print (f"{song_name} has finished playing"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 0.5

        #new_song_name = filename.replit("-", 2)
        #await ctx.send(f"Playing {new_song_name}")

def setup(client):
    client.add_cog(Audio(client))
