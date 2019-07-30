import random

import discord
from discord.ext.commands import Bot
import references
from discord.ext import commands

client = Bot(command_prefix="ff")

@client.event
async def on_ready():
    print("loading...")
    games = "with Pink Guy", "with myself"
    await client.change_presence(game=discord.Game(name=random.choice(games)))
    print("loaded!")

@client.event
async def on_message(message):
    if message.content == "ffstop":
        stop = "Its time to STOP! Its time to stop, ok? NO MORE!", "This-This-This is NOT OK! This needs to stop, NOW! This is CANCER! This is so much cancer, that I can feel the tumors Growing on my BACK!"
        await client.send_message(message.channel, random.choice(stop))

    if message.content == "ffrank":
        ranks = "U succ in every perspective. it can't be helped", "yo alrighty", "...", "your gay"
        await client.send_message(message.channel, random.choice(ranks))

    if message.content == "ffmeme":
        memes = "filthymemes/meme1.png", "filthymemes/meme2.png", "filthymemes/meme3.png", "filthymemes/meme4.png", "filthymemes/meme5.png", "filthymemes/meme6.png", "filthymemes/meme7.png", "filthymemes/meme8.png", "filthymemes/meme9.png", "filthymemes/meme10.jpg", "filthymemes/meme11.jpg", "filthymemes/meme12.jpg", "filthymemes/meme12.gif"
        await client.send_file(message.channel, random.choice(memes))

    if message.content == "ffhelp":
        helps = discord.Embed(title="Da Filthy Commands", description='ffstop - will stop you \n ffrank - Will rank you \n ffmeme - some filthy memes \n ffhelp - this.\n ffask - ask some stupid questions  \n WARNING! I am a bad programmer... You need to write lowercase ff, everything else wont work ;-;', url="https://www.youtube.com/user/TVFilthyFrank", color=discord.Colour.gold())
        await client.send_message(message.channel, embed=helps)

    if message.content.startswith("ffask"):
        answers = "yes", "no", "maybe", "eventually", "Ask Derpy, he is stupid enough for this question", "hah lol **no**", "I...I-I don't even know anymore...", "What the fuck do you think?", "I don't know man...seems kinda gay to me." "What are you, fucking gay?", "As sure as I'm filthy.", "Yeah...", "Hell no...", "...Ok...", "Uh...yeah..."
        await client.send_message(message.channel, random.choice(answers))

    if message.content.startswith("ffgreet"):
            await client.send_message(message.channel, "hello bitch named " + client.get_user_info(message.content))

@client.event
async def on_member_join(member):
    client.send_message(member, "Yo whaddup bitch called " + member.name + "and welcome to autism 100")
    role = discord.utils.get(member.server.roles, name="test")
    await client.add_roles(member, role)

client.run("NTcxNzM3NTc0Njc1MzE2NzQ3.XMSGgw.rdr8GNOsk51QPvOPm06V2bUR9k8")
