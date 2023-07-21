# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 13:04:48 2023

@author: Administrator
"""

a=10
b=5
if a>b:
    print("a is greater than b")
else:
    print("b is greater")
    
name='python'
if name.isupper():
    print("name is in upper case")
else:
    print("name is in lower case")
    
if name.startswith('p'):
    print("true")
    
#lang=input("Enter the language:")
lang='python'
if lang=='python':
    print("Entered language is {}".format(lang))
elif lang=='java':
    print("Entered language is {}".format(lang))
else:
    print("Entered language is {}".format(lang))
    
#range(start,stop,increment/step)
for val in range(1,10):
    print(val)

for char in lang:
    print("Char is {}".format(char))