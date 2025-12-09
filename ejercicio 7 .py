def capturar_radio():
    # Pedimos el radio
    radio = float(input("Digite el radio del cono: "))
    return radio

def capturar_altura():
    # Pedimos la altura
    altura = float(input("Digite la altura del cono: "))
    return altura

def procesar_datos(r, h):
    # Calculamos el volumen del cono SIN usar math
    pi = 3.1416
    volumen = (1/3) * pi * (r * r) * h
    return volumen

def mostrar_resultados(volumen):
    # Mostramos el resultado
    print("resultado")
    print("El volumen del cono es:", volumen)

# Programa principal
radio = capturar_radio()      # return del radio
altura = capturar_altura()    # return de la altura
volumen = procesar_datos(radio, altura)
mostrar_resultados(volumen)