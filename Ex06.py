"""

Esta função executa a tarefa simples de calcular quantos números ímpares há em uma lista.

"""


def pedidos_impares(list):
        totalOdds = 0
        
        for i in list:
                if i % 2 != 0:
                        totalOdds += 1
                        
        return totalOdds
                                                
        
pilhaPedidos = [7, 8, 90, 33, 20, 35]

totalImpares = pedidos_impares(pilhaPedidos)

print(totalImpares)
