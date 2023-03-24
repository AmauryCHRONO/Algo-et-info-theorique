#!/usr/bin/env python
# coding: utf-8
"""
author : Amaury CHRONOWSKI

"""
# Exo 1

def recursive(n, m = 1):
    print(m)
    if m == n :
        return(0)
    return recursive(n, m+1)

def recursiveInv(n):
    if n == 0 :
        return(0)
    print(n)
    return recursiveInv(n-1)

# recursive(10)
# recursiveInv(10)

# Exo 2
import matplotlib.pyplot as plt
def syracuse(n, list_syra = []):
    list_syra.append(n)
    if n == 1:
        return list_syra, len(list_syra), max(list_syra)
    if n%2 == 0 :
        return syracuse(int(n/2), list_syra)
    else:
        return syracuse(int(3*n+1), list_syra)

def AffichageSyracuse(n = 1):
    vol = []
    for i in range(n):
        list_syra, vol_n, max_n = syracuse(i+1)
        vol.append(vol_n)
    plt.plot(vol, "ro")
    plt.title("Temps de vol de la suite de Syracuse allant jsuqu'à "+str(n))
    plt.show()
            
# AffichageSyracuse(100)
# list_syra, vol, max = syracuse(13)
# plt.plot(list_syra)
# plt.title('Suite de Syracuse commencant à '+str(list_syra[0]))
# plt.show()
    
# Exo 3
def fibonacciDumb(n):
    if n == 1:
        return 1
    if n == 0:
        return 0 
    return fibonacciDumb(n-1) + fibonacciDumb(n-2)
    
def fibonacciSmart(n, f_1 = 1, f_2 = 0, fibo = [0, 1]):
    if n == 1:
        return fibo
    f = f_1+f_2
    fibo.append(f)
    return fibonacciSmart(n-1, f, f_1, fibo)
#print(fibonacciDumb(10))
#print(fibonacciSmart(10))
"""
3/ fibonacciDumb(5) -> fibonacciDumb(4) -> fibonacciDumb(3) -> fibonacciDumb(2) -> fibonacciDumb(1) -> 1
                    |                   |                   |                   -- fibonacciDumb(0) -> 0
                    |                   |                   -- fibonacciDumb(1) -> 1
                    |                   -- fibonacciDumb(2) -> fibonacciDumb(1) -> 1
                    |                                       -- fibonacciDumb(0) -> 0                                         
                    -- fibonacciDumb(3) -> fibonacciDumb(2) -> fibonacciDumb(1) -> 1
                                        |                   -- fibonacciDumb(0) -> 0 
                                        -- fibonacciDumb(1) -> 1
"""

# Exo 4
from math import floor
def diviserPourReigner(list_try):
    if len(list_try) == 1:
        return list_try[0]
    temp_1 = diviserPourReigner(list_try[:floor(len(list_try)/2)])
    temp_2 = diviserPourReigner(list_try[floor(len(list_try)/2):])
    if  temp_1 >= temp_2:
        return temp_1
    return temp_2

# print(diviserPourReigner([1,0,2,4,1,6,8,14,95,1,-1]))

# Exo 5

def hanoi(n,a=1,b=2,c=3):
    if (n > 0):
        hanoi(n-1,a,c,b)
        print("Déplace un disque du pilier",a,"le pilier",c)
        hanoi(n-1,b,a,c)

# hanoi(7)

# Exo 6
"""
1. a) 1
   b) n
   c) n/2
"""
import math
def dichotomie(k, liste_tri, ind = 0):

    if len(liste_tri) == 0:
        return -1
    
    if k == liste_tri[math.floor(len(liste_tri)/2)]:
        return math.floor(len(liste_tri)/2)+ind
    
    if k < liste_tri[math.floor(len(liste_tri)/2)]:
        return dichotomie(k,liste_tri[:math.floor(len(liste_tri)/2)], ind)
    
    if k > liste_tri[math.floor(len(liste_tri)/2)]:
        return dichotomie(k,liste_tri[math.floor(len(liste_tri)/2)+1:], ind+len(liste_tri[:math.floor(len(liste_tri)/2)+1]))
    
    
test = [1,3,7,8,9,11,15,16]
# print(dichotomie(7, test))