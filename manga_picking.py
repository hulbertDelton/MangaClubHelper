import manga_utils
import os, csv, json, re, gspread, requests, random
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

filepath = os.path.dirname(__file__) + "\\credentials.json"

class MangaEntry:
    def __init__(self, listitem) -> None:
        self.title = listitem['Manga Title']
        self.author = listitem['Author']
        self.available = listitem['Where its Available']
        self.genres = re.split(',|/',listitem['Genre'])
        self.length = listitem['Length']
        self.synopsis = listitem['Brief Synopsis']
    def __str__(self) -> str:
        strout = "TITLE: " + self.title + "\n"
        strout += "AUTHOR: " + self.author + "\n"
        strout += "AVAILABLE: " + self.available + "\n"
        gen = ""
        for genre in self.genres:
            gen += genre + ", "
        strout += "GENRE(S): " + gen[:-2] + "\n"
        strout += "LENGTH: " + self.length + "\n"
        strout += "Synopsis: " + self.synopsis + "\n"
        return strout

def OAthRefresh():
    creds = ServiceAccountCredentials.from_json_keyfile_name(filepath, manga_utils.SCOPE)
    cli = gspread.authorize(creds)
    return cli

def GetLiveMangaList():
    cli = OAthRefresh()
    manga_sheet = cli.open("MangaSubmissions").get_worksheet(0)
    archive_sheet = cli.open("MangaSubmissions").get_worksheet(1)
    mangalist = manga_sheet.get_all_records()
    return mangalist


def PickRandomManga():
    mangalist = GetLiveMangaList()
    rand_int = random.randrange(0,len(mangalist))
    selection = mangalist[rand_int]
    return selection

def PickNextManga() -> str:
    mangalist = GetLiveMangaList()
    selection = mangalist[2]
    return selection

def ArchiveManga():
    pass

def SetMangaToClubActive():
    pass

def ParseSelectionType(message:str):
    msg = message.lower().split()
    for m in msg:
        if m == "random":
            return MangaEntry(PickRandomManga())
        elif m == "next":
            return MangaEntry(PickNextManga())
    pass