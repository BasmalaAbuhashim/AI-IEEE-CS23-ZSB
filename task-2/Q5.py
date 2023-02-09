#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 21:14:13 2023

@author: basmala
"""

from Q4 import dictt
z_filter=open("filterd.txt",'w')
for i in dictt.keys():
    z_filter.write("\n{} {}-{}".format(i,dictt[i]['name'],dictt[i]['birthyear']))
z_filter.close()