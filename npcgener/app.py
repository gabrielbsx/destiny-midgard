# -*- coding: utf-8 -*-
import json
from google_trans_new import google_translator


def readNPCGener():
    translate = google_translator()
    npcs = {}
    with open('NPCGener.txt', 'r', encoding='euc_kr', errors='ignore') as gener:
        with open('mobname.txt', 'w') as mobname:
            id = -1
            for line in gener.readlines():
                if line[0] == '/':
                    pass
                elif line[0] == '#':
                    line = line.replace('#', '').replace(' ', '').replace('\t', '').replace('[', '').replace(']', '')
                    id = int(line)
                    npcs[id] = {}
                    npcs[id]['id'] = line
                else:
                    line = line.replace(' ', '').replace('\t', '').replace('\r', '').replace('\n', '')
                    if len(line) > 0:
                        if id >= 0:
                            data = line.split(':')
                            if data[0] == 'Leader' or data[0] == 'Follower':
                                name = translate.translate(data[1], lang_tgt='en')
                                npcs[id][data[0] + '_before'] = data[1]
                                npcs[id][data[0]] = name.replace(' ', '_')
                                print('[{0}]: {1} {2}'.format(data[0], npcs[id][data[0] + '_before'], npcs[id][data[0]]))
                            else:
                                npcs[id][data[0]] = data[1]
            mobname.close()
        gener.close()
        
        
        
if __name__ == '__main__':
    readNPCGener()