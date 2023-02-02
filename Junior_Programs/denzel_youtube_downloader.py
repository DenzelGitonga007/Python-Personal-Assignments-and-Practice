# Trying to download YouTube video in audio format using Python
# First install pytube 3 from pip-- pip install pytube3
# Next, import YouTube module
from pytube import YouTube
# Welcome message
print("\n...Welcome to Denzel YouTube Downloader 🤗🎬🎶...")
# Allow the program to run until the user exits
rerun = "y"
while rerun.lower() == "y":
    # Get the user input and handle any errors-- video link:
    video_link = input("Enter the link of the video: ")
    save_location = "C:/Users/giton/OneDrive/Desktop"
    # User to select download format
    download_format = input("Which format do you want to download in? \n[Type video for video and audio for audio]: ")
    # Download audio
    if download_format.lower() == "audio":
        # To handle the connection errors:
        try:
            download_audio = YouTube(video_link)
            print("\nDownloading {}...\n...Please wait...\n...Almost there...".format(download_audio.title))
            audio = download_audio.streams.filter(only_audio=True, file_extension='mp4').first()
            audio.download(save_location)

            print("Download complete, check in your file 😉.\nEnjoy listening to {}".format(download_audio.title))

        except:
            print("...Connection Error...")
    # Download video
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

    # Ask if the user wishes to continue
    rerun = input("Would you like to download another one? \n[Type y to continue or x to exit] ")
# If the user exits
print("You're welcome 😉... \nFollow me on: \nTikTok: https://tinyurl.com/Denzel-TikTok \nYouTube: https://tinyurl.com/Denzel-YouTube \nInstagram: https://tinyurl.com/Denzel-Instagram \nTwitter: https://tinyurl.com/Denzel-Twitter \nLinkedIn: https://tinyurl.com/Denzel-LinkedIn")