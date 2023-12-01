import os, asyncio
import discord
from discord.ext import commands
from discord.ext.commands import cooldown, BucketType
import manga_utils, manga_picking

TOKEN = "MTE3OTk1NTY1NTgxODM1ODk4NQ.G6tS0X.m6J7o6gCq2WZ6QzQJa1B1rOIhcGroxnsA5g0MM"
wave_emoji = ":wave:"
    
intents = discord.Intents.default()
intents.message_content = True
intents.emojis = True

secretary = commands.Bot(command_prefix='>', intents=intents)

@secretary.event
async def on_message(message):
    if message.author == secretary.user:
        return
    
    #bot @ed
    elif manga_utils.BotAtted(secretary, message.mentions):
        msg = ""
        if manga_utils.IsGreeting(message.content):
            msg = "Oh, hello " + message.author.name + " " + wave_emoji + "\nHow can I help you?"
        else:
            msg = "sorry, I don't understand that yet."
        await message.channel.send(msg)

    await secretary.process_commands(message)

@secretary.command(name = 'pick')
async def PickARandomManga(ctx, *, arg):
    print("picking manga")
    msg = manga_picking.ParseSelectionType()
    #await ctx.send("Okay! Give me just a minute here, I'm finishing up a Candy Crush Saga level.")
    await ctx.send("Alright, I've set the club's new manga. Here's the details")
    await ctx.send(msg)

@secretary.command(name = 'schedule')
async def ScheduleMeeting(ctx, date, time):
    #await ctx.send("Okay, I've added the " + date + " meeting to the books.")
    pass

@secretary.command(name='cancel')
async def CancelMeeting(ctx):
    await ctx.send("Got it. Next meeting has been cancelled.")

    pass

asyncio.run(secretary.run(TOKEN))