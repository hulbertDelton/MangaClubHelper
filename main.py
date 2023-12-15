import asyncio
import discord
from discord.ext import commands
from discord.ext.commands import cooldown, BucketType
from discord.ext.commands.help import HelpCommand
from decouple import config
import manga_utils, manga_picking

TOKEN = config('TOKEN')

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
            msg = "Oh, hello " + message.author.name + " " + manga_utils.wave_emoji + "\nHow can I help you?"
        else:
            msg = "sorry, I don't understand that yet."
        await message.channel.send(msg)

    await secretary.process_commands(message)

@secretary.command(name = 'pick')
async def PickARandomManga(ctx, *, arg):
    print("picking manga")
    msg = manga_picking.ParseSelectionType(arg)
    current_manga = msg
    #await ctx.send("Okay! Give me just a minute here, I'm finishing up a Candy Crush Saga level.")
    await ctx.send("Alright, I've set the club's new manga. Here's the details:")
    await ctx.send(msg)

@secretary.command(name = 'schedule')
async def ScheduleMeeting(ctx, date, time):
    #await ctx.send("Okay, I've added the " + date + " meeting to the books.")
    pass

@secretary.command(name='cancel')
async def CancelMeeting(ctx):
    await ctx.send("Got it. Next meeting has been cancelled.")

    pass

@secretary.command(name='ListMangaEntry')
async def ListEntry(ctx, listentry):
    entryint = int(listentry)
    secretary.current_manga = manga_picking.GetLiveMangaList()[entryint]
    await ctx.send("That would be " + secretary.current_manga['Manga Title'])

@secretary.command()
async def ListCurrentlyReading(ctx):
    await ctx.send("The club is currently reading this:")
    await ctx.send(secretary.current_manga)

@secretary.command()
async def Help(ctx):
    helpstr = "Hello! I'm your Manga Club Assistant, Gokulisha. I can handle a bunch of manga-related tasks.\nHere's a list of my commands, that are all prefixed with '>'\n- Pick: You can ask me to $pick a random manga or $pick the next manga. In either case, I'll pull a list item from the spreadsheet and that will be the club's next selection!\n- ListMangaEntry: With this, you can ask me for a specific listing, or just say 'random' and I'll give you a manga back. I'll do my best to interpret what you're asking for, but try to be as exact as possible with the title.\n- ListCurrentManga: This will tell you what we're currently reading.\n\nOTHER FEATURES ARE COMING SOON"
    await ctx.send(helpstr)

asyncio.run(secretary.run(TOKEN))