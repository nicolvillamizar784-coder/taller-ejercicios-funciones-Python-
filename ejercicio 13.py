#Determinar el volumen de una pirámide con longitud de la base, ancho de la base y altura especificados. 

def long_base():
    long = int(input("digitar la longitud de la base de la pirámide (centímetros): "))
    return long

def ancho_base():
    ancho = int(input("digitar el ancho de la base de la pirámide (centímetros): "))
    return ancho

def altura_pir():
    altura = int(input("digitar la altura de la pirámide (centímetros): "))
    return altura

def calcular_area_base(long, ancho):
    area_base = long * ancho 
    return area_base

def calcular_volumen(area_base, altura):
    volumen = (1 / 3) * (area_base * altura)
    return volumen

def mostrar_resultado(volumen):
    print("El volumen de la pirámide es:", volumen)

# CÓDIGO PRINCIPAL.
 
long=long_base() 

ancho=ancho_base() 

altura=altura_pir() 

area_base=calcular_area_base(long, ancho)

volumen=calcular_volumen(area_base,altura)

mostrar_resultado(volumen) 