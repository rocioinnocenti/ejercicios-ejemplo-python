#Pedir frase
frase = input("Introduce una frase: ")

#Resultados
longitud = len(frase)
frase_mayusculas = frase.upper()
frase_minusculas = frase.lower()

#Imprimir
print("Tu frase: ", frase)
print("Longitud de la frase: ", longitud, "caracteres")
print("Frase en mayúsculas: ", frase_mayusculas)
print("Frase en minúsculas: ", frase_minusculas)