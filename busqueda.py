def buscar_elemento(matriz, objetivo):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == objetivo:
                return f"El número {objetivo} se encontró en la posición ({i}, {j})"
    return f"El número {objetivo} no está en la matriz."

matriz = [
    [5, 8, 3],
    [2, 9, 6],
    [1, 4, 7]
]
numero = int(input("Ingresa un número para buscar en la matriz: "))

resultado = buscar_elemento(matriz, numero)

print(resultado)