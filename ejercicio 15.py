#  Calcular el área de un paralelogramo con base y altura dadas.

def tomar_base():
    base = int(input("digitar la base del paralelogramo (centímetros): "))
    return base

def tomar_altura():
    altura = int(input("digitar la altura del paralelogramo (centímetros): "))
    return altura

def calcular_area(base, altura):
    area = base * altura
    return area

def mostrar_resultado(area):
    print("El área del paralelogramo es:", area)

# CÓDIGO PRINCIPAL.

base=tomar_base() 

altura=tomar_altura() 

area=calcular_area(base, altura) 

mostrar_resultado(area)