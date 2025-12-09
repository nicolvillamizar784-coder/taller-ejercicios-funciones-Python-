#  Diseña un algoritmo que pida un número y calcule su cuadrado utilizando el operador de multiplicación.


def numero():
    num = int(input("digitar un número para averiguar su cuadrado: "))
    return num

def cuad_num(num):
    cuadrado = num ** 2
    return cuadrado

def mostrar_resultado(cuadrado):
    print("El cuadrado del número que insertó es:", cuadrado)

# CÓDIGO PRINCIPAL 

num = numero() 
cuadrado = cuad_num(num) 

mostrar_resultado(cuadrado) 

