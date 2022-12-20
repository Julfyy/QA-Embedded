#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 16:10:23 2022

@author: bohdan
"""
import subprocess

server_ip = "192.168.0.102"

def client(server_ip):
    iperf_conn = subprocess.Popen(["iperf3", "-c", server_ip],
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE)
    res = iperf_conn.communicate()
    
    return res

def parser(res):
    if len(res[1]) == 0:
        print(res[0].decode('utf-8'), end="")
    else:
        print(res[1].decode('utf-8'), end='')
    
    
res = client(server_ip)

parser(res)
