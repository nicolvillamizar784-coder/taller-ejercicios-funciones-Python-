#  Crea un algoritmo que solicite el radio de un círculo y calcule su circunferencia. 


def toma_radio():
    radio = float(input("digitar el radio del círculo: "))
    return radio

def calc_circ(radio):
    circunf = 2 * 3.1416 * radio
    return circunf

def mostrar_resultado(circunf):
    print("La circunferencia de el círculo es:", circunf)

# CÓDIGO PRINCIPAL.

radio = toma_radio() 

circunf = calc_circ(radio)

mostrar_resultado(circunf)

