#  Determinar el volumen de un prisma rectangular con longitud, ancho y altura especificados. 

def obt_longitud():
    longitud = int(input("digitar la longitud del prisma rectangular (centímetros): "))
    return longitud

def obt_ancho():
    ancho = int(input("digitar el ancho del prisma rectangular (centímetros): "))
    return ancho

def obt_altura():
    altura = int(input("digitar la altura del prisma rectangular (centímetros): "))
    return altura

def calcular_volumen(longitud, ancho, altura):
    volumen = longitud * ancho * altura
    return volumen

def imprimir_resultado(volumen):
    print("El volumen del prisma rectangular es:", volumen)

# CÓDIGO PRINCIPAL

longitud=obt_longitud() 

ancho=obt_ancho() 

altura=obt_altura() 

volumen=calcular_volumen(longitud, ancho, altura) 

imprimir_resultado(volumen) 
