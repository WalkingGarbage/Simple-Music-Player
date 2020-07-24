#!/usr/bin/env python3

import os
#import globals



def setup(confdir, tempdir, playlist):

    if not os.path.exists(confdir):
        os.makedirs(confdir)
        print("Created config directory!")

    if not os.path.exists(tempdir):
        os.makedirs(tempdir)
        print("Created temp directory!")

    f = open(tempdir + playlist, 'w+')
    f.write("")                                                                                 #empties the directory file
    f.close()

def setplaylist(path):

    playlist = open(globals.tempdir + 'playlist.txt', 'a+')

    for file in os.listdir(path):
        if file.endswith(".mp3") or file.endswith(".wav"):                                      #checks the files' extension
            playlist.write(file + '\n')
    playlist.close()

def checkddir():

    ddir = open(globals.confdir + 'ddir.conf', 'r')
    out = ddir.readline()
    ddir.close()

    return out


def setddir():
     
    ddir = open(globals.confdir + 'ddir.conf', 'w+')
    ddir.write("")
    ddir.close()

    ddir = open(globals.confdir + 'ddir.conf', 'a+')
    ddir.write(input("New music directory:"))



