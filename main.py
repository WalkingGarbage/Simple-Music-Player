#!/usr/bin/env python3

import player

path = "/home/fra/Music/"
queue = player.queue(path)
queue.listtracks()
queue.seltracks()
queue.play()
queue.loop()
