#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 16:37:35 2023

@author: basmala
"""
dictt={}
#lst=[]
old_id = 1
z_id = 1
with open("grades.txt",'r') as f:
    f.readline()
    for i in f:
        i=i.replace(":"," ")
        i=i.replace("-"," ")
        id_ = int(i.split()[0])
        name = i.split()[1]
        grade = i.split()[2]
        birthyear = int(i.split()[3])
        gender = i.split()[4]
        if grade == 'N/A':
            continue
        dictt[id_] =  {'name' : name,'grade' : grade,
                                  'gender' : gender,'birthyear' : birthyear}
        #b
        if(dictt[id_]['birthyear'] < dictt[old_id]['birthyear']):
            old_id=id_
        if(dictt[id_]['grade'] < dictt[z_id]['grade']):
            z_id=id_
#a
print(dictt)

      
#c
avg = 0
val = dictt.values()
for k in val:
    avg += int(k['grade'])
avg= avg/len(val)
print("the oldest user is {}".format(old_id))
print("the average score is {}".format(avg))
print("the gender of user with highest score {}".format(dictt[z_id]['gender']))
