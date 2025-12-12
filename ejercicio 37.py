# Crea un algoritmo que determine si un número es múltiplo de otro ingresados por el usuario.

# ZONA DE FUNCIONES. 

def primer_numero():
    num1 = int(input("Inserte el primer número: "))
    return num1

def segundo_numero():
    num2 = int(input("Inserte el segundo número: "))
    return num2

def multiplicacion(num1, num2):
    if num1 % num2 == 0:
        print("El primer número es múltiplo del segundo.\n")
    else: 
        print("El primer número no es múltiplo del segundo.\n")

def imprimir_resultado():
    print("El programa finalizó.")

# CÓDIGO PRINCIPAL.

num1 = primer_numero()

num2 = segundo_numero() 

multiplicacion(num1, num2) 

imprimir_resultado() 
