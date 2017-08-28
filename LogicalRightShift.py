# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 18:34:59 2017

@author: danna
"""

def logical_rightShift(target, n):
    return (target % 0x100000000) >> n

print(logical_rightShift(-1000, 3))