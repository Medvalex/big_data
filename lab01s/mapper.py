#!/usr/bin/python

#* Lab01 code by A. Medvedev

import sys

for line in sys.stdin:
    columns = line.split(',')
    print(columns[2] + '\t' + columns[4].replace("\n",""))