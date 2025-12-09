#Calcular el área de un trapecio con sus longitudes de bases y altura especificadas. 

def obt_basemenor(): 
    basemenor = int(input("digitar la base menor del trapecio (centímetros): "))
    return basemenor

def obt_basemayor():
    basemayor = int(input("digitar la base mayor del trapecio (centímetros): "))
    return basemayor

def obt_altura():
    altura = int(input("digitar la altura del trapecio (centímetros): "))
    return altura

def calcular_area(basemenor, basemayor, altura):
    area = ((basemenor + basemayor) * altura) / 2
    return area

def imprimir_resultado(area):
    print("El área del trapecio es: ", area)

# CÓDIGO PRINCIPAL. 

basemenor= obt_basemenor() 

basemayor= obt_basemayor() 

altura= obt_altura() 

area= calcular_area(basemenor, basemayor, altura) 

imprimir_resultado(area) 