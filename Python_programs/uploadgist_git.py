# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 16:27:51 2023

@author: Administrator
"""

import requests
import json

server = "https://api.github.com"
url = server + "/gists"
user = "dharunjr"


print("checking ", url, "using user:", user)

local_file = "adult.csv"    # change this filename accordingly
with open(local_file) as fh:
    mydata = fh.read()
files = {
    "description": "rest api - giri testing",
    "public": "true",
    "user" : user,
    "files": {
    local_file: {
    "content": mydata
        }
      }
}
r1 = requests.post(url, data=json.dumps(files), auth=(user,'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'))
print(r1.json())