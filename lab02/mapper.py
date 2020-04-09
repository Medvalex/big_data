#!/opt/anaconda/envs/bd9/bin/python

import sys
import re
import happybase 

def emit(key, value, timestamp):
    table.put(key,{b"cf1:column":value}, timestamp = timestamp)


def map(key, timestamp, url):
    if key.isdigit():
        key = int(key) 
        if key % 256 == 157: 
            if is_float(timestamp):
                if re.match(r'http',url) is not None:
                    timestamp = int(float(timestamp)*1000) 
                    value = "{}:{}".format(timestamp, url)  
                    emit(key,value, timestamp)

def mapper():
    for line in sys.stdin:
        objects = line.strip().split('\t')
        if len(objects) == 3:
            map(objects[0], objects[1], objects[2])

def is_float(str):
    try:
        float(str)
        return True
    except:
        return False

if __name__ == '__main__':
    connection = happybase.Connection("spark-node2.newprolab.com", 9090, autoconnect = False)
    try:
        connection.open()
    except Exeption as fuck:
        print(fuck)

    table = connection.table("alexander.medvedev")
    mapper()