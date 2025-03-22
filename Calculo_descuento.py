def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento aplicado a una compra y devuelve el monto del descuento.
    :param monto_total: Monto total de la compra.
    :param porcentaje_descuento: Porcentaje de descuento a aplicar (por defecto 10%).
    :return: Monto del descuento calculado.
    """
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento

# Llamadas a la función
monto1 = 200  # Ejemplo de monto total de compra
monto2 = 500  # Otro ejemplo de monto total de compra
porcentaje_personalizado = 15  # Porcentaje personalizado

descuento1 = calcular_descuento(monto1)
descuento2 = calcular_descuento(monto2, porcentaje_personalizado)

# Cálculo del monto final a pagar
total_pagar1 = monto1 - descuento1
total_pagar2 = monto2 - descuento2

# Mostrar los resultados
print(f"Monto total: ${monto1}, Descuento aplicado: ${descuento1}, Total a pagar: ${total_pagar1}")
print(f"Monto total: ${monto2}, Descuento aplicado ({porcentaje_personalizado}%): ${descuento2}, Total a pagar: ${total_pagar2}")
