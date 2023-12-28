import interactions
from interactions import slash_command, SlashContext
from decouple import config
import manga_utils, manga_picking

TOKEN = config('TOKEN')

secretary = interactions.Client(token = TOKEN)

#@secretary.event
#async def on_message(message):
#    if message.author == secretary.user:
#        return
    
#    #bot @ed
#    elif manga_utils.BotAtted(secretary, message.mentions):
#        msg = ""
#        if manga_utils.IsGreeting(message.content):
#            msg = "Oh, hello " + message.author.name + " " + manga_utils.wave_emoji + "\nHow can I help you?"
#        else:
#            msg = "sorry, I don't understand that yet."
#        await message.channel.send(msg)
#        return
    
#    await secretary.process_commands(message)
#    return

@slash_command(
                name = 'manga',
                description = "Choose a manga from the list in the google sheet",
                group_name = "pick",
                group_description = "commands for choosing the next manga we'll read",
                sub_cmd_name = "random",
                sub_cmd_description = "choose a random manga from the list"
            )
async def PickARandomManga(ctx: SlashContext):
    print("picking manga")
    msg = manga_picking.ParseSelectionType("random")
    current_manga = msg
    await ctx.send("Alright, I've set the club's new manga. Here's the details:")
    await ctx.send(str(msg))
    return

@PickARandomManga.subcommand(
        group_name = "pick",
        group_description = "commands for choosing the next manga we'll read",
        sub_cmd_name = "next",
        sub_cmd_description = "choose the second manga in the list"
)
async def PickNextManga(ctx: SlashContext):
    print("picking next manga")
    msg = manga_picking.ParseSelectionType("next")
    await ctx.send("Alright! The next manga in the list has been queued up. Here's the details:")
    await ctx.send(str(msg))
    return

@PickARandomManga.subcommand(
        group_name = "rate",
        group_description = "commands for opening up ratings for a manga",
        sub_cmd_name = "current",
        sub_cmd_description = "rate the manga listed as \"currently reading\""
)
async def RateCurrent(ctx: SlashContext):
    return

@slash_command(
                name = 'schedule',
                description = "club meeting schedule management",
                group_name = "meeting",
                group_description = "manage the club meetings here",
                sub_cmd_name = "next",
                sub_cmd_description = "Schedule the next club meeting"
            )
async def ScheduleMeeting(ctx: SlashContext, *, date, time):
    #await ctx.send("Okay, I've added the " + date + " meeting to the books.")
    return

@ScheduleMeeting.subcommand(
        group_name = "meeting",
        group_description = "manage the club meetings here",
        sub_cmd_name = "cancel",
        sub_cmd_description = "Cancel the next club meeting"
        )
async def CancelMeeting(ctx: SlashContext):
    await ctx.send("Got it. Next meeting has been cancelled.")
    return

@ScheduleMeeting.subcommand(
        group_name = "meeting",
        group_description = "manage the club meetings here",
        sub_cmd_name = 'recurring',
        sub_cmd_description = 'Set up recurring club meetings'
)
async def SetupRecurringMeeting(ctx: SlashContext, *, first_date, interval_num, interval_time, last_date):
    return

@slash_command(name = 'list_manga_entry')
async def ListEntry(ctx: SlashContext, listentry):
    entryint = int(listentry)
    secretary.current_manga = manga_picking.GetLiveMangaList()[entryint]
    await ctx.send("That would be " + secretary.current_manga['Manga Title'])
    return

@slash_command(name = "list_current_manga")
async def ListCurrentlyReading(ctx: SlashContext):
    await ctx.send("The club is currently reading this:")
    await ctx.send(secretary.current_manga)
    return

@slash_command(name = "help")
async def Help(ctx: SlashContext):
    helpstr = "Hello! I'm your Manga Club Assistant, Gokulisha. I can handle a bunch of manga-related tasks.\nHere's a list of my commands, that are all prefixed with '>'\n- Pick: You can ask me to $pick a random manga or $pick the next manga. In either case, I'll pull a list item from the spreadsheet and that will be the club's next selection!\n- ListMangaEntry: With this, you can ask me for a specific listing, or just say 'random' and I'll give you a manga back. I'll do my best to interpret what you're asking for, but try to be as exact as possible with the title.\n- ListCurrentManga: This will tell you what we're currently reading.\n\nOTHER FEATURES ARE COMING SOON"
    await ctx.send(helpstr)
    return

secretary.start()