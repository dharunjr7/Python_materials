# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 20:57:47 2023

@author: Administrator
"""

import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='192.168.163.133',username='user',password='password')
stdin,stdout,stderr = ssh.exec_command('hostname -I')

print(stdout.read().decode())

for line in stdout.read().splitlines():
    print(line.decode("UTF-8"))
ssh.close()

import os
print(os.listdir())