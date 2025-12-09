#  Diseña un algoritmo que calcule el área de un rectángulo, solicitando su longitud y ancho.

def tomar_longitud():
    longitud = int(input("digitar la longitud del rectángulo (centímetros): "))
    return longitud

def tomar_ancho():
    ancho = int(input("digitar el ancho del rectángulo (centímetros): "))
    return ancho

def calcular_area(longitud, ancho):
    area = longitud * ancho 
    return area

def mostrar_resultado(area):
    print("El área del rectángulo es:", area)

# CÓDIGO PRINCIPAL

longitud = tomar_longitud() 

ancho = tomar_ancho()  

area = calcular_area(longitud, ancho) 

mostrar_resultado(area) 
