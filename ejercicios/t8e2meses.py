meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

def mostrar_mes(numero):
    if 1 <= numero <= 12:
        mes = meses[numero - 1]
        mensaje = "El mes que has seleccionado es: " + mes
        if numero == 6:
            mensaje = "El mes que has seleccionado es EL MEJOR MES: " + mes
    else:
        mensaje = "Número inválido. Por favor, ingresa un número entre 1 y 12. "
    return mensaje

numero = int(input("Elige un número entre 1 y 12: "))

respuesta = mostrar_mes(numero)
print(respuesta)