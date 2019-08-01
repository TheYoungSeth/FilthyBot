import random

import discord
from discord.ext.commands import Bot
import references
from discord.ext import commands

client = Bot(command_prefix="ff")

@client.event
async def on_ready():
    print("loading...")
    await client.change_presence(game=discord.Game(name="STFU - Pink Guy", type=3), status=discord.Status.idle)
    print("loaded!")

@client.event
async def on_message(message):
    if message.content.lower() == "ffstop":
        stop = "Its time to STOP! Its time to stop, ok? NO MORE!", "This-This-This is NOT OK! This needs to stop, NOW! This is CANCER! This is so much cancer, that I can feel the tumors Growing on my BACK!"
        await client.send_message(message.channel, random.choice(stop))

    if message.content.lower() == "ffrank":
        ranks = "U succ in every perspective. it can't be helped", "yo alrighty", "...", "your gay"
        await client.send_message(message.channel, random.choice(ranks))

    if message.content.lower() == "ffmeme":
        memes = "/home/pi/Desktop/FilthyBot/filthymemes/meme1.png", "/home/pi/Desktop/FilthyBot/filthymemes/meme2.png", "/home/pi/Desktop/FilthyBot/filthymemes/meme3.png", "/home/pi/Desktop/FilthyBot/filthymemes/meme4.png", "/home/pi/Desktop/FilthyBot/filthymemes/meme5.png", "/home/pi/Desktop/FilthyBot/filthymemes/meme6.png", "/home/pi/Desktop/FilthyBot/filthymemes/meme7.png", "/home/pi/Desktop/FilthyBot/filthymemes/meme8.png", "/home/pi/Desktop/FilthyBot/filthymemes/meme9.png", "/home/pi/Desktop/FilthyBot/filthymemes/meme10.jpg", "/home/pi/Desktop/FilthyBot/filthymemes/meme11.jpg", "/home/pi/Desktop/FilthyBot/filthymemes/meme12.jpg", "/home/pi/Desktop/FilthyBot/filthymemes/meme12.gif"
        await client.send_file(message.channel, random.choice(memes))

    if message.content.lower() == "ffhelp":
        helps = discord.Embed(title="Da Filthy Commands", description='ffstop - will stop you \nffrank - Will rank you \nffmeme - some filthy memes \nffhelp - this. \nffask - ask some stupid questions', url="https://www.youtube.com/user/TVFilthyFrank", color=discord.Colour.gold())
        await client.send_message(message.channel, embed=helps)

    if message.content.lower().startswith("ffask"):
        answers = "yes", "no", "maybe", "eventually", "Ask Derpy, he is stupid enough for this question", "hah lol **no**", "I...I-I don't even know anymore...", "What the fuck do you think?", "I don't know man...seems kinda gay to me." "What are you, fucking gay?", "As sure as I'm filthy.", "Yeah...", "Hell no...", "...Ok...", "Uh...yeah..."
        await client.send_message(message.channel, random.choice(answers))
        
@client.event
async def on_member_join(member):
    channel = client.get_channel("568874563551756303")
    await client.send_message(channel, "Welcome " + member.mention + " to **Derpy Boi's Hang Out**! Be sure to read <#568874640567697448>, <#584506223592865822> and make sure to go to <#582791862881091605> to get some roles!\nTry to have some fun or don't. I don't give a flying fuck...")
    role = discord.utils.get(member.server.roles, name="Standard Bois")
    await client.add_roles(member, role)
    
@client.event
async def on_member_remove(member):
    channel = client.get_channel("568874563551756303")
    await client.send_message(channel, "Well **" + member.name + "** left. I hated him anyway...")
    
@client.event
async def on_message_delete(message):
    logs_channel = client.get_channel("606206039179788348")
    embed_log = discord.Embed(title=message.author.name + " has deleted his message", colour=discord.Colour.gold())
    embed_log.add_field(name="Message", value=message.content, inline=False)
    await client.send_message(logs_channel, embed=embed_log)
    
@client.event
async def on_message_edit(before, after):
    logs_channel = client.get_channel("606206039179788348")
    if before.bot:
        print("bot smh")
    else:
        embed_log = discord.Embed(title=before.author.name + " edited his message", colour=discord.Colour.gold())
        embed_log.add_field(name="before", value=before.content, inline=False)
        embed_log.add_field(name="after", value=after.content, inline=False)
        await client.send_message(logs_channel, embed=embed_log)
        
@client.event
async def on_member_update(before, after):
    if before.bot:
        print('bot smh')
    else:
        logs_channel = client.get_channel("606206039179788348")
        await client.send_message(logs_channel, "**" + before.name + "** changed his name to **" + after.nick + "**")
    
@client.event
async def on_member_ban(guild, user):
    logs_channel = client.get_channel("606206039179788348")
    await client.send_message(logs_channel, "**" + user.name + "** got banned from **" + guild.name + "**")
    
@client.event
async def on_member_unban(guild, user):
    logs_channel = client.get_channel("606206039179788348")
    await client.send_message(logs_channel, "**" + user.name + "** got unbanned from **" + guild.name + "**")

client.run(TOKEN)
