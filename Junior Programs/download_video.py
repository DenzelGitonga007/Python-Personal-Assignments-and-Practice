# Trying to download YouTube video in audio format using Python
# First install pytube 3 from pip-- pip install pytube3
# Next, import YouTube module
from pytube import YouTube
# Video link:
video_link = input("Enter the link")
save_location = "C:/Users/giton/OneDrive/Desktop"
# To handle the connection errors:
try:
    video = YouTube(video_link)
    print("...Welcome to Denzel Audio-YouTube Downloader...")
    print("\nDownloading {}...\n...Please wait...\n...Almost there...".format(video.title))
    audio = video.streams.filter(only_audio=True, file_extension='mp3').first()
    audio.download(save_location)

    print("Download complete")

except:
    print("Connection Error")