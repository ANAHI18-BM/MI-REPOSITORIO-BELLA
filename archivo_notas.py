# Creación y escritura en el archivo my_notes.txt
# Abre el archivo en modo escritura ('w') y si no existe, lo crea
with open("my_notes.txt", "w") as archivo:
    # Escribimos tres líneas de notas personales
    archivo.write("Hoy aprendí a manejar archivos de texto en Python.\n")
    archivo.write("Los métodos write() y readline() son muy útiles.\n")
    archivo.write("Debo practicar más para mejorar mis habilidades.\n")

# Lectura del contenido del archivo
# Abre el archivo en modo lectura ('r')
with open("my_notes.txt", "r") as archivo:
    print("Contenido del archivo my_notes.txt:\n")
    
    # Lee cada línea del archivo una por una
    for linea in archivo:
        # Muestra cada línea en la consola
        print(linea.strip())  # strip() elimina los saltos de línea extras

# Nota: Al usar 'with', el archivo se cierra automáticamente al finalizar cada bloque
