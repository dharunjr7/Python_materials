# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 15:37:50 2023

@author: Administrator
"""
import requests
import json

user = 'dharunjr7'
password = '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'


#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
server = 'https://api.github.com/'
data = requests.get(server,auth=(user,password))
op = data.status_code
print("status code:",op)

if op == 200:
    jdata = json.loads(data.text)
    for key,value in jdata.items():
        print(key,':',value)
