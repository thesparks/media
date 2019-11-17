#!/usr/bin/env python



import os
from shutil import copy2, rmtree

os.chdir('..')

MAINDIR = ('random-violence',  'vandalism-and-police-actions', 'hk-universities', 'media', 'oxford', 'misc')

with open('.etc/index.md', 'w') as indexfile:
    indexfile.write('''\
---
output:
    rmarkdown::html_document:
        number_sections: true
        toc: true
---

''')
    for h1 in MAINDIR:
        indexfile.write(f'# {h1}\n\n')      ############################
        for h2 in os.listdir(h1):
            sd = '/'.join([h1, h2]) 
            if os.path.isdir(sd):
                indexfile.write(f'## {h2}\n\n')    ############################
                try:
                    with open(f'{sd}/{h2}.txt') as infofile:
                        info = infofile.read()
                    indexfile.write(f'{info}\n\n')      ############################
                except:
                    pass
                fp_s = list(map(lambda fn: f'../{sd}/{fn}', os.listdir(sd)))
                print(fp_s)
                for fp in fp_s:
                    _, ext = os.path.splitext(fp)
                    ext = ext.lower() 
                    if ext in ('.jpeg', '.jpg'):
                        indexfile.write(f'![]({fp})\n\n')        ############################
                    elif ext in ('.mp4', '.mov', '.avi'):
                        indexfile.write(f'[click to view video]({fp})\n\n')   ############################

with open('.etc/index_critical.md', 'w') as indexfile:
    indexfile.write('''\
---
output:
    rmarkdown::html_document:
        number_sections: true
        toc: true
---

''')
    for h1 in MAINDIR:
        indexfile.write(f'# {h1}\n\n')      ############################
        for h2 in os.listdir(h1):
            sd = '/'.join([h1, h2]) 
            if os.path.isdir(sd):
                if '0' in h2.split('-'):
                    indexfile.write(f'## {h2}\n\n')    ############################
                    try:
                        with open(f'{sd}/{h2}.txt') as infofile:
                            info = infofile.read()
                        indexfile.write(f'{info}\n\n')      ############################
                    except:
                        pass
                    fp_s = list(map(lambda fn: f'../{sd}/{fn}', os.listdir(sd)))
                    print(fp_s)
                    for fp in fp_s:
                        _, ext = os.path.splitext(fp)
                        ext = ext.lower() 
                        if ext in ('.jpeg', '.jpg'):
                            indexfile.write(f'![]({fp})\n\n')        ############################
                        elif ext in ('.mp4', '.mov', '.avi'):
                            indexfile.write(f'[click to view video]({fp})\n\n')   ############################