cantidad_de_notas = int(input("¿Cuántas notas quieres ingresar para calcular tu nota media? "))
suma = 0

for i in range(cantidad_de_notas):
    nota = float(input("Completa tu nota: "))
    suma += nota

def calcular_media(suma, cantidad_de_notas):
    nota_media = suma / cantidad_de_notas
    return nota_media

nota_media = calcular_media(suma, cantidad_de_notas)
mensaje = nota_media
print("Tu nota media es: ", nota_media)