# Escribe un programa que pida un número y determine si es par o impar usando el operador de módulo (%).


def numero():
    num = int(input("digitar un número para saber si par o impar: "))
    return num

def par_imp(num):
    if num % 2 == 0:
        print("El número es par.")
    else:
        print("El número es impar.")

def mostrar_resultado():
    print("El programa finalizó.")

# CÓDIGO PRINCIPAL.

num = numero() 

par_imp(num) 

mostrar_resultado()