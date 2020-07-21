#!/usr/bin/env python3

import player
import ascii

ascii.title()
ascii.logo()
path = "/home/fra/Music/"
queue = player.queue(path)
queue.listtracks()
queue.seltracks()
queue.play()
queue.loop()
