# Desarrolla un programa que pida dos números y muestre el mayor de los dos utilizando operadores aritméticos.

# ZONA DE FUNCIONES.

def primer_numero():
    num1 = int(input("Inserte el primer número: "))
    return num1

def segundo_numero():
    num2 = int(input("Inserte el segundo número: "))
    return num2

def mayoromenor(num1, num2):
    if num1 > num2:
        print("El primer número es mayor que el segundo.")
    else:
        print("El segundo número es mayor que el primero.")

def imprimir_resultado():
    print("El programa finalizó.")

# CÓDIGO PRINCIPAL. 

num1 = primer_numero() 

num2 = segundo_numero() 

mayoromenor(num1, num2) 

imprimir_resultado() 