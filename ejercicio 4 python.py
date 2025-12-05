def capturar_radio():
    print("capturar datos")
    radio = float(input("Digite el radio del cilindro: "))
    return radio
def capturar_altura():
    altura = float(input("Digite la altura del cilindro: "))
    return altura


def procesar_datos(r, h):
    print("procesar datos")
    pi = 3.1416
    volumen = pi * (r * r) * h
    return volumen


def mostrar_resultados(vol):
    print("resultados")
    print("El volumen del cilindro es:", vol)


# Programa principal
radio = capturar_radio()
altura =capturar_altura()
volumen = procesar_datos(radio, altura)
mostrar_resultados(volumen)