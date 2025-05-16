#Precios
camisetas = 10 
sudaderas = 20.5 
gorras = 5.5 
recargo_IVA = 1.21

#Preguntar cantidades al usuario
cantidad_camisetas = int(input("¿Cuántas camisetas quiere comprar? "))
cantidad_sudaderas = int(input("¿Cuántas sudaderas quiere comprar? "))
cantidad_gorras = int(input("¿Cuántas gorras quiere comprar? "))

#Operaciones
multiplicacion_camisetas = camisetas * cantidad_camisetas 
multiplicacion_sudaderas = sudaderas * cantidad_sudaderas
multiplicacion_gorras = gorras * cantidad_gorras 
total_sin_IVA = multiplicacion_camisetas + multiplicacion_sudaderas + multiplicacion_gorras
total_con_IVA = total_sin_IVA * recargo_IVA

#Resultados
print("Costo camisetas sin IVA: ", multiplicacion_camisetas)
print("Costo sudaderas sin IVA: ", multiplicacion_sudaderas)
print("Costo gorras sin IVA: ", multiplicacion_gorras)
print("Total a pagar sin IVA: ", total_sin_IVA)
print("Total a pagar con IVA: ", total_con_IVA)