# Determinar el volumen de un prisma triangular con la longitud de la base, altura y ancho especificados.


def long_base():
    longitud = int(input("digitar la longitud de la base del prisma triangular (centímetros): "))
    return longitud

def altura_pris():
    altura = int(input("digitar la altura del prisma triangular (centímetros): "))
    return altura

def altura_triang():
    alturat = int(input("digitar la altura del triángulo (centímetros): "))
    return alturat

def calc_volumen(longitud, altura, alturat):
    volumen = (longitud * altura * alturat) / 2
    return volumen

def mostrar_resultado(volumen):
    print("El volumen del prisma triangular es:", volumen)

# CÓDIGO PRINCIPAL.

longitud = long_base() 

altura = altura_pris() 

alturat = altura_triang() 

volumen = calc_volumen(longitud, altura, alturat) 

mostrar_resultado(volumen) 



