# Playing music and mixing it
# import mixer
from pygame import mixer
# Start the mixer
mixer.init()
# Load the music
mixer.music.load("C:\\Users\\Denzel\\Music\\Tunaleta Sifa by Essence of Worship.mp3")
# Set volume
# mixer.music.set_volume(0.7)
# Start playing
mixer.music.play()
# Give instructions
print("...Welcome to Denzel music player...")
print("Press p to pause, r to resume, and e to exit the music player")
# Set the loop for playing
while True:
    instructions = input(" ")
    if instructions == 'p':
        #pause
        mixer.music.pause()
        print("You have paused the music, press r to resume playing...")
    elif instructions == 'r':
        #resume playing
        mixer.music.unpause()
        print("The music has resumed playing")
    elif instructions == 'e':
        #stop music
        mixer.music.stop()
        print("You have exited the music player")
        break