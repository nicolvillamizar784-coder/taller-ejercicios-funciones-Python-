# Escribe un programa que pida dos números enteros y muestre el cociente de la división entera.

# ZONA DE FUNCIONES. 

def primer_num():
    num1 = int(input("Inserte el primer número: "))
    return num1

def segundo_num():
    num2 = int(input("Inserte el segundo número: "))
    return num2

def calcular_cociente(num1, num2):
    cociente = num1 // num2
    return cociente

def imprimir_resultado(cociente):
    print("El cociente de la división es:", cociente)

# CÓDIGO PRINCIPAL.

num1 = primer_num() 

num2 = segundo_num() 

cociente = calcular_cociente(num1, num2) 

imprimir_resultado(cociente) 

