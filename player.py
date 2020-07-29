#!/usr/bin/env python3

import os
import mpv

class queue:

    def __init__(self, path):
        """ Initializes the class and its variables """

        self.dir = path
        self.confdir = r'config/'
        self.tempdir = self.confdir + r'temp/'
        self.playlist = 'playlist.txt'

    def getconf(self): 
        """ Return value to create the playlist file """

        return self.confdir, self.tempdir, self.playlist

    def listtracks(self):
        """ 
        Makes a list of all the audio files 
        in the default directory and prints it 
        """

        print("TRACKS: \n")
        self.tracks = []
        x = 0
        for file in os.listdir(self.dir):
            if file.endswith(".mp3") or file.endswith(".wav"): # Checks the files' extension
                x += 1
                print(str(x) + ' ' + file)
                self.tracks = self.tracks + [file]
        
        with open(self.tempdir + self.playlist, 'a') as playlist:
            for i in range(len(self.tracks)):
                playlist.write(self.dir + self.tracks[i] + "\n")

    def seltracks(self):
        """ Makes the user select the track from the list """

        while True:
            try:
                self.num = int(input("Select the track: "))
                if self.num > 0 and self.num <= len(self.tracks): # Checks if the number of the track is in the list
                    self.song = self.tracks[self.num - 1]
                    break
                else:
                    print ("Select a number in the given list!")
            except ValueError:
                print("Select a number in the given list!")
    
    def play(self):
        """ Play the song """

        print(self.song)
        #self.source = mpv.MPV(ytdl=True, log_handler=print, loglevel='debug') # Debug
        self.source = mpv.MPV(ytdl=True, terminal=True, input_terminal=True) # Initializes the class of the track
        f = open(self.tempdir + self.playlist, 'r+') 

        linnum = int(len(open(self.tempdir + self.playlist).readlines(  ))) # Get the number of the audio files
        
        self.source.play(self.dir + self.song) # Actually plays the song
        
        for _ in range(linnum):
            self.source.playlist_append(f.readline()) # Add the song into playlist.txt
        f.close()
                                                                 
    def loop(self):
        """ Manage tracks and playlist """

        global status # Variable to check the while-loop 
        status = True

        while status: # Sets the loop
            
            @self.source.on_key_press('SPACE')
            def pause():
                """ Stop the song """

                if not self.source.pause:
                    self.source.pause = True
                else:
                    self.source.pause = False

            @self.source.on_key_press('n')            
            def skip_next():
                """ Skip to the next song """

                if self.num < len(self.tracks):
                    self.num += 1
                else:
                    self.num = 1

                self.source.stop()
                self.source.play(self.dir + self.tracks[self.num - 1])
            
            @self.source.on_key_press('p')            
            def skip_prev():
                """ Skip to the previous song """

                if self.num > 1:
                    self.num -= 1
                else:
                    self.num = len(self.tracks)

                self.source.stop()
                self.source.play(self.dir + self.tracks[self.num - 1])
            
            @self.source.on_key_press('q')
            def quit():
                """ Quit """

                global status
                self.source.quit()
                status = False

