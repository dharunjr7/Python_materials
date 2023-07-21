# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 12:07:37 2023

@author: Administrator
"""
#string slicing
#string[start:stop:incremental]

name='python programming'

print(len(name))
print(name[::])
print(name[:18:2])
print(name[-1])
print(name[::-1])
print(name[18:0:-1])

print("Original string:",name)
print(name.upper())
print(name.capitalize())
print(name.lower())
print(name.title())
print("The count of p in name is:",name.count('p'))
print(name.find('on'))
print(name.replace('python','scala'))
print(name.startswith('p'))
print(name.startswith('a'))
print(name.endswith('q'))
print(name.endswith('g'))
print(len(name))
print("")
ex=' Python  '
print(len(ex))
print(ex.lstrip())
print(ex.rstrip())
print("split name:",ex.strip() + "\nlength after split",len(ex.strip()))

string='My name is {}. I love to play {}'
print(string.format('Dharun','football'))
print(string.format(1,2))
print(name.split(' '))
print(string.split('.'))
