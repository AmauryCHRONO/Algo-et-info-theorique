#!/usr/bin/env python
# coding: utf-8
"""
author : Amaury CHRONOWSKI

"""
# Exo 1
"""
1)
         |->70
     |->65
 |->60
 |   |           |->55 
 |   |       |->50
 |   |   |->45
 |   |   |   |->40
 |   |->35
 |       |->30
25
 |   |->20
 |   |   |->15
 |->10
     |->5 
2)
         |->70
     |->65
 |->60
 |   |       |->55 
 |   |   |->50
 |   |->45
 |       |->40
 |           |->30
25
 |   |->20
 |   |   |->15
 |->10
     |->5

         |->70
     |->65
->60
   |               |->55 
   |           |->50
   |       |->45
   |       |   |->40
   |       |       |->30
   |   |->20
   |   |   |->15
   |->10
       |->5

     
3)
     |->70
 |->65
60
 |           |->55 
 |       |->50
 |   |->45
 |   |   |->40
 |->35
     |       |->30
     |   |->20
     |   |   |->15
     |->10
         |->5    

"""

# Exo 2
"""
1)
   |->4
|->*
|  |->4
*
   |->-8
|->/
   |  |->z
   |->+
      |->5

2)5+z/-8*4*4
oui mais il manque les parentheses. il faudrait les ajouter a chque fois que l'ont quitte un niveau.

3) Ordre postfit

4)rcursif
"""

def NPI(liste):
    op=("+", "-", "/", "*")
    temp=[]
    for i in liste:
        if i in op:
            if i=="+":
                temp.append(temp.pop()+temp.pop())
            if i=="-":
                temp.append(-temp.pop()+temp.pop())
            if i=="*":
                temp.append(temp.pop()*temp.pop())
            if i=="/":
                temp.append((1/temp.pop())*temp.pop())
        elif i == "#":
            temp.append(-temp.pop())
        else:
            print(i)
            temp.append(i)
    return temp.pop()
test=[1, 2, "+", 4, 5, "/", "-", 6, "#", "*"]
print(NPI(test))

# Exo 3

def arbre(liste):



    a?b?c:d:e?f:g


    