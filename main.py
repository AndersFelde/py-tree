#!/bin/python3
from direc import direc
import sys
import os
import argparse

parser = argparse.ArgumentParser("Argument parser")

parser.add_argument("--out", "-o", type=str,
                    help="file to write output to", dest="outFile", default=False)
parser.add_argument("--maxDepth", "-mD", type=int, default=False,
                    help="max depth it will explore in directories", dest="maxDepth")
parser.add_argument("direcName", type=str, default=os.getcwd(), nargs="?",
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
    root = direc(res.direcName, 0, maxDepth=res.maxDepth, outFile=f)
except:
    print(f"'{res.direcName}' does not exist")
    if(f):
        f.close()
    exit()
if not f:
    print(root)
else:
    f.write(str(root))

root.searchDir()

if(f):
    f.close()
