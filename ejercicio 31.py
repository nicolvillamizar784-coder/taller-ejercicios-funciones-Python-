#  Desarrolla un programa que pida un número de horas y lo convierta a minutos utilizando operadores aritméticos.


def toma_hora():
    horas = int(input("Inserte el número de horas que quiere convertir a minutos: "))
    return horas

def calc_mins(horas):
    mins = horas * 60
    return mins

def mostrar_resultado(mins):
    print("Las cantidad de horas que introdujo, se traducen a:", mins, "minutos.")

# CÓDIGO PRINCIPAL.

horas = toma_hora() 

mins = calc_mins(horas) 

mostrar_resultado(mins) 

