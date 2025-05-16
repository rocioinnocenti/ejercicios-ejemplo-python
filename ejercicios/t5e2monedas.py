cantidad_euros = float(input("Introduce la cantidad de Euros: "))
conversion_dolar = 1.1
conversion_libra = 0.87

def convertir_a_dolar(cantidad_euros,conversion_dolar):
    dolares = cantidad_euros * conversion_dolar
    return dolares

def convertir_a_libra(cantidad_euros,conversion_libra):
    libras = cantidad_euros * conversion_libra
    return libras

dolares = convertir_a_dolar(cantidad_euros,conversion_dolar)
libras = convertir_a_libra(cantidad_euros,conversion_libra)

print("Cantidad de Euros: ", cantidad_euros)
print("Equivalente en dólares: ", dolares)
print("Equivalente en libras: ", libras)