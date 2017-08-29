# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 17:22:24 2017

@author: danna
"""

def numOf1sDifference_1(a, b):
    c = a ^ b
    count = 0
    while c:
        c = c & (c-1)
        count += 1
    return count

def numOf1sDifference_2(a, b):
    c = a ^ b
    count = 0
    while c:
        count += c & 1
        c = (c >> 1)
    return count

print(numOf1sDifference_1(56, 15)) # 5
print(numOf1sDifference_2(56, 15)) # 5