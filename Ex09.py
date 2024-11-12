def ordenar_inteiros(list):
    n = len(list)
    
    for i in range(n):
        check = False
        for j in range(0, n-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                check = True

        if (check == False):
            break


inteiros = [4, 2, 40, 100, 98, 79, 23, 10, 35, 24]

ordenar_inteiros(inteiros)

print(inteiros)
