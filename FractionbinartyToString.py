# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 17:37:24 2017

@author: danna
"""

def binaryToString(target):
    if target < 0 or target > 1:
        return 'ERROR'
    result = ['0', '.']
    while target > 0:
        r = target * 2.0
        print("r", r)
        if r >= 1:
            result.append('1')
            target = r - 1
        else:
            result.append('0')
            target = r
    print(''.join(result))
    
binaryToString(0.625) # 0.101 (binary)
