#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 23:34:53 2022

@author: bohdan
"""

def parser(arg):

    arg = str(arg)
    text = arg.split('[  3]')
    mass = []
    for i in range(2,len(text) - 1  ):
        temp = text[i].split(' ')
        mass.append([temp[2] + temp[3],
                     float(temp[-5])*(1000 if temp[-4] == 'MBytes' else 1),
                     temp[-2]])
    print("====================================================")
    for j in range(len(mass)):
        if float(mass[j][1]) > 200 and float(mass[j][1] ) > 1:
            print('Interval: ', mass[j][0],
                  '\tTransfer: ', mass[j][1], " Kbytes", 
                  '\tBitrate: ', mass[j][2],  " Mbits/sec")

    return mass