import requests
import re
from bs4 import BeautifulSoup
import discord

TRACKS = { "Crash Cove": ["crashcove", "cc", "cove"],
           "Roo's Tubes": ["roo'stubes", "roostubes", "rt", "tubes"],
           "Mystery Caves": ["mysterycaves", "mystery", "caves", "mc"],
           "Sewer Speedway": ["sewerspeedway", "sewer", "speedway", "sewers", "ss"],
           "Coco Park": ["cocopark", "coco", "park", "cp"],
           "Tiger Temple": ["tigertemple", "tt", "temple"],
           "Dingo Canyon": ["dingocanyon", "dingo", "canyon", "dc"],
           "Papu's Pyramid": ["papuspyramid", "papu", "pyramid", "papu's", "pp"],
           "Blizzard Bluff": ["blizzardbluff", "blizzard", "bluff", "bb"],
           "Dragon Mines": ["dragonmines", "dragon", "mines", "dm"],
           "Polar Pass": ["polarpass", "polar", "pass", "pp"],
           "Tiny Arena": ["tinyarena", "tiny", "arena", "ta"],
           "Cortex Castle": ["cortexcastle", "cortex", "castle", "cc"],
           "N. Gin Labs": ["n.ginlabs", "nginlabs", "n.gin", "ngin", "labs", "nl"],
           "Hot Air Skyway": ["hotairskyway", "hotair", "hot", "air", "skyway", "has"],
           "Oxide Station": ["oxidestation", "oxide", "station", "os"],
           "Turbo Track": ["turbotrack", "turbo", "track", "tt"],
           "Retro Stadium": ["retrostadium", "retrotrack" "retro", "stadium", "rs", "rt"],
           "Slide Coliseum": ["slidecoliseum", "slide", "coliseum", "sc"],
           "Inferno Island": ["infernoisland", "inferno", "island", "ii"],
           "Jungle Boogie": ["jungleboogie", "jungle", "boogie", "jb"],
           "Tiny Temple": ["tinytemple", "tiny", "temple", "tt"],
           "Meteor Gorge": ["meteorgorge", "meteor", "gorge", "mg"],
           "Barin Ruins": ["barinruins", "barin", "ruins", "br"],
           "Deep Sea Driving": ["deepseadriving", "deepsea", "driving", "deep", "dsd"],
           "Out of Time": ["outoftime", "time", "oot"],
           "Clockwork Wumpa": ["clockworkwumpa", "clockwork", "wumpa", "cw"],
           "Thunder Struck": ["thunderstruck", "thunder", "struck", "ts"],
           "Assembly Lane": ["assemblylane", "assembly", "lane", "al"],
           "Android Alley": ["androidalley", "android", "alley", "aa"],
           "Electron Avenue": ["electronavenue", "electron", "avenue", "ea"],
           "Hyper Spaceway": ["hyperspeedway", "hyperspaceway", "hyper", "speedway", "spaceway", "hs"],
           "Twilight Tour": ["twilighttour", "twilight", "tour", "tt"],
           "Prehistoric Playground": ["prehistoricplayground", "prehistoric", "playground", "pp"],
           "Spyro Circuit": ["spyrocircuit", "spyro", "circuit", "sc"],
           "Nina's Nightmare": ["nina'snightmare", "ninasnightmare", "nina's", "ninas", "nina", "nightmare", "nn"],
           "Koala Carnival": ["koalacarnival", "koala", "carnival", "kc"] }

ENGINES = { "Speed": ["spd", "speed"],
            "Accel": ["accel", "acceleration", "acc"],
            "Turn": ["turn", "trn"],
            "Drift": ["drift", "dft"],
            "Balanced": ["balanced", "bal"] }

