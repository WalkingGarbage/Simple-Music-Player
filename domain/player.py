import mpv

class Player:

    def __init__(self):
        """ Initializing attributes """
        #self.__source = mpv.MPV(ytdl=True, terminal=True, input_terminal=True, loglevel='debug')
        self.__source = mpv.MPV(ytdl = True, terminal = False)
        self.__counter = 0

    def playSong(self, pathSong):
        """ Start the song """
        
        self.__source.play(pathSong)
        self.__source.wait_for_playback()

    def stopSong(self):
        """ Stop the song """

        # TODO: Looking for a way to stop the song
        self.__source.terminate()

    def getCounter(self):
        """ Return the index of the playlist """

        return self.__counter
