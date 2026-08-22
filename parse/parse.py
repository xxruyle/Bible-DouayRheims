'''
Parsing script for a selection of a chapter

Assumes that each chapter is followed by the seperator `____________________`

Replace temp.txt with a chapter
'''

import json 
import re
file = open('./temp.txt').readlines()

txt = ""

out = {}

for line in file: 
    txt += line.strip() + "\n"


splt = txt.split("____________________")

pattern = r'^\d+ '
for ch_num, ch in enumerate(splt): 
    lsplt = ch.split("\n")
    out[ch_num+1] = {}
    verse_num = 1
    for line in lsplt: 
        if len(line) >= 2: 
            if (re.match(pattern, line)): 
                out[ch_num+1][verse_num] = re.sub(pattern, '', line)
                verse_num += 1


with open(f'./temp.json', 'w') as f:
    json.dump(out, f, indent=True)