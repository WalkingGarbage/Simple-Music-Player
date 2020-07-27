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
                x += 1
                print(str(x) + ' ' + file)
                self.tracks = self.tracks + [file]
        
        with open(self.tempdir + self.playlist, 'a') as playlist:
            for i in range(len(self.tracks)):
                playlist.write(self.tracks[i] + "\n")

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
        self.source = mpv.MPV(ytdl=True, terminal=True, input_terminal=True)                        #initializes the class of the track
        f = open(self.tempdir + self.playlist, 'r+') 

        linnum = int(len(open(self.tempdir + self.playlist).readlines(  )))
        
        self.source.loop_playlist = 'inf' 
        self.source.play(self.dir + self.song) #actually plays the song
        
        for _ in range(linnum):
            self.source.playlist_append(f.readline())
        f.close()
                                                                 
    def loop(self):
        global status 
        status = True

        while status:                                                                                 #sets the loop
            """
            @self.source.property_observer("time-pos")
            def time(_name, value):
                try:
                    print("\rNow playing at {:.2f}s".format(value), end = "", flush = True)
                except:
                    pass
            """

            @self.source.on_key_press('p')
            def pause():
                if self.source.pause == False:
                    self.source.pause = True
                else:
                    self.source.pause = False

            @self.source.on_key_press('s')            
            def skip():
                pass

            @self.source.on_key_press('q')
            def quit():
                global status
                self.source.quit()
                status = False

            """
            action = input("Input: ")
            if action.lower() == 'p':                                                      #pauses the track
                if self.source.pause == False:
                    self.source.pause = True
                else:
                    self.source.pause = False
            
            elif action.lower() == 's':                                                    #skips to the next track of the list
                self.num += 1
                #print(self.num)
                print(self.source.playlist)
                print(self.source.playlist[self.num]['filename'])
                self.source.command('stop', 'keep-playlist')
                self.source.play(self.source.playlist[self.num]['filename'])
            
            elif action.lower() == 't':                                                     #get time
                @self.source.property_observer("time-pos")
                def time(_name, value):
                    print("\rNow playing at {:.2f}s".format(value), end = "", flush = True)

            else:
                break                                                                               #exits the loop
            """
