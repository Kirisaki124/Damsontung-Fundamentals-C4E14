from urllib.request import urlopen
from bs4 import BeautifulSoup
import codecs
import pyexcel


raw_data = urlopen("https://www.nhaccuatui.com").read().decode("utf8")


file = codecs.open("nct.html", "w", "utf8")     # w: write  b: binary (raw)
file.write(raw_data)
file.close()
# print(raw_data)
soup = BeautifulSoup(raw_data, "html.parser")
ul = soup.find("div", "list_chart_music")
li_list = ul.find_all("li")

songs = []


    # print(li.prettify())
# a = li.div.h3.a         #i stoped her.e
# b = li.div.h4.a
# song = {
#     "title":a.string,
#     "artist": b.string
#     }
# songs.append(song)
# print(songs)
for li in li_list:
    a = li.div.h3
    b = li.div.h4

    artists = b.find_all("a")
    c = " "
    for artist in artists:
        c += artist.string

    song = {
    "title": a.string,
    "artist": c
    }
    songs.append(song)
pyexcel.save_as(records = songs, dest_file_name = "nct.xlsx" )
