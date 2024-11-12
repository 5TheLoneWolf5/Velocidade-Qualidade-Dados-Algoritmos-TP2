import random

def primeiro_algoritmo(list):
    length = len(list)
    for i in range(length):
        for j in range(length):
            if list[i] == list[j]:
                print(f"Número duplicado encontrado! {list[i]}")

def segundo_algoritmo(list):
    
    length = len(list)
    listForSearch = []

    def binary_search(array, value):
        first = 0
        last = len(array) - 1

        for item in range(0, len(array)):
            middlePoint = (first + last) // 2

            if (value == array[middlePoint]):
                print(f"Número duplicado encontrado! {array[item]}")
            else:
                if (value > array[middlePoint]):
                    first = middlePoint + 1
                else:
                    last = middlePoint - 1

        return -1

    for i in range(length):
        binary_search(list, list[i])

listNumbers = [int(random.random() * 100) for _ in range(50)]

print(listNumbers)

print("### Primeiro Algoritmo ###")
primeiro_algoritmo(listNumbers)
print("### Segundo Algoritmo ###")
segundo_algoritmo(listNumbers)
