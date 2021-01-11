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

        self.audiotrack = StringVar()
        self.audiostatus = StringVar()

        # Creating the Track Frames for Song label & status label
        trackframe = LabelFrame(self.root,text="Now Playing...",font=("arial",10,"bold"),bg="Navyblue",fg="white",bd=5,relief=GROOVE)
        trackframe.place(x=0,y=0,width=285,height=60)
        # Inserting Song Track Label
        songtrack = Label(trackframe,textvariable=self.audiotrack,width=20,font=("arial",10,"bold"),bg="Orange",fg="gold").grid(row=0,column=0,padx=10,pady=5)
        # Inserting Status Label
        trackstatus = Label(trackframe,textvariable=self.audiostatus,font=("arial",10,"bold"),bg="orange",fg="gold").grid(row=0,column=1,padx=10,pady=5)

        # Creating Button Frame
        buttonframe = LabelFrame(self.root,text="Player Control",font=("arial",10,"bold"),bg="grey",fg="white",bd=5,relief=GROOVE)
        buttonframe.place(x=0,y=60,width=285,height=60)
        # Inserting Play Button
        playbutton = Button(buttonframe,text="Play",width=5,font=("arial",10,"bold"),fg="navyblue",bg="pink").grid(row=0,column=0,padx=10,pady=5)
        # Inserting Pause Button
        pausebutton = Button(buttonframe,text="Pause",width=5,font=("arial",10,"bold"),fg="navyblue",bg="pink").grid(row=0,column=1,padx=10,pady=5)
        # Inserting Stop Button
        stopbutton = Button(buttonframe,text="Stop",width=5,font=("arial",10,"bold"),fg="navyblue",bg="pink").grid(row=0,column=2,padx=10,pady=5)
        # Inserting Load Button
        loadbutton = Button(buttonframe,text="Load",width=5,font=("arial",10,"bold"),fg="navyblue",bg="pink").grid(row=0,column=3,padx=10,pady=5)

        # Creating Playlist Frame
        songsframe = LabelFrame(self.root,text="Playlist",font=("arial",10,"bold"),bg="grey",fg="white",bd=5,relief=GROOVE)
        songsframe.place(x=285,y=0,width=205,height=120)
        # Inserting scrollbar
        scrol_y = Scrollbar(songsframe,orient=VERTICAL)
        # Inserting Playlist listbox
        self.playlist = Listbox(songsframe,yscrollcommand=scrol_y.set,selectbackground="gold",selectmode=SINGLE,font=("arial",10,"bold"),bg="silver",fg="navyblue",bd=5,relief=GROOVE)
        # Applying Scrollbar to listbox
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.playlist.yview)
        self.playlist.pack(fill=BOTH)
        # Changing Directory for fetching Songs
        os.chdir("C:\\Music")
        # Fetching Songs
        songtracks = os.listdir()
        # Inserting Songs into Playlist
        for track in songtracks:
            self.playlist.insert(END,track)

root = Tk()
self = StringVar()
app = AudioPlayer.__init__(self, root)
mainloop()