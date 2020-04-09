#!/usr/bin/python

'''
    first lab in this course
'''
import sys

for line in sys.stdin:
    columns = line.split(',')
    print(columns[2] + '\t' + columns[4].replace("\n",""))