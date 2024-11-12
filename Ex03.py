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
        for j in range(i, length):
            if list[i] == list[j]:
                print(f"Número duplicado encontrado! {list[i]}")

listNumbers = [int(random.random() * 100) for _ in range(50)]

print(listNumbers)

print("### Primeiro Algoritmo ###")
primeiro_algoritmo(listNumbers)
print("### Segundo Algoritmo ###")
segundo_algoritmo(listNumbers)
