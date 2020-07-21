#!/usr/bin/env python3

import os

class queue:

    def __init__(self, path):
        self.dir = path
        pass

    def listtracks(self):
        tracks = []
        x = 0
        for file in os.listdir(self.dir):
            if file.endswith(".mp3") or file.endswith(".wav"):
                print(str(x+1) + ' ' + file)
                tracks = tracks + [file]
                x=x+1

