def respuesta(numero):
    mensaje = ""
    if numero == 4:
        mensaje = "¡Has ganado! El número es correcto."
    else:
        mensaje = "Lo siento, perdiste. El número correcto era el 4."
    return mensaje


def elegir_numero():
    numero = int(input("Elige un número del 1 al 10: "))
    return numero

numero_elegido = elegir_numero()
mensaje = respuesta(numero_elegido)

print(mensaje)