class Track:

    name = ""
    link = ""

    def __init__ (self, name):

        self.all_rows = []
        self.all_links = []
        self.all_images = []

        self.users = []
        self.user_links = []
        self.times = []
        self.time_links = []
        self.dates = []
        self.ranks = []
        self.engine = []
        self.flags = []
        self.chars = []

        self.find_track(name)

    def find_track(self, name):
        track = name.lower()

        if track in TRACKS['Crash Cove']:
            self.name = 'Crash Cove'
            self.link = "https://crashteamranking.com/nftttable/?track_choice=1&course_lap=0&kart_style=0&country_choice=0&version_used=0&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob"
        elif track in TRACKS["Roo's Tubes"]:
            self.name = "Roo's Tubes"
            self.link = "https://crashteamranking.com/nftttable/?track_choice=3&course_lap=0&kart_style=0&country_choice=0&version_used=0&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob"
        elif track in TRACKS["Tiger Temple"]:
            self.name = "Tiger Temple"
            self.link = "https://crashteamranking.com/nftttable/?track_choice=5&course_lap=0&kart_style=0&country_choice=0&version_used=0&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob"
        elif track in TRACKS["Coco Park"]:
            self.name = "Coco Park"
            self.link = "https://crashteamranking.com/nftttable/?track_choice=7&course_lap=0&kart_style=0&country_choice=0&version_used=0&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob"
        elif track in TRACKS["Mystery Caves"]:
            self.name = "Mystery Caves"
            self.link = "https://crashteamranking.com/nftttable/?track_choice=9&course_lap=0&kart_style=0&country_choice=0&version_used=0&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob"
        elif track in TRACKS["Blizzard Bluff"]:
            self.name = "Blizzard Bluff"
            self.link = "https://crashteamranking.com/nftttable/?track_choice=11&course_lap=0&kart_style=0&country_choice=0&version_used=0&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob"
        elif track in TRACKS["Sewer Speedway"]:
            self.name = "Sewer Speedway"
            self.link = "https://crashteamranking.com/nftttable/?track_choice=13&course_lap=0&kart_style=0&country_choice=0&version_used=0&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob"
        elif track in TRACKS["Dingo Canyon"]:
            self.name = "Dingo Canyon"
            self.link = "https://crashteamranking.com/nftttable/?track_choice=15&course_lap=0&kart_style=0&country_choice=0&version_used=0&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob"
        elif track in TRACKS["Papu's Pyramid"]:
            self.name = "Papu's Pyramid"
            self.link = "https://crashteamranking.com/nftttable/?track_choice=17&course_lap=0&kart_style=0&country_choice=0&version_used=0&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob"
        elif track in TRACKS["Dragon Mines"]:
            self.name = "Dragon Mines"
            self.link = "https://crashteamranking.com/nftttable/?track_choice=19&course_lap=0&kart_style=0&country_choice=0&version_used=0&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob"
        elif track in TRACKS["Polar Pass"]:
            self.name = "Polar Pass"
            self.link = "https://crashteamranking.com/nftttable/?track_choice=21&course_lap=0&kart_style=0&country_choice=0&version_used=0&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob"
        elif track in TRACKS["Cortex Castle"]:
            self.name = "Cortex Castle"
            self.link = "https://crashteamranking.com/nftttable/?track_choice=23&course_lap=0&kart_style=0&country_choice=0&version_used=0&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob"
        elif track in TRACKS["Tiny Arena"]:
            self.name = "Tiny Arena"
            self.link = "https://crashteamranking.com/nftttable/?track_choice=25&course_lap=0&kart_style=0&country_choice=0&version_used=0&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob"
        elif track in TRACKS["Hot Air Skyway"]:
            self.name = "Hot Air Skyway"
            self.link = "https://crashteamranking.com/nftttable/?track_choice=27&course_lap=0&kart_style=0&country_choice=0&version_used=0&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob"
        elif track in TRACKS["N. Gin Labs"]:
            self.name = "N. Gin Labs"
            self.link = "https://crashteamranking.com/nftttable/?track_choice=29&course_lap=0&kart_style=0&country_choice=0&version_used=0&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob"
        elif track in TRACKS["Oxide Station"]:
            self.name = "Oxide Station"
            self.link = "https://crashteamranking.com/nftttable/?track_choice=31&course_lap=0&kart_style=0&country_choice=0&version_used=0&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob"
        elif track in TRACKS["Slide Coliseum"]:
            self.name = "Slide Coliseum"
            self.link = "https://crashteamranking.com/nftttable/?track_choice=33&course_lap=0&kart_style=0&country_choice=0&version_used=0&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob"
        elif track in TRACKS["Turbo Track"]:
            self.name = "Turbo Track"
            self.link = "https://crashteamranking.com/nftttable/?track_choice=35&course_lap=0&kart_style=0&country_choice=0&version_used=0&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob"
        elif track in TRACKS["Inferno Island"]:
            self.name = "Inferno Island"
            self.link = "https://crashteamranking.com/nftttable/?track_choice=37&course_lap=0&kart_style=0&country_choice=0&version_used=0&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob"
        elif track in TRACKS["Jungle Boogie"]:
            self.name = "Jungle Boogie"
            self.link = "https://crashteamranking.com/nftttable/?track_choice=39&course_lap=0&kart_style=0&country_choice=0&version_used=0&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob"
        elif track in TRACKS["Tiny Temple"]:
            self.name = "Tiny Temple"
            self.link = "https://crashteamranking.com/nftttable/?track_choice=41&course_lap=0&kart_style=0&country_choice=0&version_used=0&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob"
        elif track in TRACKS["Meteor Gorge"]:
            self.name = "Meteor Gorge"
            self.link = "https://crashteamranking.com/nftttable/?track_choice=43&course_lap=0&kart_style=0&country_choice=0&version_used=0&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob"
        elif track in TRACKS["Barin Ruins"]:
            self.name = "Barin Ruins"
            self.link = "https://crashteamranking.com/nftttable/?track_choice=45&course_lap=0&kart_style=0&country_choice=0&version_used=0&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob"
        elif track in TRACKS["Deep Sea Driving"]:
            self.name = "Deep Sea Driving"
            self.link = "https://crashteamranking.com/nftttable/?track_choice=47&course_lap=0&kart_style=0&country_choice=0&version_used=0&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob"
        elif track in TRACKS["Out of Time"]:
            self.name = "Out of Time"
            self.link = "https://crashteamranking.com/nftttable/?track_choice=49&course_lap=0&kart_style=0&country_choice=0&version_used=0&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob"
        elif track in TRACKS["Clockwork Wumpa"]:
            self.name = "Clockwork Wumpa"
            self.link = "https://crashteamranking.com/nftttable/?track_choice=51&course_lap=0&kart_style=0&country_choice=0&version_used=0&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob"
        elif track in TRACKS["Thunder Struck"]:
            self.name = "Thunder Struck"
            self.link = "https://crashteamranking.com/nftttable/?track_choice=53&course_lap=0&kart_style=0&country_choice=0&version_used=0&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob"
        elif track in TRACKS["Assembly Lane"]:
            self.name = "Assembly Lane"
            self.link = "https://crashteamranking.com/nftttable/?track_choice=55&course_lap=0&kart_style=0&country_choice=0&version_used=0&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob"
        elif track in TRACKS["Android Alley"]:
            self.name = "Android Alley"
            self.link = "https://crashteamranking.com/nftttable/?track_choice=57&course_lap=0&kart_style=0&country_choice=0&version_used=0&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob"
        elif track in TRACKS["Electron Avenue"]:
            self.name = "Electron Avenue"
            self.link = "https://crashteamranking.com/nftttable/?track_choice=59&course_lap=0&kart_style=0&country_choice=0&version_used=0&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob"
        elif track in TRACKS["Hyper Spaceway"]:
            self.name = "Hyper Spaceway"
            self.link = "https://crashteamranking.com/nftttable/?track_choice=61&course_lap=0&kart_style=0&country_choice=0&version_used=0&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob"
        elif track in TRACKS["Retro Stadium"]:
            self.name = "Retro Stadium"
            self.link = "https://crashteamranking.com/nftttable/?track_choice=63&course_lap=0&kart_style=0&country_choice=0&version_used=0&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob"
        elif track in TRACKS["Twilight Tour"]:
            self.name = "Twilight Tour"
            self.link = "https://crashteamranking.com/nftttable/?track_choice=65&course_lap=0&kart_style=0&country_choice=0&version_used=0&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob"
        elif track in TRACKS["Prehistoric Playground"]:
            self.name = "Prehistoric Playground"
            self.link = "https://crashteamranking.com/nftttable/?track_choice=67&course_lap=0&kart_style=0&country_choice=0&version_used=0&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob"
        elif track in TRACKS["Spyro Circuit"]:
            self.name = "Spyro Circuit"
            self.link = "https://crashteamranking.com/nftttable/?track_choice=69&course_lap=0&kart_style=0&country_choice=0&version_used=0&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob"
        elif track in TRACKS["Nina's Nightmare"]:
            self.name = "Nina's Nightmare"
            self.link = "https://crashteamranking.com/nftttable/?track_choice=71&course_lap=0&kart_style=0&country_choice=0&version_used=0&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob"
        elif track in TRACKS["Koala Carnival"]:
            self.name = "Koala Carnival"
            self.link = "https://crashteamranking.com/nftttable/?track_choice=73&course_lap=0&kart_style=0&country_choice=0&version_used=0&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob&ymUZloJA=qiPWmNfE&yvjg-lJGszZbFi=paClgyBGEMusTq&FkEGXuc=8TCnQob"


    def parse_link(self):
        resp = requests.get(self.link)
        soup = BeautifulSoup(resp.text, 'html.parser')
        table = soup.find('table', {'class': 'nfTimesTable'})
        table_rows = table.find_all('tr')

        for row in table_rows:
            td = row.find_all('td')
            a = row.find_all('a', attrs={'href': re.compile("^https://")})
            this_row = [str(i.text) for i in td]
            self.all_rows += [this_row]
            imgs = row.find_all('img', attrs={'src': re.compile("^https://crashteamranking.com/media/img/")})
            images = [image.get('src') for image in imgs]
            self.all_images += [images]
            links = [str(i.get('href')) for i in a]
            self.all_links += [links]

        for row in self.all_rows:
            try:
                self.ranks += [row[0]]
                self.users += [row[1]]
                self.times += [row[3]]
                self.engine += [row[6]]
                self.dates += [row[8]]
            except:
                pass
        for link in self.all_links:
            try:
                self.user_links += [link[0]]
                self.time_links += [link[1]]
            except:
                pass
        for image in self.all_images:
            try:
                self.flags += [image[0]]
                self.chars += [image[1]]
            except:
                pass

    def wr(self, kart_style=0):
        self.link = self.link.replace("kart_style=0", "kart_style=" + str(kart_style))
        self.parse_link()
        embed = discord.Embed(title=self.name, url=self.link)
        try:
            embed.add_field(name=self.users[0], value='[' + self.times[0] + '](' + self.time_links[0] + ') ' + self.engine[0], inline=True)
            embed.set_footer(text=self.dates[0])
            embed.set_thumbnail(url=self.chars[0])
            embed.set_image(url=self.flags[0])
        except:
            pass # no times
        return embed

    def top10(self, kart_style=0):
        self.link = self.link.replace("kart_style=0", "kart_style=" + str(kart_style))
        self.parse_link()
        embed = discord.Embed(title = self.name, url=self.link)
        if len(self.users) >= 10:
            for i in range(10):
                embed.add_field(name=self.ranks[i] + ' ' + self.users[i], value='[' + self.times[i] + '](' + self.time_links[i] + ') ' + self.engine[i], inline=False)
        else:
            for i in range(len(self.users)):
                embed.add_field(name=self.ranks[i] + ' ' + self.users[i], value='[' + self.times[i] + '](' + self.time_links[i] + ') ' + self.engine[i], inline=False)

        embed.set_thumbnail(url="https://i.imgur.com/tUd2uVa.png")
        return embed

    def ourtimes(self, ctx):
        embed = discord.Embed(title=self.name, url=self.link)
        with open('./' + ctx.guild.name + '/' + self.name + '.txt', 'r') as f:
            lines = f.readlines()

        lines = sorted(lines)

        for rank, line in enumerate(lines):
            line = line.split()
            time = line[0]
            name = line[1]
            link = ''
            if len(line) == 3:
                if line[2].upper() in ('TURN', 'ACCEL', 'SPD', 'DRIFT'):
                    name += ' ' + line[2].upper()
                else:
                    name += ' ' + 'SPD'
                    link = line[2]
            elif len(line) == 4:
                if line[3].upper() in ('TURN', 'ACCEL', 'SPD', 'DRIFT'):
                    name += ' ' + line[3].upper()

            if link != '':
                embed.add_field(name=str(rank+1) + ' ' + name, value='['+time+']('+link+')')
            else:
                embed.add_field(name=str(rank+1) + ' ' + name, value=time)

        return embed
