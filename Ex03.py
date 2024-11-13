"""

O primeiro algoritmo implementa com força bruta cada elemento da lista.

O segundo algoritmo pula a parte já comparada da lista, e também pula o elemento em comparação para não fazer uma comparação com si mesmo.
Com poucos passos, o resultado é mais eficiente e adequado para encontrar valores todos os duplicados em uma coleções de dados.

"""


import random

def primeiro_algoritmo(list):
    length = len(list)
    for i in range(length):
        for j in range(length):
            if list[i] == list[j]:
                print(f"Número duplicado encontrado! {list[i]}")

def segundo_algoritmo(list):
    
    length = len(list)

    for i in range(length):
        for j in range(i + 1, length):
            if list[i] == list[j]:
                print(f"Número duplicado encontrado! {list[i]}")

listNumbers = [int(random.random() * 100) for _ in range(50)]

print(listNumbers)

print("### Primeiro Algoritmo ###")
primeiro_algoritmo(listNumbers)
print("### Segundo Algoritmo ###")
segundo_algoritmo(listNumbers)
