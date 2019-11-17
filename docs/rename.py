#!/usr/bin/env python

import os
from shutil import copy2, rmtree

os.chdir('..')

MAINDIR = ('random-violence',  'vandalism-and-police-actions', 'hk-universities', 'media', 'oxford', 'misc')

for d in MAINDIR:
    for d1 in os.listdir(d):
        sd = '/'.join([d, d1]) 
        if os.path.isdir(sd):
            for i, f in enumerate(list(os.listdir(sd))):
                _, ext = os.path.splitext(f)
                if ext:
                    if ext == '.txt':
                        os.rename('/'.join([sd, f]), '/'.join([sd, d1+ext]))
                    else:
                        os.rename('/'.join([sd, f]), '/'.join([sd, d1+str(i)+ext]))