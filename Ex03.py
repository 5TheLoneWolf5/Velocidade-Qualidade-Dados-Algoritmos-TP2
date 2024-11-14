"""

O primeiro algoritmo faz uma comparação de força bruta em cada elemento na lista.

O segundo algoritmo pula a parte já comparada da lista, e também pula o elemento em comparação para não fazer uma comparação com si mesmo.
Com poucos passos, o resultado é mais eficiente e adequado para encontrar todos os valores duplicados em uma coleções de dados.
O algoritmo também conta com um break dentro da condição, para garantir que o número de ocorrências seja coerente, sem repetir mais do que necessário.
(A quantidade total de números repetidos de um valor sempre será o total saídas de ocorrências desse valor + 1 (no console, nesse caso, mas poderia ser de outro modo).

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
                print(f"Número duplicado encontrado! Valor: {list[i]} | Index inicial: {i} | Index do valor duplicado: {j}")
                break

listNumbers = [int(random.random() * 100) for _ in range(50)]

print(listNumbers)

print("### Primeiro Algoritmo ###")
primeiro_algoritmo(listNumbers)
print("### Segundo Algoritmo ###")
segundo_algoritmo(listNumbers)

"""

Exemplo:

[28, 44, 34, 35, 80, 46, 98, 31, 12, 88, 82, 59, 13, 93, 11, 10, 8, 19, 78, 97, 11, 16, 40, 98, 46, 57, 29, 86, 80, 88, 2, 31, 36, 55, 82, 82, 13, 82, 20, 3, 10, 38, 84, 7, 94, 75, 32, 14, 40, 26]
### Primeiro Algoritmo ###
Número duplicado encontrado! 28
Número duplicado encontrado! 44
Número duplicado encontrado! 34
Número duplicado encontrado! 35
Número duplicado encontrado! 80
Número duplicado encontrado! 80
Número duplicado encontrado! 46
Número duplicado encontrado! 46
Número duplicado encontrado! 98
Número duplicado encontrado! 98
Número duplicado encontrado! 31
Número duplicado encontrado! 31
Número duplicado encontrado! 12
Número duplicado encontrado! 88
Número duplicado encontrado! 88
Número duplicado encontrado! 82
Número duplicado encontrado! 82
Número duplicado encontrado! 82
Número duplicado encontrado! 82
Número duplicado encontrado! 59
Número duplicado encontrado! 13
Número duplicado encontrado! 13
Número duplicado encontrado! 93
Número duplicado encontrado! 11
Número duplicado encontrado! 11
Número duplicado encontrado! 10
Número duplicado encontrado! 10
Número duplicado encontrado! 8
Número duplicado encontrado! 19
Número duplicado encontrado! 78
Número duplicado encontrado! 97
Número duplicado encontrado! 11
Número duplicado encontrado! 11
Número duplicado encontrado! 16
Número duplicado encontrado! 40
Número duplicado encontrado! 40
Número duplicado encontrado! 98
Número duplicado encontrado! 98
Número duplicado encontrado! 46
Número duplicado encontrado! 46
Número duplicado encontrado! 57
Número duplicado encontrado! 29
Número duplicado encontrado! 86
Número duplicado encontrado! 80
Número duplicado encontrado! 80
Número duplicado encontrado! 88
Número duplicado encontrado! 88
Número duplicado encontrado! 2
Número duplicado encontrado! 31
Número duplicado encontrado! 31
Número duplicado encontrado! 36
Número duplicado encontrado! 55
Número duplicado encontrado! 82
Número duplicado encontrado! 82
Número duplicado encontrado! 82
Número duplicado encontrado! 82
Número duplicado encontrado! 82
Número duplicado encontrado! 82
Número duplicado encontrado! 82
Número duplicado encontrado! 82
Número duplicado encontrado! 13
Número duplicado encontrado! 13
Número duplicado encontrado! 82
Número duplicado encontrado! 82
Número duplicado encontrado! 82
Número duplicado encontrado! 82
Número duplicado encontrado! 20
Número duplicado encontrado! 3
Número duplicado encontrado! 10
Número duplicado encontrado! 10
Número duplicado encontrado! 38
Número duplicado encontrado! 84
Número duplicado encontrado! 7
Número duplicado encontrado! 94
Número duplicado encontrado! 75
Número duplicado encontrado! 32
Número duplicado encontrado! 14
Número duplicado encontrado! 40
Número duplicado encontrado! 40
Número duplicado encontrado! 26
### Segundo Algoritmo ###
Número duplicado encontrado! Valor: 80 | Index inicial: 4 | Index do valor duplicado: 28
Número duplicado encontrado! Valor: 46 | Index inicial: 5 | Index do valor duplicado: 24
Número duplicado encontrado! Valor: 98 | Index inicial: 6 | Index do valor duplicado: 23
Número duplicado encontrado! Valor: 31 | Index inicial: 7 | Index do valor duplicado: 31
Número duplicado encontrado! Valor: 88 | Index inicial: 9 | Index do valor duplicado: 29
Número duplicado encontrado! Valor: 82 | Index inicial: 10 | Index do valor duplicado: 34
Número duplicado encontrado! Valor: 13 | Index inicial: 12 | Index do valor duplicado: 36
Número duplicado encontrado! Valor: 11 | Index inicial: 14 | Index do valor duplicado: 20
Número duplicado encontrado! Valor: 10 | Index inicial: 15 | Index do valor duplicado: 40
Número duplicado encontrado! Valor: 40 | Index inicial: 22 | Index do valor duplicado: 48
Número duplicado encontrado! Valor: 82 | Index inicial: 34 | Index do valor duplicado: 35
Número duplicado encontrado! Valor: 82 | Index inicial: 35 | Index do valor duplicado: 37

"""
