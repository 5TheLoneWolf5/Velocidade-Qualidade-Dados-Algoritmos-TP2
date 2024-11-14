# Em cada iteração exterior do loop presente na função ordenar_avaliacoes, há uma condição para encontrar o menor número e o colocar na primeira posição não ordenada (desde que a condição seja verdadeira).

def ordenar_avaliacoes(list):
    size = len(list)

    for i in range(size - 1):
        smallest_idx = i

        for j in range(i + 1, size):
            if list[j] < list[smallest_idx]:
                smallest_idx = j

        list[i], list[smallest_idx] = list[smallest_idx], list[i]


pilhaAvaliacoes = [10, 7.4, 9.5, 8.2, 7.8, 6, 4.5, 2.5]

ordenar_avaliacoes(pilhaAvaliacoes)

print(pilhaAvaliacoes)
