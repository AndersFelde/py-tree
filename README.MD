# Python Tree
## A python3 script that prints your directories in a tree format


# Setup
```
pip install termcolor
pip install ntpath
```

# Usage

```
usage: Py-tree [-h] [--out OUTFILE] [--maxDepth MAXDEPTH] [directoryName]

positional arguments:
  directoryName         name of directory you want to be listed

optional arguments:
  -h, --help            show this help message and exit
  --out OUTFILE, -o OUTFILE
                        file to write output to
  --maxDepth MAXDEPTH, -mD MAXDEPTH
                        max depth it will explore in directories
```