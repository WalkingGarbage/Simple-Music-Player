#!/usr/bin/env python3

import player
import ascii


    ##################################
    #                                #
    #           ASCII ART            #
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


path = "/home/fra/Music/"                           #sets the default directory
queue = player.queue(path)                          #initializes the queue
queue.listtracks()                                  #prints a list of all audio files in the default directory
queue.seltracks()                                   #select a track from the list
queue.play()                                        #plays the selected track
queue.loop()                                        #sets a loop where the user can perform different actions
