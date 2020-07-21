#!/usr/bin/env python3

import os
import pyglet

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
                print (num - 1)
                self.song = self.tracks[num - 1]
                break
            else:
                print ("Select a number in the given list!")

    def play(self):
        print(self.song)
        source = pyglet.media.load(self.dir + self.song)
        source.play()
