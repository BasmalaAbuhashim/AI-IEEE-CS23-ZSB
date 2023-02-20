#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 20:18:30 2023

@author: basmala
"""
from math import sqrt  

def Q1(lst):
    lst.sort()
    f_half = median(lst[:len(lst)//2])
    return f_half
    
def Q3(lst): 
    lst.sort()
    sec_half = median(lst[len(lst)//2 + 1:])
    return sec_half
    
def median(lst):
    lst.sort()
    if (len(lst) % 2 == 0):
        fst_med = lst[len(lst)//2]
        sec_med = lst[len(lst)//2-1]
        
        the_med = (fst_med + sec_med)/2
    else:
        the_med = lst[len(lst)//2]
    return the_med
    
def variance_std(lstt):
    mean = sum(lst) / len(lst)
    return sum([(x - mean)**2 for x in lstt]) /len(lstt)
        
if __name__ == "__main__":
    lst= []
    while True:
        try:
            lst = list(map(int,input().split()))
            lstt = lst
            IQR = Q3(lst) - Q1(lst)
            variance  = variance_std(lstt)
            std = sqrt(variance)
            print("Min: ",min(lst))
            
            '''if(len(lst) == 2):
                print("Q1: ",lst[0])
                print("Q2: ",(lst[0]+lst[1])/2)
                print("Q3: ",lst[1])
            else:
                print("Q1: ",Q1(lst))
                print("Q2: ",median(lst))
                print("Q3: ",Q3(lst))
            i tried to handle a case where the size of list = 2 
            but it's giving error.
                '''
                
            print("Q1: ",Q1(lst))
            print("Q2: ",median(lst))
            print("Q3: ",Q3(lst))
            print("Max: ",max(lst))
            print("range: ",max(lst) - min(lst))
            print("iqr: ",IQR)
            print("variance: %0.3f"%variance)
            print("standard deviation: %0.3f"%std)
            break
        except ValueError:
            print("please enter an integer number: ")
        except (ZeroDivisionError, IndexError, ValueError):
             print("Error:'the list is empty'")
        
