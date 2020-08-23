#!/bin/python3
import ntpath
import os
from termcolor import cprint, colored


class direc():
    # short for direcTORY
    def __init__(self, path, depth, maxDepth=False, outFile=False, outString=""):
        self.path = path
        if(not self.exists()):
            raise(Exception())
        self.depth = depth
        self.maxDepth = maxDepth
        self.outFile = outFile
        self.sl = os.sep
        self.outString = outString

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
                outString = self.outString + "│   "
                newDir = direc(self.path + self.sl + d, self.depth +
                               1, outFile=self.outFile, maxDepth=self.maxDepth, outString=outString)
                self.__printOut(str(newDir), type="dir")
                newDir.searchDir()
            else:
                self.__printOut(d, type="file")

        del self
        # spare RAM fordi objekt er ikke lenger nødvendig

    def __str__(self):
        return ((self.outString) + "└─" + ntpath.basename(self.path) + self.sl)

    def __printOut(self, string="", type=None):
        fileString = self.outString + "└─ "
        errorString = [self.outString + "    ",
                       f"Was not able to access '{self.path + self.sl}'"]

        if not self.outFile:
            if(type == "dir"):
                cprint(string, "blue")
            elif(type == "file"):
                print(colored(fileString, "blue") +
                      colored(string, "green"))
            else:
                print(colored(errorString[0], "blue") +
                      colored(errorString[1], "red"))
        else:
            if(type == "dir"):
                self.outFile.write(string + "\n")
            elif(type == "file"):
                self.outFile.write(fileString + string + "\n")
            else:
                self.outFile.write(errorString[0] + errorString[1] + "\n")


if __name__ == "__main__":
    root = direc(os.getcwd(), 0)
    cprint(root, "yellow")
    root.searchDir()
