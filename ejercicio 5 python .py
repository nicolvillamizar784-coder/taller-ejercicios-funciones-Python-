import math

def capturar_datos():
    print("calcular el area de un circulo")
    radio = float(input("Digite el radio del círculo: "))
    return radio

def procesar_datos(radio):
    area = math.pi * radio * radio
    return area

def mostrar_resultados(area):
    print("El área del círculo es:", area)

# Programa principal
radio_capturado = capturar_datos()
resultado = procesar_datos(radio_capturado)
mostrar_resultados(resultado)