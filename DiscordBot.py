import discord, os, sys
from discord.ext import commands

#opens the token text file and reads it to obtain the bot token
def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()
token = read_token()

client = commands.Bot(command_prefix = '!')

#Loads in the various cogs in the cogs folder
if __name__ == "__main__":
    for filename in os.listdir("./cogs"):
        try:
            #checks if the files end in .py and loads them if they are
            if filename.endswith(".py"):
                client.load_extension(f"cogs.{filename[:-3]}")
        except Exception as e:
            print (f"Failed to load extension {filename}", file = sys.stderr)
    print(" All extensions have loaded")
            #traceback.print_exc()

#alters the bots status and activity
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game("A GAME"))
    print("READY.")

@client.command()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")
    print(f"{extension} has been loaded")

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    print(f"{extension} has been unloaded")

@client.command()
async def reload(ctx, extension):
    client.reload_extension(f"cogs.{extension}")
    print(f"{extension} has been reloaded")

client.run(token)
