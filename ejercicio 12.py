# Calcular el área de un cuadrado con el lado dado.

def toma_lado():
    lado = int(input("digite el lado del cuadrado (centímetros): "))
    return lado

def calcular_area(lado):
    area = lado ** 2
    return area

def mostrar_resultado(area):
    print("El area del cuadrado es:", area)

# CÓDIGO PRINCIPAL 

lado=toma_lado() 

area=calcular_area(lado)

mostrar_resultado(area)