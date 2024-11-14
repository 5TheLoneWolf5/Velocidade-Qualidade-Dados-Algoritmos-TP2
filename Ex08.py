"""

Esta função inverte os extremos de uma fila e retorna o resultado.

"""

def inverter_fila(fila_pacientes):
    fila_invertida = fila_pacientes
    
    fila_invertida[0], fila_invertida[-1] = fila_invertida[-1], fila_invertida[0]

    return fila_invertida

fila_hospital = ["Paciente Paul", "Paciente Tom", "Paciente Sophie", "Paciente Adam"]

fila_invertida = inverter_fila(fila_hospital)

print(fila_invertida)
