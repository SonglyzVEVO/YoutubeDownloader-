from os import path as ospath
from pytube import YouTube
import tkinter.messagebox as tk1

def getVideo(URL):
    """Get Highest Quality Video from YT URL."""
    YT = YouTube(URL)
    try:
        print(f"Downloading Video: {YT.title}")
        YTVIDEO_FILE_PATH = YT.streams.filter(only_audio=False, progressive=True, 
        file_extension='mp4').order_by('resolution').desc().first().download('Downloads/')
    except Exception as e:
        print(f"Error: {e}")

def getAudio(URL):
    """Get Highest Quality Audio from YT URL."""
    YT = YouTube(URL)
    try:
        print(f"Downloading Audio[]: {YT.title}")
        YTAUDIO_FILE_PATH = YT.streams.filter(only_audio=True, 
        file_extension='mp4').order_by('abr').desc().first().download('Downloads/')
    except Exception as e: 
        print(f"Error: {e}")

# getAudio("https://www.youtube.com/watch?v=EAqE5XGMsyY&list=RDEMJOA4GmWeK1YNLi2jgDH4Wg&index=26")