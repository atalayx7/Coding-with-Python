#!/usr/bin/env python3
#List files recursively on the current directory 
import os

path = os.path.dirname(os.path.realpath(__file__))
files = []
directorie = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        directorie.append(os.path.join(r, file))

for f in directorie:
    f = f.split('/')[-1]
    files.append(f)
    if f == 'mal.py':
        continue
    else:
        print(f)
