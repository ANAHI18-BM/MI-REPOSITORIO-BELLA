# Crear un diccionario con información personal ficticia
informacion_personal = {
    "nombre": "Juan Pérez",
    "edad": 30,
    "ciudad": "Quito",
    "profesion": "Ingeniero"
}

# Acceder y modificar el valor de la clave 'ciudad'
informacion_personal["ciudad"] = "Guayaquil"  # Cambiamos la ciudad a Guayaquil

# Agregar una nueva clave-valor para la profesión de la persona
informacion_personal["profesion"] = "Desarrollador de Software"  # Modificamos la profesión

# Verificar si la clave 'telefono' existe en el diccionario
if "telefono" not in informacion_personal:  # Si no existe la clave 'telefono'
    informacion_personal["telefono"] = "0987654321"  # Agregamos un número de teléfono ficticio

# Eliminar la clave 'edad' del diccionario
del informacion_personal["edad"]  # Eliminamos la información de la edad

# Imprimir el diccionario resultante
print(informacion_personal)
