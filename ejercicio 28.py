# Diseña un algoritmo que solicite la base y la altura de un triángulo y calcule su área.

def tomar_base():
    base = int(input("Digite la base del triángulo: "))
    return base

def tomar_altura():
    altura = int(input("Digite la altura del triángulo: "))
    return altura

def calcular_area(base, altura):
    area = (base * altura) / 2 
    return area

def mostrar_resultado(area):
    print("El área del triángulo es:", area)

# CÓDIGO PRINCIPAL.

base = tomar_base() 

altura = tomar_altura() 

area = calcular_area(base, altura) 

mostrar_resultado(area) 
