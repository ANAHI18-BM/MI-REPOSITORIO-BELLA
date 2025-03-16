def calcular_promedio_temperaturas(temperaturas):
    """
    Calcula la temperatura promedio de cada ciudad por semana y el promedio general de cada ciudad.
    
    :param temperaturas: Diccionario con nombres de ciudades como claves y una lista de listas de temperaturas (semanas) como valores.
    :return: Diccionario con los promedios semanales y el promedio general de cada ciudad.
    """
    promedios_ciudades = {}

    for ciudad, semanas in temperaturas.items():
        promedios_semanales = [sum(semana) / len(semana) for semana in semanas]
        promedio_total = sum(promedios_semanales) / len(promedios_semanales)

        promedios_ciudades[ciudad] = {
            "promedios_semanales": promedios_semanales,
            "promedio_total": round(promedio_total, 2)
        }

    return promedios_ciudades


# Datos de temperaturas (Ciudades, Semanas, Días)
temperaturas = {
    "Quito": [
        [78, 80, 82, 79, 85, 88, 92],
        [76, 79, 83, 81, 87, 89, 93],
        [77, 81, 85, 82, 88, 91, 95],
        [75, 78, 80, 79, 84, 87, 91]
    ],
    "Guayaquil": [
        [62, 64, 68, 70, 73, 75, 79],
        [63, 66, 70, 72, 75, 77, 81],
        [61, 65, 68, 70, 72, 76, 80],
        [64, 67, 69, 71, 74, 77, 80]
    ],
    "Cuenca": [
        [90, 92, 94, 91, 88, 85, 82],
        [89, 91, 93, 90, 87, 84, 81],
        [91, 93, 95, 92, 89, 86, 83],
        [88, 90, 92, 89, 86, 83, 80]
    ]
}

# Llamamos a la función y mostramos los resultados
resultados = calcular_promedio_temperaturas(temperaturas)

for ciudad, datos in resultados.items():
    print(f"\nCiudad: {ciudad}")
    for semana_idx, promedio in enumerate(datos["promedios_semanales"]):
        print(f"  Semana {semana_idx + 1}: {promedio:.2f} grados")
    print(f"  Promedio total en {ciudad}: {datos['promedio_total']} grados")

