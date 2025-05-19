def destino(color):
    mensaje = ""
    if color == "rojo":
        mensaje = "El rojo es el color de la pasión y la energía. ¡Hoy será un día lleno de acción y emoción! No temas a los desafíos, saldrás victorioso."
    elif color == "verde":
        mensaje = "El verde representa la esperanza y el crecimiento. Algo nuevo y positivo está por florecer en tu vida. Confía en los pequeños cambios que te acercan a tus metas."
    elif color == "azul":
        mensaje = "El azul simboliza la calma y la serenidad. Hoy estarás rodeado de tranquilidad y equilibrio. Aprovecha este momento para reflexionar y renovar tu energía."    
    elif color == "amarillo":
        mensaje = "El amarillo es el color de la felicidad y el optimismo. ¡Prepárate para un día lleno de alegría y buenas noticias! Alguien cercano te sorprenderá de forma positiva."
    elif color == "morado":
        mensaje = "El morado evoca la sabiduría y la creatividad. Hoy te sentirás inspirado y lleno de ideas. Es el momento ideal para dejar volar tu imaginación y tomar decisiones importantes."
    else:
        mensaje = "Color inválido. Por favor, elegir entre rojo, verde, azul, amarillo o morado."
    return mensaje

def elegir_color():
    color = input("Elige un color para saber tu destino: rojo, verde, azul, amarillo o morado. ¿Cuál escoges?: ")
    return color.lower()

color_elegido = elegir_color()
mensaje = destino(color_elegido)

print(mensaje)