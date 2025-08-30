# Programa 1: Búsqueda en una matriz bidimensional

# Definimos una matriz 3x3
matriz = [
    [4, 8, 12],
    [3, 7, 9],
    [10, 5, 1]
]

# Función de búsqueda
def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return f"Valor {valor} encontrado en posición ({i}, {j})"
    return f"Valor {valor} NO encontrado en la matriz"

# Ejemplo: buscar el número 7
valor_buscado = 7
print("Matriz:")
for fila in matriz:
    print(fila)

print(buscar_valor(matriz, valor_buscado))
