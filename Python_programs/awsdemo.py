# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 17:38:27 2023

@author: Administrator
"""

import boto3
aws_con=boto3.session.Session(profile_name="user24")
iam_con=aws_con.resource('iam')

for each_user in iam_con.users.all():
    print(each_user.name)
    
    
for each_user in iam_con.groups.all():
    print(each_user.name)