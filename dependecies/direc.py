#!/bin/python3
import ntpath
import os
from termcolor import cprint, colored


class direc():
    # short for direcTORY
    def __init__(self, path, depth, maxDepth=False, outFile=False, outString="", last=False):
        self.path = path
        if(not self.exists()):
            raise(Exception())
        self.depth = depth
        self.maxDepth = maxDepth
        self.outFile = outFile
        self.sl = os.sep
        self.outString = outString
        self.last = last
        self.signs = {False: "├─", True: "└─", "Root": ""}
        self.typesOfOutstrings = {True: "    ", False: "│   ", "Root": "    "}

    def exists(self):
        return os.path.isdir(self.path)

    def __createNewDirec(self, d, last):
        outString = self.outString + self.typesOfOutstrings[self.last]
        newDir = direc(self.path + self.sl + d, self.depth +
                       1, outFile=self.outFile, maxDepth=self.maxDepth, outString=outString, last=last)
        self.__printOut(str(newDir), type="dir")
        newDir.searchDir()

    def searchDir(self):
        if self.maxDepth and self.depth == self.maxDepth or self.__str__().find(".git/") > 0:
            return

        try:
            dirs = os.listdir(self.path)
        except:
            self.__printOut(type="Error")
            # printer rød error
            return

        last = False

        for d in dirs:
            if d == dirs[-1]:
                # checks if is last element in folder
                last = True
            if os.path.isdir(self.path + self.sl + d):
                self.__createNewDirec(d, last)
            else:
                self.__printOut(d, type="file", last=last)

        del self
        # spare RAM fordi objekt er ikke lenger nødvendig

    def __str__(self):
        return ((self.outString) + self.signs[self.last] + ntpath.basename(self.path) + self.sl)

    def __printOut(self, string="", type=None, last=False):
        fileString = self.outString + \
            self.typesOfOutstrings[self.last] + self.signs[last]

        errorString = [self.outString + self.typesOfOutstrings[False],
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
    print("U know joe?")
