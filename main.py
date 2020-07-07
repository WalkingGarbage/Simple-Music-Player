#!/usr/bin/env python3

import os
import player
import string
import globals


globals.initialize()
path = "/home/fra/PycharmProjects/prototype/audio/"


player.listtracks(path)

while True:
    i = player.select(globals.queue)
    player.play(globals.queue[i], path)
    y=input("Press Q to end the program or any other key to select another track ")
    if y=='q' or y=='Q':
        break

