#!/usr/bin/env python3
# coding: utf-8

#initial convertion form 2 > 3
#discrepencies done:
#    print function differnce 
#
#future fixes:
#    when socket use convert strings to bytes 
#    ???
#    ???

import sys

py2 = sys.argv[1]
py3 = 'v3_'+py2

with open(py2,'r') as f2, open(py3,'w') as f3:
    for line in f2.readlines():
        if "print" in line:
            line = line.rstrip()
            point = line.index('print')+4
            new_line = line[point:]+'('+line[:point+1]+')\n'
            f3.write(new_line)
        else:
            f3.write(line)
        
        

