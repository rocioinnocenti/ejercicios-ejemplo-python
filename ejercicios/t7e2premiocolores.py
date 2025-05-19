def premio(color):
    mensaje = ""
    if color == "azul":
        mensaje = "¡El premio ha sido conseguido!"
    else:
        mensaje = "No has conseguido el premio."
    return mensaje

for i in range(5):
    color = input("Ingresa un color: ").lower()

mensaje = premio(color)

print(mensaje)