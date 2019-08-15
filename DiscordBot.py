import discord
import time
import os
from discord.ext import commands

def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()
token = read_token()

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print("READY.")

@client.command(aliases=["hi", "greetings", "yo"])
async def hello(ctx):
    time.sleep(0.5)
    await ctx.send("GREETINGS.")

@client.command()
async def clear(ctx, amount = 10):
    await ctx.channel.purge(limit = amount)

@client.event
async def on_message(message):
    banned_words = ["fuck", "shit", "kys"]
    for word in banned_words:
        if message.content.count(word) > 0:
            print("BANNED WORD STATED")
            await message.channel.purge(limit=1)
    await client.process_commands(message)

@client.command()
async def mocha(ctx):
    await ctx.send("HERE IS A PHOTO OF THE DESIRED CANINE")
    await ctx.send(file=discord.File('mocha1.jpeg'))

@client.command()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    client.load_extension(f"cogs.{extension}")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

client.run(token)
