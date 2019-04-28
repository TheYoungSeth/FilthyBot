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

    if message.content == "ffrank":
        with open('Me.png', 'rb') as me:
            ranks = "You too good for this planet :D ur already god mode", "U succ in every perspective. it can't be helped", "yo alrighty", "..."
            await client.send_message(message.channel, random.choice(ranks))

    if message.content == "ffmeme":
        memes = "filthymemes/meme1.png", "filthymemes/meme2.png", "filthymemes/meme3.png", "filthymemes/meme4.png", "filthymemes/meme5.png", "filthymemes/meme6.png", "filthymemes/meme7.png", "filthymemes/meme8.png", "filthymemes/meme9.png", "filthymemes/meme10.jpg", "filthymemes/meme11.jpg", "filthymemes/meme12.jpg", "filthymemes/meme12.gif"
        await client.send_file(message.channel, random.choice(memes))

    if message.content == "ffhelp":
        helps = discord.Embed(title="Da Filthy Commands", description='ffstop - will stoping you \n ffrank - Will rank you \n ffmeme - some filthy memes \n ffhelp - this.', url="https://www.youtube.com/user/TVFilthyFrank", color=discord.Colour.gold())
        await client.send_message(message.channel, embed=helps)

@client.event
async def on_member_join(member):
    joins = [member, "it mah puss"]
    await client.send_message(client.get_channel("568874563551756303"), joins]

client.run("NTcxNzM3NTc0Njc1MzE2NzQ3.XMSGgw.rdr8GNOsk51QPvOPm06V2bUR9k8")
