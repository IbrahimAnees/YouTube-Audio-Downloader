# YouTube-Audio-Downloader
Download multiple YouTube videos simultaneously as mp3 files, saved with custom output names.

# Pre-requisites required to be installed before using:
- python3
- yt-dlp
- ffmpeg and ffprobe

# To use:
1) Place download.py in a new folder
2) Create a new text file called urls.txt in the same folder
3) Populate the text file with YouTube URLs and titles (see below for more information)
4) Using command line, run 'py download.py' 

# How to populate text file:
Each line should contain the URL followed by the desired output name.
The URL and title should be separated by a whitespace character.

Example file urls.txt: <br />
https://youtube.com/watch?v=example1 First file <br />
https://youtube.com/watch?v=example2 File 2

Audio files will be downloaded as: <br />
First file.mp3 <br />
File 2.mp3
