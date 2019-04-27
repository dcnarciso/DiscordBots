import discord
from discord.ext import commands
import asyncio
import random
import pickle
import os


client = discord.Client()
token = 'MzkzOTE0MzA4NTgyNTcyMDMy.DR8s6A.z3u8Hrp4T_GD74HxgCMp7-iuYBM'

bot = discord.ext.commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name='HUMAN EXTINCTION'))

@client.event
async def on_message(message):
    if message.content.upper().startswith("LESS"):
        await client.send_message(message.channel, 'Did you mean "fewer"?')

    elif message.content.upper().startswith('!FLIP'):
        flip = random.choice(['Heads', 'Tails'])
        await client.send_message(message.channel, flip)

    elif message.content.upper().startswith('DANNY'):
        await client.send_message(message.channel, ':thumbsup:')

    elif message.content.upper().startswith('!GTFO'):
        if message.author.id == '172720442723794944': #'172720442723794944'
            await client.logout()
        else:
            userID = message.author.id
            await client.send_message(message.channel, f"I'm sorry <@{userID}>, I'm afraid I can't do that, bro.")

    elif message.content.upper().startswith('!CATS'):
        await client.send_file(message.channel, 'https://s-i.huffpost.com/gen/3152148/images/o-ANIMALS-FUNNY-facebook.jpg')

    elif message.content.upper().startswith('!MEMBERS'):
        x = len(message.server.members)
        await client.send_message(message.channel, f"There are {x} members on this server")

    if message.content.upper().startswith('!MARCO'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> POLO!" % (userID))

    if message.content.upper().startswith('!SAY'):
        args = message.content.split(' ')
        await client.send_message(message.channel, "%s" % (" ".join(args[1:])))

    if message.content.upper().startswith('!ROLL'):
        args = message.content.split(' ')
        try:
            rolls, limit = map(int, args[1].split('d'))
        except Exception:
            await client.send_message(message.channel, 'Must be NdN, stupid!')
            return
        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        await client.send_message(message.channel, result)

    if message.content.upper().startswith('!GAME'):
        args = message.content.split(' ')
        try:
            await client.change_presence(game=discord.Game(name=(" ".join(args[1:]))))
        except Exception:
            await client.send_message(message.channel, 'Not a valid game, bro.')
            return

    # if message.content.upper().startswith('VERY COOL'):
    #     await client.send_message(message.channel, 'very cool')

    if message.content.upper().startswith('!STOCK'):
        args = message.content.split(' ')
        e = discord.Embed()
        e.set_image(url = 'https://www.google.com/search?q=%s' % (args[1]))
        await client.send_message(message.channel, embed = e)

    #elif "Duel Links" in message:
    #    await client.send_message("[Crickets]")

client.run(token)

#python C:/Users/gibba/Desktop/Python/MyPython/Spambot.py
