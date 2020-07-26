#!/usr/bin/env python3

import os
import mpv
#import globals



class queue:

    def __init__(self, path):                                                                       #initializes the class and its variables
        self.dir = path
        self.confdir = r'config/'
        self.tempdir = self.confdir + r'temp/'
        self.playlist = 'playlist.txt'
        pass

    def getconf(self):
        return self.confdir, self.tempdir, self.playlist

    def listtracks(self):                                                                           #makes a list of all the audio files in the default directory and prints it
        print("""TRACKS:
                """)
        self.tracks = []
        x = 0
        for file in os.listdir(self.dir):
            if file.endswith(".mp3") or file.endswith(".wav"):                                      #checks the files' extension
                print(str(x+1) + ' ' + file)
                self.tracks = self.tracks + [file]
                x=x+1

    def seltracks(self):                                                                            #makes the user select the track from the list
        while True:
            try:
                self.num = int(input("Select the track: "))
                if self.num > 0 and self.num <= len(self.tracks):                                       #checks if the number of the track is in the list
                    self.song = self.tracks[self.num - 1]
                    break
                else:
                    print ("Select a number in the given list!")
            except ValueError:
                print("Select a number in the given list!")
    def play(self):                                                                                 #plays the song
        print(self.song)
        #self.source = mpv.MPV(ytdl=True, log_handler=print, loglevel='debug')                                                            #debug
        self.source = mpv.MPV(ytdl=True)                                                            #initializes the class of the track
        f = open(self.tempdir + self.playlist, 'r+') 

        linnum = int(len(open(self.tempdir + self.playlist).readlines(  )))
        for _ in range(linnum):
            self.source.playlist_append(f.readline(self.tempdir + self.playlist))
        f.close()
        self.source.play(self.dir + self.song)                                                      #actually plays the song
    
    def loop(self):
        while True:                                                                                 #sets the loop
            action = input("Input: ")
            if action == 'p' or action == 'P':                                                      #pauses the track
                if self.source.pause == False:
                    self.source.pause = True
                else:
                    self.source.pause = False
            
            elif action == 's' or action == 'S':                                                    #skips to the next track of the list
                self.source.playlist_next()

            else:
                break                                                                               #exits the loop

