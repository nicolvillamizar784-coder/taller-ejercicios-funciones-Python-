# Diseña un algoritmo que solicite la cantidad de dinero en una cuenta y calcule el 5% de interés.

# ZONA DE FUNCIONES. 

def dinero_cuenta():
    dinero = float(input("Inserte la cantidad de dinero que hay en su cuenta: "))
    return dinero

def calcular_interes(dinero):
    interes = dinero * 0.05
    return interes

def total(dinero, interes):
    tot = dinero + interes
    return tot

def imprimir_rslt(interes, tot):
    print("el interés de su cuenta es de:", interes)
    print("el total en la cuenta después de sumar el interés es de:", tot)

# CÓDIGO PRINCIPAL.

dinero = dinero_cuenta() 

interes = calcular_interes(dinero) 

tot = total(dinero, interes) 

imprimir_rslt(interes, tot) 
