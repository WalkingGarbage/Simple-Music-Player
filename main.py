#!/usr/bin/env python3

__author__ = "WalkingGarbage, open-antux"
__version__ = 0.1

from resources_manager import manager
from domain import player
from persistance import filePersistence

# TODO: Add UserInterface object
manager = manager.Manager(
    player.Player(),
    filePersistence.Persistence()
)

manager.playSong()
manager.stopSong()

"""
import player
import ascii
import settings
import sys
import os

    ##################################
    #                                #
    #              LOGO              #
    #                                #
    ##################################


print(ascii.title() + "\n" + ascii.logo()) # Show title and logo
print("\n\n\n") # Spacer
os.path.exists
    ##################################
    #                                #
    #           MAIN CORE            #
    #                                #
    ##################################

stat = True

while stat:
    try:
        if os.path.exists(sys.argv[1]): # Check if the path exist
            path = sys.argv[1] 
    except IndexError: # If there isn't arguments
        path = input("Insert path: ") 
        while not os.path.exists(path):
            path = input("Insert path: ")
    stat = False
    if settings.checkPath(path):
        stat = True

queue = player.queue(path) # Initializes the queue
settings.setup(queue.getconf()[0], 
        queue.getconf()[1], 
        queue.getconf()[2]) # Creates the enviroment
queue.listtracks() # Prints a list of all audio files in the default directory
queue.seltracks() # Select a track from the list
queue.play() # Plays the selected track
queue.loop() # Sets a loop where the user can perform different actions
"""
