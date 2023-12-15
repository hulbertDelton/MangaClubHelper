import manga_utils
import re, gspread, random, json
#import csv, requests, os
from decouple import config
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

creds = config('CREDENTIALS')
json_keyfile = json.loads(creds)

class MangaEntry:
    def __init__(self, listitem) -> None:
        self.index = 0
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
    creds = ServiceAccountCredentials.from_json_keyfile_dict(json_keyfile, manga_utils.SCOPE)
    cli = gspread.authorize(creds)
    return cli

def RefreshMangaList() -> list[MangaEntry]:
    cli = OAthRefresh()

    manga_sheet = cli.open("MangaSubmissions").get_worksheet(0)
    #archive_sheet = cli.open("MangaSubmissions").get_worksheet(1)

    allmanga = manga_sheet.get_all_records()
    listout : list[MangaEntry] = [MangaEntry(allmanga[0])]
    listout.clear()
    for manga in allmanga:
        new_entry = MangaEntry(manga)
        new_entry.index = allmanga.index(manga)
        listout.append(new_entry)
    return listout

    #allarchives = archive_sheet.get_all_records()
    #archive_list.Clear()
    #for arch in allarchives:
        #new_archive = MangaEntry(arch)
        #new_archive.index = allarchives.index(arch)
        #archive_list.Add(new_archive)


def PickRandomManga():
    manga_list = RefreshMangaList()

    rand_int = random.randrange(0,len(manga_list))
    selection = manga_list[rand_int]
    return selection

def PickNextManga() -> str:
    mangalist = RefreshMangaList()
    selection = mangalist[1]
    return selection

def ArchiveManga(item:MangaEntry):
    pass

def SetMangaToClubActive():
    pass

def ParseSelectionType(message:str):
    msg = message.lower().split()
    for m in msg:
        if m == "random":
            return PickRandomManga()
        elif m == "next":
            return PickNextManga()
    pass