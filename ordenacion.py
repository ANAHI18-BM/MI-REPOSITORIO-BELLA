# Crear una matriz 3x3 con valores numéricos
matriz = [
    [9, 7, 5],
    [6, 3, 8],
    [1, 2, 4]
]

# Función para ordenar una fila específica de la matriz
def ordenar_fila(matriz, fila):
    matriz[fila].sort()  # Ordena la fila en orden ascendente

# Definir la fila a ordenar (por ejemplo, la fila 1)
fila_a_ordenar = 1

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Ordenar la fila seleccionada
ordenar_fila(matriz, fila_a_ordenar)

# Mostrar la matriz con la fila ordenada
print(f"\nMatriz con la fila {fila_a_ordenar} ordenada:")
for fila in matriz:
    print(fila)
