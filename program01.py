#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Ajeje the librarian, recently found a hidden room
in the Keras Library (a great place located in
Umkansa, the largest village in the White Mountains).
There, she discovered several books, containing
music scores of ancient Tarahumara songs.
So, she invited over a musician friend to have a look
at them, and he informed her that the scores are
written in Tarahumara notation and need to be translated
into a notation familiar to Umkansanian musicians,
so they can play them back.

Tarahumaras used numbers instead of letters for
writing notes:
0 in place of A, 1 in place of B, and so on, until
7 in place of G. Flat (b) and sharp (#) notes
(see note 3 below, if you do not know what flat
and sharp notes are)
were followed by a - and a +, respectively (for example,
0- meant flat A). Moreover, they just repeated the
same number multiple times to represent the note's
duration. For example, 0000 would mean that the
A note had a length of 4, while 0-0-0-0- would mean
that the A flat note had a length of 4.
Pauses were written down
as spaces; for example, twelve spaces represent
a pause of 12. Both notes and pauses could span
different lines of the score (e.g., starting on line
x and continuing on line x + 1, x + 2, and so on).
Finally, music scores were written from right
to left and from top to bottom, and going to a new
line did not mean anything in terms of the music score.
Umkansanians, instead, are used to write down notes using letters,
and each note is followed by its duration (so, the example
above would be written as A4). Flat and sharp notes are
followed by a b or a #, respectively (for example, A flat
is written as Ab, so the example above would be written ad
Ab4). Pauses are written using the letter P, followed by
their duration, and no spaces are used at all.
Finally, they are used to read music from left
to right on a single row.

As Ajeje knows that you are a skilled programmer, she
provides you with a folder containing the transcription
of all the Tarahumara songs she found, organized in
multiple subfolders and files (one song per file).
Also, she prepared an index file in which each row
contains the title of a Tarahumara song (in quotes),
followed by a space and the path of the file containing
that song (in quotes, relative to the root folder).
She would like to translate all the songs listed in
the index and store them into new files, each one
named with the title of the song it contains (.txt),
in a folder structure matching the original one.
Also, she would like to store in the root folder of
the created structure, a file containing on each row
the title of a song (in quotes) and the corresponding
song length, separated by a space. Songs in the index
need to be ordered in descending length and, if the
length of some songs is the same, in ascending alphabetical
order. The length of a song is the sum of the durations
of all notes and pauses it is made of.

Would you be able to help Ajeje out in translating
the Tarahumara songs into Umkansanian ones?

Note 0: below, you are provided with a function to
Umkansanize the Tarahumara songs; after being executed,
it must return a dictionary in which each key is a song
title and the associated value is the song's duration

Note 1: the songs index file index.txt
is stored in the source_root folder

Note 2: the index of the translated songs
index.txt is in the target_root folder

Note 3: flat and sharp notes are just "altered" versions
of regular notes; for example an F# ("F sharp") is the
altered version of an F, that is, an F note which is a
half of a tone higher than a regular F; the same holds for
flat notes, which are a half of a tone lower than regular notes;
from the point of view of the homework, flat and sharp notes
must be treated the same as regular notes (except for their notation).

Note 4: to create the directory structure you can use the 'os' library functions
(e.g. os.makedirs)
'''

import os

def Translate(sourceFile:str):
    with open(sourceFile, encoding="utf8") as f:
        data = f.read().split("\n")
    data = [i[::-1] for i in data]
    data = list("".join(data))
    
    newlist = []
    translation = {
        "0": "A",
        "1": "B",
        "2": "C",
        "3": "D",
        "4": "E",
        "5": "F",
        "6": "G",
        "-": "b",
        "+": "#",
        " ": "P"
        }
    
    lowestIndex = 0 ### save lowest index and add special char at that index
    for i, val in enumerate(data):
        if val not in {"b", "+", "-"}: #val.isnumeric() or val == " ":
            newlist.append(translation[val]) 
            lowestIndex += 1
        else:
            # newlist.append("")
            # newlist[i-1] += translation[val]
            newlist[lowestIndex-1] += translation[val]
    # finalList = []
    # for i in newlist:
    #     if i:
    #         finalList.append(i)
            
    count = 1
    length = 0
    out = ""
    for i in range(1, len(newlist)):
        if newlist[i] == newlist[i-1]:
            count += 1
        else:
            out += newlist[i-1] + str(count)
            length += count
            count = 1
    out += newlist[-1] + str(count)
    length += count
    
    return (out, length)
    pass

def Title(source_root):
    indexFile = source_root + "/index.txt"
    with open(indexFile, encoding="utf8") as f:
        data = f.read().split('"')
        # data = [[x for x in line.split()] for line in f.read().split("\n")]
    print(data)
    titleFileDict = {}
    title = True
    for i in range(1, len(data), 2):
        if title:
            titleFileDict[data[i]] = ""
            title = False
        else:
            titleFileDict[data[i-2]] = data[i]
            title = True
    
    return titleFileDict

def Umkansanize(source_root:str, target_root:str) -> dict[str,int]:
    os.makedirs(target_root, exist_ok=True)
    index = Title(source_root)
    outDict = []
    for i in index:
        translated, length = Translate(source_root + "/" + index[i])
        if len(index[i]) > 5:
            pathPart, fileName = os.path.split(index[i])
            os.makedirs(target_root + "/" + pathPart, exist_ok=True)
            file = target_root + "/" + pathPart + "/" + i + ".txt"
        else:
            file = target_root + "/" + i + ".txt"
        
        with open(file, "w", encoding="utf8") as f:
            f.write(translated)
        outDict.append([i, length])
    outDict = dict(sorted(outDict, key = lambda item: (-item[1], item[0])))
    
    indexFile = ['"' + str(i) + '"' + " " + str(outDict[i]) + "\n" for i in outDict]
    with open(target_root + "/index.txt", "w", encoding="utf8") as f:
        f.writelines(indexFile)
    
    return outDict
    pass

if __name__ == "__main__":
    Umkansanize("Tarahumara", "Umkansanian")

