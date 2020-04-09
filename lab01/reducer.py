#!/usr/bin/python

import sys

prev_key = None
sub_total = 0 

for line in sys.stdin:
    
    key,value = line.split('\t')
    if key != prev_key and prev_key is not None:
        print(prev_key + '\t' +str(round(sub_total,2)))
        sub_total = 0
    sub_total += float(value)
    prev_key = key
if prev_key is not None:
    print(prev_key + '\t' +str(round(sub_total,2)))     
