#!/bin/python3
import ntpath
import os
from termcolor import cprint


class direc():
    def __init__(self, path, depth, maxDepth=False, outFile=False):
        self.path = path
        if(not self.exists()):
            raise(Exception())
        self.depth = depth
        self.maxDepth = maxDepth
        self.outFile = outFile

    def exists(self):
        return os.path.isdir(self.path)

    def searchDir(self):
        if self.maxDepth and self.depth == self.maxDepth:
            return

        if os.name != "nt":
            sl = "/"
        else:
            sl = "\\"
        try:
            dirs = os.listdir(self.path)
        except:
            self.__printOut()
            return
        for d in dirs:
            if os.path.isdir(self.path + sl + d):
                newDir = direc(self.path + sl + d, self.depth +
                               1, outFile=self.outFile, maxDepth=self.maxDepth)
                self.__printOut(newDir, "dir")
                # if(self.outFile):
                #     self.outFile.write(str(newDir))
                newDir.searchDir()
            else:
                self.__printOut(d, type="file")

    def __str__(self):
        return ("    " * self.depth) + "└─" + ntpath.basename(self.path) + "/"

    def __printOut(self, string=None, type=None):
        if not self.outFile:
            if(type == "dir"):
                cprint(string, "blue")
            elif(type == "file"):
                cprint(("    " * (self.depth+1)) + "└─ " + string, "green")
            else:
                cprint(f"Was not able to access '{self.path}'", "red")
        else:
            if(type == "dir"):
                self.outFile.write(str(string) + "\n")
            elif(type == "file"):
                self.outFile.write(
                    ("    " * (self.depth+1)) + "└─ " + string + "\n")
            else:
                self.outFile.write(
                    f"Was not able to access '{self.path}'" + "\n")


if __name__ == "__main__":
    root = direc(os.getcwd(), 0)
    print(root)
    root.searchDir()
