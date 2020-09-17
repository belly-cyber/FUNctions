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

with open(py2) as f2, open(py3) as f3:
    for line in f2.readlines():
        if "print" in line:
            start_point = line.index('print')+5
            new_line = line[start_point:]+'(' +line[:start_point+1]+')'
            f3.write(new_line)
        else:
            f3.write(line)
        
        

