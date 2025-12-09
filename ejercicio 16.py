# Determinar el volumen de un cubo con la longitud de un lado especificada

def long_lado():
    lado = int(input("digitar la longitud del lado (centímetros): "))
    return lado

def calcular_volumen():
    volumen = lado ** 3
    return volumen

def mostrar_resultado(volumen):
    print("El volumen del cubo es:", volumen)

# CÓDIGO PRINCIPAL.

lado=long_lado() 

volumen=calcular_volumen() 

mostrar_resultado(volumen) 
