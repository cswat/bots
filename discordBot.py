#python3

import asyncio
import discord
from logposting import create_logpost

token = discord_token

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    
@client.event
async def on_message(message):
    if '!crab' in message.content:
        await client.send_message(message.channel, "https://youtu.be/LDU_Txk06tM?t=18")
        await client.add_reaction(message, u"\U0001F980")
    if '!riseup' in message.content:
        await client.add_reaction(message, u"\U0001F0CF")
    if message.content.startswith('!logpost'):
        logpostText = message.content
        logpostText = logpostText.replace('!logpost', '')
        print(logpostText)
        create_logpost(logpostText)
        logpath = path_to_logpost
        await client.send_file(message.channel,logpath)
    await client.add_reaction(message, u"\U0001F44D")

client.run(token)
