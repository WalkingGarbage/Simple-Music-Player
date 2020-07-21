#!/usr/bin/env python3

import os
import pyglet
import mpv
from playsound import playsound


pyglet.options['search_local_libs'] = True


class queue:

    def __init__(self, path):
        self.dir = path
        pass

    def listtracks(self):
        self.tracks = []
        x = 0
        for file in os.listdir(self.dir):
            if file.endswith(".mp3") or file.endswith(".wav"):
                print(str(x+1) + ' ' + file)
                self.tracks = self.tracks + [file]
                x=x+1

    def seltracks(self):
        
        while True:
            num = int(input("Select the track: "))
            if num > 0 and num <= len(self.tracks):
                self.song = self.tracks[num - 1]
                break
            else:
                print ("Select a number in the given list!")

    def play(self):
        print(self.song)
        self.source = mpv.MPV(ytdl=True)
        self.source.play(self.dir + self.song)
    
    def loop(self):
        while True:
            action = input("Input: ")
            if action == 'p' or action == 'P':
                if self.source.pause == False:
                    self.source.pause = True
                else:
                    self.source.pause = False
            else:
                break

