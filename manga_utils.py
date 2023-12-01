import os
import discord

greet_strings = ["hi","hello","hey","whats up","what's up","greet","howdy","hail","well met","sup","whatup","whadup","whaddup","yo","konichiwa","konnichiwa","こんにちは","kon ban wa","konbanwa","こんばんは", "ohaiyo","ohayo","ohaiyou","ohayou","おはよう","おはよ","osu","おす"]

def IsGreeting(message:str) -> bool:
    if len(message) < 1:
        return False
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
    