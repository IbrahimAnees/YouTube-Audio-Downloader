import youtube_dl
import sys

inputUrl = sys.argv[1]
inputName = sys.argv[2]


def run():

    video_url = inputUrl
    video_info = youtube_dl.YoutubeDL().extract_info(
        url = video_url,download=False
    )
    filename = f"{inputName}.mp3"
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':filename,
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    print("Download complete... {}".format(filename))

if __name__=='__main__':
    run()