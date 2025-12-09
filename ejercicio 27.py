#  Desarrolla un programa que pida un número y calcule su raíz cuadrada utilizando operadores aritméticos.


def numero():
    num = int(input("digitar un número, para averiguar su raíz cuadrada: "))
    return num

def raiz_cuad(num):
    raiz = num ** (1/2)
    return raiz

def imprimir_rslt(raiz):
    print("La raíz cuadrada del número que insertó es:", raiz)

# CÓDIGO PRINCIPAL

num = numero() 

raiz = raiz_cuad(num) 

imprimir_rslt(raiz)  