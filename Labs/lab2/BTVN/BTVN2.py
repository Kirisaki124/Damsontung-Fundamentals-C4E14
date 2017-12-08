from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from youtube_dl import YoutubeDL

# raw_data = urlopen("https://www.apple.com/itunes/charts/songs/").read().decode("utf8")
#
# file = codecs.open("itune.html", "wb", "utf8")
# file.write(raw_data)
# file.close()

webpage = urlopen("https://www.apple.com/itunes/charts/songs/")
data = webpage.read()
html_content = data.decode("utf8")
soup = BeautifulSoup(html_content, "html.parser")
ul = soup.find("section", "section chart-grid")
li_list = ul.find_all("li")
n = 0
songs = []
for li in li_list:
    a = li.h3.a
    b = li.h4.a
    song = {
        "title": a.string,
        "artist": b.string
    }

    songs.append(song)

for i in range(len(songs)):
    dl = YoutubeDL()
    options = {
        "default_search": "ytsearch",
        "max_download": 1,
        "format": "bestaudio/audio"
    }
    dl = YoutubeDL(options)
    dl.download([songs[i]["title"]])
    # print(songs[n]["title"])
    # n += 1
    # print(songs[n]["title"])

pyexcel.save_as(records = songs, dest_file_name = "itunes.xlsx")
