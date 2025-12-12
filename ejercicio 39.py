# Diseña un algoritmo que solicite dos números y calcule el promedio de ambos. 

# ZONA DE FUNCIONES. 

def primer_numero():
    num1 = int(input("Inserte el primer número: "))
    return num1

def segundo_numero():
    num2 = int(input("Inserte el segundo número: "))
    return num2

def calcular_promedio(num1, num2):
    promedio = (num1 + num2) / 2
    return promedio 

def imprimir_resultado(promedio):
    print("El promedio de ambos números es de:", promedio)

# CÓDIGO PRINCIPAL. 

num1 = primer_numero() 

num2 = segundo_numero() 

promedio = calcular_promedio(num1, num2) 

imprimir_resultado(promedio) 

