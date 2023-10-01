# bot.py
import os
import random
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')
INVITE_URL = os.getenv('INVITE_URL')
APPLICATION_ID = os.getenv('APPLICATION_ID')
PUBLIC_KEY = os.getenv('PUBLIC_KEY')

intents = discord.Intents().all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    hello = [
        'Hello, {}.'.format(message.author.name),
        'Good Morning, {}.'.format(message.author.name),
        'Good Evening, {}.'.format(message.author.name)
    ]

    if message.content == 'hello':
        response = random.choice(hello)
        await message.channel.send(response)
        print(response)

client.run(TOKEN)
