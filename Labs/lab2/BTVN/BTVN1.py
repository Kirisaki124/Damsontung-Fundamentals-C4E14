from youtube_dl import YoutubeDL



#                               Download 1 or mutiple youtube videos
# dl = YoutubeDL()
# dl.download(["https://www.youtube.com/watch?v=BF-oyMcJOnk"])
# dl.download(["https://www.youtube.com/watch?v=BF-oyMcJOnk","https://www.youtube.com/watch?v=6fFi5x_2IAg"])


#                               Download audio
# dl = YoutubeDL()
# options = {
#     "format": "bestaudio/audio"
# }
# dl = YoutubeDL(options)
# dl.download(["https://www.youtube.com/watch?v=1XBH2ENImTc"])


#                               Search and download video
# dl = YoutubeDL
# options = {
#     "default_search": "ytsearch",
#     "max_download": 1                                     ### may not work for every video cause it use the youtube's search tool and download the first one
# }
# dl = YoutubeDL(options)
# dl.download(["perfect"])


#                               Search and download bestaudio
dl = YoutubeDL()
options = {
    "default_search": "ytsearch",
    "max_download": 1,                                       ### may not work for every audio cause it use the youtube's search tool and download the first one
    "format": "bestaudio/audio"
}
dl = YoutubeDL(options)
dl.download(["con điên"])
