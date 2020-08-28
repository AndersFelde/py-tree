#!/bin/python3
from dependecies.direc import direc
import sys
import os
import argparse
from termcolor import cprint

parser = argparse.ArgumentParser("Py-tree")

parser.add_argument("--out", "-o", type=str,
                    help="file to write output to", dest="outFile", default=False)
parser.add_argument("--maxDepth", "-mD", type=int, default=False,
                    help="max depth it will explore in directories", dest="maxDepth")
parser.add_argument("directoryName", type=str, default=os.getcwd(), nargs="?",
                    help="name of directory you want to be listed")
# nargs="?" for at den ikke skal være required


res = parser.parse_args()

if(res.outFile):
    print(f"Outfile: {res.outFile}")
    f = open(res.outFile, "w", encoding="utf-8")
else:
    f = False
if(res.maxDepth):
    print(f"Max Depth: {res.maxDepth}")


try:
    root = direc(res.directoryName, 0, maxDepth=res.maxDepth,
                 outFile=f, last="Root")
except:
    print(f"'{res.directoryName}' does not exist")
    if(f):
        print("Closed file")
        f.close()
    exit()

if not f:
    cprint(root, "yellow")
else:
    f.write(str(root) + "\n")

root.searchDir()

if(f):
    f.close()
