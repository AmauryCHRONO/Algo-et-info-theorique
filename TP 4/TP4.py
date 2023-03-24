# Exo 1

def tri_selection(liste_nontri):

   for i in range(len(liste_nontri)):
       indmin = i

       for j in range(i+1, len(tab)):
           if liste_nontri[indmin] > liste_nontri[j]:
               indmin = j
                
       tmp = liste_nontri[i]
       liste_nontri[i] = liste_nontri[indmin]
       liste_nontri[indmin] = tmp

   return liste_nontri

tab = [3, 5, 4, 1, 8, 7, 2, 1]
print(tri_selection(tab))

# Exo 2
"""
1.O(n)+O(?)

2.
""" 

def triFusion(L):
    if len(L) == 1:
        return L
    else:
        return fusion( triFusion(L[:len(L)//2]) , triFusion(L[len(L)//2:]) )
    
def fusion(A,B):
    if len(A) == 0:
        return B
    elif len(B) == 0:
        return A
    elif A[0] <= B[0]:
        return [A[0]] + fusion( A[1:] , B )
    else:
        return [B[0]] + fusion( A , B[1:] )

# Exo 3

def quick_sort(arr):

    if len(arr) < 2:
        return arr

    pivot_index = len(arr) - 1
    pivot = arr[pivot_index]

    lesser = [item for item in arr[:pivot_index] if item <= pivot]
    greater = [item for item in arr[:pivot_index] if item > pivot]

    return quick_sort(lesser) + [pivot] + quick_sort(greater)


# Exo 4
import numpy
def tabAlea(n, k):
    tab = []
    for i in range(k):
        tab.append(numpy.randint(1,n))
    return tab

# Exo 5
