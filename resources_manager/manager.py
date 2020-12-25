class Manager:

    def __init__(self, player, persistence):
        """ Initializing player and persistence """
        # TODO: Initialize an object for the UserInterface

        self.__player = player
        self.__persistence = persistence
        
        self.__persistence.createPlaylistFile()

    def createPlaylistFile(self):
        """ Create playlist file """
        
        self.__persistence.createPlaylistFile()

    def playSong(self):
        """ Start a song """

        nSong = self.__player.getCounter()
        songPath = self.__persistence.getSongN(nSong)
        
        self.__player.playSong(songPath)
    
    def stopSong(self):
        """ Stop a song """

        self.__player.stopSong()
