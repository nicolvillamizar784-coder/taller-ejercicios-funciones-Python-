#Determinar el volumen de una esfera con su radio dado

#pide el radio y lo entrega

def capturar_datos():
    print("calcular volumen de una esfera")
    radio = float(input("Digite el radio de la esfera: "))
    return radio

#hace la formula del volumn con radio 

def procesar_datos(radio):
    volumen = (4/3) * 3.1416 * (radio * 3)
    return volumen

#muestra el volumen ya calculado

def mostrar_resultado(volumen):
    print("El volumen de la esfera es:", volumen)


# Programa principal
radio = capturar_datos()
volumen = procesar_datos(radio)
mostrar_resultado(volumen)