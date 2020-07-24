#!/usr/bin/env python3

import player
import ascii
import settings
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



path = "/home/antonio/Musica/Playlist - Salmo/MP3/"                           #sets the default directory
queue = player.queue(path)                          #initializes the queue


#globals.init()
settings.setup(queue.getconf()[0], queue.getconf()[1], queue.getconf()[2])                                    #creates the enviroment
queue.listtracks()                                  #prints a list of all audio files in the default directory
queue.seltracks()                                   #select a track from the list
queue.play()                                        #plays the selected track
queue.loop()                                        #sets a loop where the user can perform different actions
