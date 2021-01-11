import os
import pygame
from tkinter import *
from tkinter import filedialog

class AudioPlayer:
    def __init__(self, root):
        self.root = root
        # Set window title and size
        self.root.title('D3vil Audio Player')
        self.root.geometry('490x120+200+200')

        # Initiate Pygame and Pygame Mixer to be used for audio playing
        pygame.init()
        pygame.mixer.init()

        # Initialize variable
        self.audiotrack = StringVar()
        self.audiostatus = StringVar()
        self.IsPaused = False

        # Creating the Track Frames for Song label & status label
        trackframe = LabelFrame(self.root,text="Now Playing...",font=("arial",10,"bold"),bg="dark slate gray",fg="white",bd=5,relief=GROOVE)
        trackframe.place(x=0,y=0,width=285,height=60)
        # Inserting Song Track Label
        songtrack = Label(trackframe,textvariable=self.audiotrack,width=20,font=("arial",10,"bold"),bg="dark sea green",fg="black").grid(row=0,column=0,padx=10,pady=5)
        # Inserting Status Label
        trackstatus = Label(trackframe,textvariable=self.audiostatus,font=("arial",10,"bold"),bg="dark sea green",fg="black").grid(row=0,column=1,padx=10,pady=5)

        # Creating Button Frame
        buttonframe = LabelFrame(self.root,text="Player Control",font=("arial",10,"bold"),bg="dark slate gray",fg="white",bd=5,relief=GROOVE)
        buttonframe.place(x=0,y=60,width=285,height=60)
        # Inserting Play Button
        playbutton = Button(buttonframe,text="Play",command=self.playtrack,width=5,font=("arial",10,"bold"),fg="black",bg="dark sea green").grid(row=0,column=0,padx=10,pady=5)
        # Inserting Pause Button
        pausebutton = Button(buttonframe,text="Pause",command=self.togglepausetrack,width=5,font=("arial",10,"bold"),fg="black",bg="dark sea green").grid(row=0,column=1,padx=10,pady=5)
        # Inserting Stop Button
        stopbutton = Button(buttonframe,text="Stop",command=self.stoptrack,width=5,font=("arial",10,"bold"),fg="black",bg="dark sea green").grid(row=0,column=2,padx=10,pady=5)
        # Inserting Load Button
        loadbutton = Button(buttonframe,text="Load",command=self.loadtrack,width=5,font=("arial",10,"bold"),fg="black",bg="dark sea green").grid(row=0,column=3,padx=10,pady=5)

        # Creating Playlist Frame
        listframe = LabelFrame(self.root,text="Playlist",font=("arial",10,"bold"),bg="dark slate gray",fg="white",bd=5,relief=GROOVE)
        listframe.place(x=285,y=0,width=205,height=120)
        # Inserting scrollbar
        scrol_y = Scrollbar(listframe,orient=VERTICAL)
        # Inserting Playlist listbox
        self.playlist = Listbox(listframe,yscrollcommand=scrol_y.set,selectbackground="dark slate gray",selectmode=SINGLE,font=("arial",10,"bold"),bg="dark sea green",fg="black",bd=5,relief=GROOVE)
        # Applying Scrollbar to listbox
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.playlist.yview)
        self.playlist.pack(fill=BOTH)

    def playtrack(self):
        # Displaying Selected Song title
        self.audiotrack.set(self.playlist.get(ACTIVE))
        # Displaying Status
        self.audiostatus.set("-Playing")
        # Loading Selected track
        pygame.mixer.music.load(self.playlist.get(ACTIVE))
        # Playing Selected track
        pygame.mixer.music.play()
    
    def stoptrack(self):
        # Displaying Status
        self.audiostatus.set("-Stopped")
        # Stopped track
        pygame.mixer.music.stop()

    def togglepausetrack(self):
        if not self.IsPaused:
            # Displaying Status
            self.audiostatus.set("-Paused")
            # Paused track
            pygame.mixer.music.pause()
            # Set True to Paused variable
            self.IsPaused = True
        else:
            # Redisplayed audio status
            self.audiostatus.set("-Playing")
            # Unpause track
            pygame.mixer.music.unpause()
            # Set False to Paused variable
            self.IsPaused = False

    def loadtrack(self):
        self.newplaylist = filedialog.askopenfilename()
        filedir = os.path.dirname(self.newplaylist)
        os.chdir(filedir)
        musictracks = os.listdir()
        for track in musictracks:
            IsMusicFile = (os.path.splitext(track)[1]) == ".mp3"
            if IsMusicFile:
                self.playlist.insert(END,track)
            else:
                break

if __name__ == "__main__":
    root = Tk()
    app = AudioPlayer(root)
    mainloop()