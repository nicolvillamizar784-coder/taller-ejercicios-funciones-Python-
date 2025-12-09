#  Calcular el área de un hexágono regular con su lado dado.

def toma_lado():
    lado = int(input("digitar el lado del hexágono (centímetros): "))
    return lado

def calcular_perimetro(lado):
    perimetro = lado * 6
    return perimetro

def calcular_apotema(lado):
    apotema = (lado ** (1/3)) / 2 
    return apotema

def calcular_area(perimetro, apotema):
    area = (perimetro * apotema) / 2
    return area

def mostrar_resultado(area):
    print("El área del hexágono es:", area)

# CÓDIGO PRINCIPAL.

lado = toma_lado()

perimetro = calcular_perimetro(lado)
 
apotema = calcular_apotema(lado) 

area = calcular_area(perimetro, apotema) 

mostrar_resultado(area) 