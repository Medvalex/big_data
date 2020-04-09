#!/opt/anaconda/envs/bd9/bin/python

import sys

def emit(key,value):
    sys.stdout.write("{}\t{}\n".format(key, value))

def reducer():
    
    prev_key = None
    count = 0

    for line in sys.stdin:
        objects = line.strip().split('\t')
        key = objects[0]
        if key != prev_key and key != None:
            emit(key, count)
            count = 0
        count += 1
        prev_key = key
    if prev_key != None:
        emit(key, count)

if __name__ == '__main__':
    reducer()
