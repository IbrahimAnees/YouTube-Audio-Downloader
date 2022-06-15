import sys
import os
import yt_dlp

def run(inputUrl:str, inputName:str):

    URLS = [inputUrl]

    ydl_opts = {
        'format': 'mp3/bestaudio/best',
        'outtmpl': inputName + ".%(ext)s",
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }]
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        error_code = ydl.download(URLS)

if __name__=='__main__':

    if(os.path.isfile('./urls.txt')) :
        print("File exists!")
        filename = './urls.txt'
        with open(filename) as file:
         lines = file.readlines()
         lines = [line.rstrip() for line in lines]

        for line in lines:
            space = line.find(" ")
            url = line[0:space]
            title = line[space+1:]
            run(url, title)

