#!/usr/bin/python3
"""
Changes spaces to underscores in file names
"""
import os
import glob
from sys import argv

def spaces_to_underscores(fname):
    if not os.path.exists(fname):
        print(f"Could not find {fname}")
        return
    if ' ' not in fname:
        return
    fname_new = fname.replace(' ', '_')
    os.rename(fname, fname_new)
    print(f"{fname} -> {fname_new}")

# Default to processing all files, otherwise args only
flist = glob.glob("*") if len(argv) == 1 else argv[1:]

for fname in sorted(flist):
    spaces_to_underscores(fname)
