import os
import discord
import manga_utils
import asyncio

TOKEN = "MTE3OTk1NTY1NTgxODM1ODk4NQ.G6tS0X.m6J7o6gCq2WZ6QzQJa1B1rOIhcGroxnsA5g0MM"
wave_emoji = ":wave:"

class Secretary(discord.Client):
    async def on_ready(self):
        print("Logged into Discord as ", self.user)
    
intents = discord.Intents.default()
intents.message_content = True
client = Secretary(intents = intents, case_insensitive=True, command_prefix='$')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    #bot @ed
    elif manga_utils.BotAtted(client,message.mentions):
        msg = ""
        if manga_utils.IsGreeting(message.content):
            msg = "Oh, hello " + message.author.name + " " + wave_emoji + "\nHow can I help you?"
        else:
            msg = "sorry, I don't understand that yet."
        await message.channel.send(msg)


@client.command
async def pickARandomManga(client):
    await client.send("Okay! Give me just a minute here, I'm finishing up a Candy Crush Saga level.")
    return

asyncio.run(client.run(TOKEN))