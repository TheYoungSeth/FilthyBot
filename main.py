import random

import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform

client = Bot(command_prefix="ff")

@client.event
async def on_ready():
    print("loading...")
    games = "with the ass flute", "with the nose flute"
    await client.change_presence(game=discord.Game(name=random.choice(games)))
    print("loaded!")

@client.event
async def on_message(message):
    if message.content == "ffstop":
        stop = "Its time to STOP! Its time to stop, ok? NO MORE!", "This-This-This is NOT OK! This needs to stop, NOW! This is CANCER! This is so much cancer, that I can feel the tumors Growing on my BACK!"
        await client.send_message(message.channel, random.choice(stop))

client.run("NTcxNzM3NTc0Njc1MzE2NzQ3.XMSGgw.rdr8GNOsk51QPvOPm06V2bUR9k8")
