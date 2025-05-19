planetas = ["Mercurio", "Venus", "Tierra", "Marte", "Jupiter", "Saturno", "Urano", "Neptuno"]

def mostrar_planeta(numero):
    if 1 <= numero <= 8:
        planeta = planetas[numero - 1]
        mensaje = "El planeta que has seleccionado es: " + planeta
    else:
        mensaje = "Número inválido, por favor introduce un número entre 1 y 8."
    return mensaje

numero = int(input("Introduce un número entre 1 y 8: "))

respuesta = mostrar_planeta(numero)
print(respuesta)