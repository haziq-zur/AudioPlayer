import os
import pygame
from tkinter import *
from tkinter import filedialog

class AudioControl:
    def __init__(self):
        self.IsPaused = False

    def playtrack(self, audiotrack, audiostatus, playlist):
        # Displaying Selected Song title
        audiotrack.set(playlist.get(ACTIVE))
        # Displaying Status
        audiostatus.set("-Playing")
        # Loading Selected track
        pygame.mixer.music.load(playlist.get(ACTIVE))
        # Playing Selected track
        pygame.mixer.music.play()
    
    def stoptrack(self, audiostatus):
        # Displaying Status
        audiostatus.set("-Stopped")
        # Stopped track
        pygame.mixer.music.stop()

    def togglepausetrack(self, audiostatus):
        print ("before", self.IsPaused)
        if not self.IsPaused:
            # Displaying Status
            audiostatus.set("-Paused")
            # Paused track
            pygame.mixer.music.pause()
            # Set True to Paused variable
            self.IsPaused = True
        else:
            # Redisplayed audio status
            audiostatus.set("-Playing")
            # Unpause track
            pygame.mixer.music.unpause()
            # Set False to Paused variable
            self.IsPaused = False
        
        print ("after", self.IsPaused)

    def loadtrack(self, playlist):
        self.newplaylist = filedialog.askopenfilename()
        filedir = os.path.dirname(self.newplaylist)
        os.chdir(filedir)
        musictracks = os.listdir()
        for track in musictracks:
            IsMusicFile = (os.path.splitext(track)[1]) == ".mp3"
            if IsMusicFile:
                playlist.insert(END,track)
            else:
                break

        return playlist