#!/usr/bin/env python3

import gi
import multiprocessing
from playsound import playsound
import os
import sys
import globals

def play(track, path):                                          #plays a song
    file = path + track
    p = multiprocessing.Process(target=playsound, args=(file,))
    p.start()
    input("press ENTER to stop the track: ")
    p.terminate()


def select(list):                                               #select the song to play from the queue
    while True:
        i = input("Select the audio (number): ")
        if i == '':
            i=0
        else:
            i = int(i)
        if i <= len(list) and i!=0:
            return (i - 1)
            break
        else:
            print("The number must be in the given list!")


def listtracks(path):                                           #prints a list of the songs in a folder and puts them on the queue
    globals.initialize()
    x = 0
    for file in os.listdir(path):
        if file.endswith(".mp3") or file.endswith(".wav"):
            print(str(x+1) + ' ' + file)
            globals.queue = globals.queue + [file]
            x=x+1

