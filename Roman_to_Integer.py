# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 08:10:22 2021

@author: KaiJax
"""

# Roman to Integer

'''
Symbol      Value
I           1
V           5
X           10
L           50
С           100
D           500
M           1000

Exemple:
Input: s = "IV"
Output: 4


Ex2:

Input: s = "IX"
Output: 9    

'''


class Solution:
    def romanToInt(self, s: str) -> int:
        s = s.replace("IV", " IV ")
        s = s.replace("IX", " IX ")
        s = s.replace("XL", " XL ")
        s = s.replace("XC", " XC ")
        s = s.replace("CD", " CD ")
        s = s.replace("CM", " CM ")
        
        e = s.split()
        
        dct = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        
        v = []
        for i in range(len(e)):
            f = e[i]
            f = list(f)
            f = [dct[x] for x in f]
            if len(f) == 2 and f[0] != f[1] and f[0] < f[1]:
                r = f[1]-f[0]
            else:
                r = sum(f)
            v.append(r)
        res = sum(v)
        
        return res
        
# Вариант 2

def romanToInt(self, n: str) -> int:
    d={"I":1, "V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    nl=[]
    for i in n:
        if i in d:
            nl.append(d[i])
    res=nl[len(nl)-1]
    for i in range(len(nl)-1,0,-1):
        if nl[i] > nl[i-1]:
            res=res-nl[i-1]
        else:
            res=res+nl[i-1]
    return(res)
     
        
        

