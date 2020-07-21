#!/usr/bin/env python3

import player

path = "/home/fra/Music/"
queue = player.queue(path)
queue.listtracks()
queue.seltracks()
queue.play()
while True:
    stop = input("Press ENTER to stop")
    break
