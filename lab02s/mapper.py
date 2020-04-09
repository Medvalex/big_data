#!/opt/anaconda/envs/bd9/bin/python

#*This is a second lab super achivment part by A. Medvedev

import sys
import re

def emit(key, value):
    sys.stdout.write("{}\t{}\n".format(key, value))

def map(key, timestamp, url):
    if key != '-':
        if len(url) != 0:
            if re.match(r'http',url) is not None:
                emit(url, 1)

def mapper():
    for line in sys.stdin:
        objects = line.strip().split('\t')
        if len(objects) == 3:
            map(objects[0], objects[1], objects[2])

if __name__ == '__main__':
    mapper()