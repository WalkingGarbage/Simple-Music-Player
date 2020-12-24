import os
import mpv
import shutil

class Player:

    def __init__(self):
        """ Initialize Player """     

        self.path = os.path.expanduser("~") + "/Teddie Music/"
        
        if not os.path.exists(self.path):
            os.makedirs(self.path)
        
        try:
            os.mknod(self.path + "player.txt")
        except:
            pass

    def setPath(self, path):
        """ Method to set another path """

        if not os.path.exists(path):
            raise Exception("Path doesn't exist")

        # Delete the default path with its content to set another default path
        shutil.rmtree(self.path)
        os.mknod(path + "player.txt")

        self.path = path

    def getPath(self):
        """ Method that return the default path """

        return self.path

        



