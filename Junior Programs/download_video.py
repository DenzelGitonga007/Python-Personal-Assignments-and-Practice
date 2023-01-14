# Trying to download YouTube video in audio format using Python
# First install pytube 3 from pip-- pip install pytube3
# Next, import YouTube module
from pytube import YouTube
# Welcome message
print("...Welcome to Denzel Audio-YouTube Downloader 🤗🎬🎶...")
# Get the user input and handle any errors-- video link:
video_link = input("Enter the link of the video: ")
save_location = "C:/Users/giton/OneDrive/Desktop"
# User to select download format
download_format = input("Which format do you want to download in? \n[Type video for video and audio for audio]: ")
if download_format.lower() == "audio":
    # To handle the connection errors:
    try:
        download_audio = YouTube(video_link)
        print("\nDownloading {}...\n...Please wait...\n...Almost there...".format(download_audio.title))
        audio = download_audio.streams.filter(only_audio=True, file_extension='mp3').first()
        audio.download(save_location)

        print("Download complete, check in your file 😉.\nEnjoy listening to {}".format(download_audio.title))

    except:
        print("...Connection Error...")
elif download_format.lower() == "video":
    try:
        download_video = YouTube(video_link)
        print("\nDownloading {}...\n...Please wait...\n...Almost there...".format(download_video.title))
        video = download_video.streams.filter(only_audio=False, only_video=False, file_extension='mp4').first()
        video.download(save_location)

        print("Download complete, check in your file 😉.\nEnjoy watching {}".format(download_video.title))
    except:
        print("...Connection Error...")
else:
    print("Something's not right...")