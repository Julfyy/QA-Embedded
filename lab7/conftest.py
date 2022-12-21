#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 23:38:27 2022

@author: bohdan
"""
import subprocess
import paramiko
import pytest

host = '192.168.0.104'
username = 'bohdan'
password = 'bohdan4ik7565'


@pytest.fixture(scope='function')
def server():
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=host,
                       username=username,
                       password=password)
    _stdin, _stdout, _stderr = ssh_client.exec_command("iperf -s -u -t 15")
    print(_stdout.read().decode())
    ssh_client.close()
    return _stderr


@pytest.fixture(scope='function')
def client(server):
    stderr = server
    sp = subprocess.Popen('iperf -c {} -u -i 1'.format(host),
                          shell=True,
                          stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE)
    out, err = sp.communicate()
    return out, err, stderr
