#Calcular el área de un rectángulo con longitud y ancho dados.

#pide longitud y ancho 
def capturar_longitud():
    print("calcular el area de un rectangulo")
    longitud = float(input("Digite la longitud: "))
    return longitud
def capturar_ancho():

    ancho = float(input("Digite el ancho: "))
    return ancho

#calcula el area multiplicando longitud * ancho 
def procesar_datos(longitud, ancho):
    area = longitud * ancho
    return area

#muestra el area 
def mostrar_resultados(area):
    print("El área del rectángulo es:", area)

# Programa principal
longitud = capturar_longitud()
ancho = capturar_ancho()
area = procesar_datos(longitud, ancho)
mostrar_resultados(area)