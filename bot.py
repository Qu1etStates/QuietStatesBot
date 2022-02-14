import discord
import os
from discord.ext import commands
# import json
import keep_alive

client = commands.Bot(command_prefix="$")

@client.event
async def on_ready():
    print(f"{client.user} is online :)")
    await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name="twitch.tv/KodineLIVE"))

@client.command()
async def test(ctx, message):
    message = "gib kodine prim"
    testEmbed(title=None, description="The **test** command has been executed successfully.\n\n*Test Message: {message}", color=0xFAACE8)
    await ctx.send(embed=testEmbed)




keep_alive.keep_alive()
login = os.environ["BOT_TOKEN"]
client.run("OTQyOTE3Mjk3NDgyMzcxMTAy.YgreKg.RYEV2cqnExhVhQ7tfjiY_YOnFSI")