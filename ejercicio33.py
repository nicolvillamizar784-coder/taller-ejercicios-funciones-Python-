# Crea un algoritmo que solicite una distancia en kilómetros y la convierta a millas. 

# ZONA DE FUNCIONES. 

def tomar_kilometros():
    kilometros = float(input("digite la cantidad de kilometros que desea convertir a millas: "))
    return kilometros

def calcular_millas(kilometros):
    millas = kilometros / 1.609
    return millas

def imprimir_resultado(millas):
    print("la cantidad de kilometras equivale a", millas, "millas.")

# CÓDIGO PRINCIPAL 

kilometros = tomar_kilometros() 

millas = calcular_millas(kilometros) 

imprimir_resultado(millas) 