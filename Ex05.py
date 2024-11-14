"""

Obtendo o item do topo de uma pilha, sem removê-lo.

"""


def tarefa_no_topo(pilha_de_tarefas):
    return pilha_de_tarefas[-1]

pilhaTarefas = ["Tarefa 1", "Tarefa 2", "Tarefa 3"]

topoPilha = tarefa_no_topo(pilhaTarefas)

print(topoPilha)
