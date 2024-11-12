def qtd_livros_id_par(list_id):

    totalOdds = 0

    for i in list_id:
        if i % 2 != 0:
            totalOdds += 1
        
    return totalOdds

livros_id = [43, 44, 45, 46, 47, 48, 49]

resultado = qtd_livros_id_par(livros_id)

print(resultado)
