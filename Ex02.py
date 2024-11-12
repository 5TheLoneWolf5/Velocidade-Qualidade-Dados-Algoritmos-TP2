"""

A complexidade de tempo desse algoritmo de ordenação (Quicksort) de é O(n log n) no melhor caso, e O(n^2) no pior caso.

"""

import random

def partition(collec, low, high):
   pivot = collec[high]
   i = low - 1

   for j in range(low, high):
       if collec[j] <= pivot:
           i += 1
           collec[i], collec[j] = collec[j], collec[i]
   collec[i+1], collec[high] = collec[high], collec[i+1]
   return i+1

def quick_sort(collec, low=0, high=None):
   if high is None:
       high = len(collec) - 1

   if low < high:
       pivot_idx = partition(collec, low, high)
       quick_sort(collec, low, pivot_idx-1)
       quick_sort(collec, pivot_idx+1, high)


data = [int(random.random() * 30) for _ in range(15)]
print("Dados pré-ordenação:")
print(data)
print("Dados pós-ordenação:")
quick_sort(data)
print(data)
