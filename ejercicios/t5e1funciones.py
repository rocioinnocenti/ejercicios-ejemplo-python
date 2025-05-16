#Pedir detalles del producto
producto = input("¿El costo de qué producto deseas calcular? ")
precio = float(input("¿Cuánto cuesta cada unidad? "))
cantidad = int(input("¿Cuántos quieres comprar? "))
descuento = float(input("¿Cuál es el porcentaje de descuento? "))
iva = float(input("¿Cuál es el porcentaje de recargo por IVA? "))

#Total
def calcular_total(precio, cantidad):
    total = precio * cantidad
    return total

#Descuento
def aplicar_descuento(descuento, total):
    total_descuento = total * (descuento / 100)
    return total_descuento

# IVA
def aplicar_iva(iva, total):
    total_iva = total * (iva / 100)
    return total_iva

# Precio final
def calcular_precio_final(total, total_descuento, total_iva):
    precio_final = total - total_descuento + total_iva
    return precio_final 

total = calcular_total(precio, cantidad)
total_descuento = aplicar_descuento(descuento, total) 
total_iva = aplicar_iva(iva, total)

precio_final = total - total_descuento + total_iva

print("Precio final: ", precio_final, "euros.")
