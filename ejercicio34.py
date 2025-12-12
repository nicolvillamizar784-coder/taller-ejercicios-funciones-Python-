# Desarrolla un programa que pida el precio de un artículo y calcule el 10% de descuento. 

# ZONA DE FUNCIONES.

def tomar_precio():
    precio = int(input("inserte el precio del artículo: "))
    return precio

def calcular_descuento(precio):
    desc = precio * 0.10
    return desc

def precio_final(desc, precio):
    precio_final = precio - desc
    return precio_final

def imprimir_resultado(precio_final):
    print("con 10% de descuento, el precio del artículo es de:", precio_final)

# CÓDIGO PRINCIPAL. 

precio = tomar_precio() 

desc = calcular_descuento(precio) 

precio_final = precio_final(desc, precio) 

imprimir_resultado(precio_final) 