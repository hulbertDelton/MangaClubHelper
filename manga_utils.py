import os
import discord
import re

SCOPE = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
TOKEN = "MTE3OTk1NTY1NTgxODM1ODk4NQ.G6tS0X.m6J7o6gCq2WZ6QzQJa1B1rOIhcGroxnsA5g0MM"
wave_emoji = ":wave:"
greet_strings = ["hi","hello","hey","whats up","what's up","greet","howdy","hail","well met","sup","whatup","whadup","whaddup","konichiwa","konnichiwa","こんにちは","kon ban wa","konbanwa","こんばんは", "ohaiyo","ohayo","ohaiyou","ohayou","おはよう","おはよ","osu","おす"]

def IsGreeting(message:str) -> bool:
    if len(message) < 1:
        return False
    
    msgparts = re.split(" |,|!", message)
    for m in msgparts:
        if m.lower() == "yo":
            return True
    
    for greeting in greet_strings:
        if message.lower().find(greeting) != -1:
            return True
        
def BotAtted(client:discord.Client, mentionList):
    botMention = False
    for at in mentionList:
        if at.name == client.user.name:
            botMention = True
            break
    return botMention
    