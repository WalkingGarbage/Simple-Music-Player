#!/usr/bin/env python3

import player
import ascii
import settings
import sys
import os
#import globals


    ##################################
    #                                #
    #              LOGO              #
    #                                #
    ##################################


ascii.title()
ascii.logo()
ascii.spacer()



    ##################################
    #                                #
    #           MAIN CORE            #
    #                                #
    ##################################

stat = True

try:
    if os.path.exists(sys.argv[1]):
        path = sys.argv[1]
except IndexError:
    path = input("Insert path: ")
    while not os.path.exists(path):
        path = input("Insert path: ")

if path[-1] != '/':
    path += '/'

for file in os.listdir(path):
    if file.endswith(".mp3") or file.endswith(".waw"):
        stat = False
        break

if stat:
    raise FileNotFoundError("There isn't any .mp3 or .waw files in this directory")

queue = player.queue(path)                          #initializes the queue
#globals.init()
settings.setup(queue.getconf()[0], queue.getconf()[1], queue.getconf()[2])                                    #creates the enviroment
queue.listtracks()                                  #prints a list of all audio files in the default directory
queue.seltracks()                                   #select a track from the list
queue.play()                                        #plays the selected track
queue.loop()                                        #sets a loop where the user can perform different actions
