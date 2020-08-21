#!/bin/python3
import ntpath
import os
from termcolor import cprint


class direc():
    # short for direcTORY
    def __init__(self, path, depth, maxDepth=False, outFile=False):
        self.path = path
        if(not self.exists()):
            raise(Exception())
        self.depth = depth
        self.maxDepth = maxDepth
        self.outFile = outFile
        self.sl = self.__getSl()

    def exists(self):
        return os.path.isdir(self.path)

    def searchDir(self):
        if self.maxDepth and self.depth == self.maxDepth:
            return

        try:
            dirs = os.listdir(self.path)
        except:
            self.__printOut()
            # printer rød error
            return

        for d in dirs:
            if os.path.isdir(self.path + self.sl + d):
                newDir = direc(self.path + self.sl + d, self.depth +
                               1, outFile=self.outFile, maxDepth=self.maxDepth)
                self.__printOut(str(newDir), type="dir")
                newDir.searchDir()
            else:
                self.__printOut(d, type="file")

        del self
        # spare RAM fordi objekt er ikke lenger nødvendig

    def __str__(self):
        return ("    " * self.depth) + "└─" + ntpath.basename(self.path) + self.sl

    def __getSl(self):
        if os.name != "nt":
            return "/"
        else:
            return "\\"

    def __printOut(self, string="", type=None):
        fileString = ("    " * (self.depth+1)) + "└─ " + string

        errorString = ("    " * (self.depth+1)) + \
            f"Was not able to access '{self.path + self.sl}'"

        if not self.outFile:
            if(type == "dir"):
                cprint(string, "blue")
            elif(type == "file"):
                cprint(fileString, "green")
            else:
                cprint(errorString, "red")
        else:
            if(type == "dir"):
                self.outFile.write(string + "\n")
            elif(type == "file"):
                self.outFile.write(fileString + "\n")
            else:
                self.outFile.write(errorString + "\n")


if __name__ == "__main__":
    root = direc(os.getcwd(), 0)
    cprint(root, "yellow")
    root.searchDir()
