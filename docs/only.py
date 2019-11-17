#!/usr/bin/env python

import os
from shutil import copy2, rmtree

os.chdir('..')

MAINDIR = ('random-violence',  'vandalism-and-police-actions', 'hk-universities', 'media', 'oxford', 'misc')

rmtree('_pic_only', )
rmtree('_video_only')
os.mkdir('_pic_only')
os.mkdir('_video_only')
for d in ['_pic_only', '_video_only']:
    for d1 in MAINDIR:
        os.mkdir('/'.join([d, d1]))

for d in MAINDIR:
    for d1 in os.listdir(d):
        sd = '/'.join([d, d1]) 
        if os.path.isdir(sd):
            for i, f in enumerate(list(os.listdir(sd))):
                fn, ext = os.path.splitext(f)
                ext = ext.lower()
                if ext in ('.jpeg', '.jpg'):
                    copy2('/'.join([sd, f]), '/'.join(['_pic_only', d, f]))
                elif ext in ('.mp4', '.mov', '.avi'):
                    copy2('/'.join([sd, f]), '/'.join(['_video_only', d, f]))
                elif ext == '.txt':
                    copy2('/'.join([sd, f]), '/'.join(['_pic_only', d, f]))
                    copy2('/'.join([sd, f]), '/'.join(['_video_only', d, f]))


