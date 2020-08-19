import ntpath
import os


class dir():

    def searchDir(self):
        dirChilds = []
        # fileChilds = []
        dirs = os.listdir(self.path)
        for d in dirs:
            if os.path.isdir(self.path + "\\" + d):
                newDir = dir(self.path + "\\" + d, self.depth+1, self)
                print(newDir)
                dirChilds.append(newDir)
            else:
                print(("--" * self.depth+1) + "\\" + d)

        # return [dirChilds, fileChilds]
        return dirChilds

    def __init__(self, path, depth, parent=None):
        self.path = path
        self.depth = depth
        self.parent = parent
        print(self.printSelf())
        # childs = self.searchDir()
        self.dirChilds = self.searchDir()
        # self.fileChilds = childs[1]

    def printSelf(self):
        return ("--" * self.depth) + ntpath.basename(self.path)
