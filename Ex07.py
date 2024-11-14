"""

Esta função executa a tarefa simples de calcular quantos números pares há em uma lista.

"""


def pedidos_pares(list):
        totalEvens = 0
        
        for i in list:
                if i % 2 == 0:
                        totalEvens += 1
                        
        return totalEvens
                                                
        
pilhaPedidos = [7, 8, 90, 33, 20, 35]

totalImpares = pedidos_pares(pilhaPedidos)

print(totalImpares)
