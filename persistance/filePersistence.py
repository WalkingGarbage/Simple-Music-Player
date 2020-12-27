import os

class Persistence:

    def __init__(self):
        """ Initializing and creating settings config file and directory """

        self.__path = os.path.expanduser("~") + "/Teddie Music/"

        if not os.path.exists(self.__path):
            os.makedirs(self.__path)
        
        try:
            os.makedirs(self.__path + "Music")
            os.mknod(self.__path + "playlist.txt")
        except:
            pass

        self.__musicDirectory = self.__path + "Music"
        self.__playlist = self.__path + "playlist.txt"

    def createPlaylistFile(self):
        """ Populate of songs the playlist """

        f = open(self.__playlist, "w+")

        for dirpath, _, files in os.walk(self.__musicDirectory):  
            for song in files:
                if song.endswith(".mp3") or song.endswith(".wav"):
                    f.writelines(dirpath + "/" + song + "\n")

        f.close()
    
    def getSongN(self, n):
        """ Return the path of the song on the N line of the file """

        f = open(self.__playlist, "r")
        songs = f.readlines()

        if(len(songs) == 0):
            print("No songs in playlist")
        elif(n > len(songs)):
            n = 0

        return songs[n].replace("\n", "")
