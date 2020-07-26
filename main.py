#!/usr/bin/env python3

import player
import ascii
import settings
import sys
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

if len(sys.argv) != 1:
    path = sys.argv[1]                           #sets the default directory
else:
    print("Error: Insert a path to a playlist!")
    exit(1)

queue = player.queue(path)                          #initializes the queue
#globals.init()
settings.setup(queue.getconf()[0], queue.getconf()[1], queue.getconf()[2])                                    #creates the enviroment
queue.listtracks()                                  #prints a list of all audio files in the default directory
queue.seltracks()                                   #select a track from the list
queue.play()                                        #plays the selected track
queue.loop()                                        #sets a loop where the user can perform different actions
