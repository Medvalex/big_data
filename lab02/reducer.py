#!/opt/anaconda/envs/bd9/bin/python

import sys

def emit(key,value):
    sys.stdout.write("{}\t{}\n".format(key, value))

def reducer():
    for line in sys.stdin:
        objects = line.strip().split('\t')
        emit(objects[0],objects[1])

if __name__ == '__main__':
    reducer()
