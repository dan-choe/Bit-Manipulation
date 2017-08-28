# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 16:36:16 2017

@author: danna
"""

def makeMast(i, j):
    if i>j:
        return 0
    big = (2 ** j) | ((2**j) -1)
    sm = ((2**i) -1)
    return big ^ sm

def bitInsertion(N,M,i,j):
    mask = makeMast(i, j)
    if mask:
        M = mask & (M << i)
        return M | N
    return -1

result = bitInsertion(1024, 19, 2, 6)
print("result {0:b}".format(result))