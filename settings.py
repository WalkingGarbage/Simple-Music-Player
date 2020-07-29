#!/usr/bin/env python3

import os

def setup(confdir, tempdir, playlist):
    """ Create the playlist file """

    if not os.path.exists(confdir):
        os.makedirs(confdir)
        print("Created config directory!")

    if not os.path.exists(tempdir):
        os.makedirs(tempdir)
        print("Created temp directory!")

    f = open(tempdir + playlist, 'w+')
    f.write("") # Empties the directory file
    f.close()

def checkPath(path):
    """ Check if there are any audio files """

    stat = True

    if path[-1] != '/': # Check if the path was written correctly
        path += '/' # Add a '/' at the end of the path

    for file in os.listdir(path): # Check if the path has audio files
        if file.endswith(".mp3") or file.endswith(".waw"):
            stat = False
            break

    if stat:
        raise FileNotFoundError(
                "There isn't any .mp3 or .waw files in this directory"
                )
