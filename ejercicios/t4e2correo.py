#Pedido de datos
correo = input("Por favor, introduce tu correo electrónico: ")

#Operaciones
longitud = len(correo)
correo_mayusc = correo.upper()
correo_minusc = correo.lower()

#Imprimir
print("Tu correo electrónico: ", correo)
print("Longitud: ", longitud, "caracteres")
print("En mayúsculas: ", correo_mayusc)
print("En minúsculas: ", correo_minusc)
