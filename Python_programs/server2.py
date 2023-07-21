# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 20:57:30 2023

@author: Administrator
"""

import paramiko
import os
#from genericpath import isfile

host = '192.168.163.134'
user= 'user'
passw = 'password'

localpath = '/home/user/Desktop/localfiles/'
rempath = '/home/user/Desktop/localfiles/'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname = host,password = passw,username = user)
sftp = ssh.open_sftp()
for file in os.listdir(localpath):
    #print(file)
    #if isfile(file):
    local_file = localpath + file
    rem_file = rempath + file
    sftp.put(local_file,rem_file)
    print("Local file {} is moved from local:{} to remote:{}".format(file,localpath,rempath))
sftp.close()
ssh.close()
        