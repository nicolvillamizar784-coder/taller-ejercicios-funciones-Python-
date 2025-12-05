#captura los datos del usuario
def capturar_datos():
    print("calculo del volumen del cono")
    radio = float(input("Digite el radio de la base: "))
    altura = float(input("Digite la altura del cono: "))
    return radio, altura

#aplica la formula del volumen 
def procesar_datos(r, h):
    volumen = (1/3) * 3.1416 * (r * r) * h
    return volumen

#muestra los resutados 
def mostrar_resultados(volumen):
    print("El volumen del cono es:", volumen)

# Programa principal
radio, altura = capturar_datos()
volumen_final = procesar_datos(radio, altura)
mostrar_resultados(volumen_final)