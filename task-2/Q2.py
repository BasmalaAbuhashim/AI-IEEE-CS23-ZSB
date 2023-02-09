#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 13:46:06 2023

@author: Basmala
"""
n = int(input("enter number of elements: "))
listt = []
for i in range(0,n):
    a=int(input("enter elements of list: "))
    listt.append(a)
cnt = len(list(filter(lambda x: (x%2 == 0) , listt)))

print("Number of even numbers in the list: ", cnt)

