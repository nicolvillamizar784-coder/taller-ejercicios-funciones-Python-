#  Convertir libras a kilogramos.

def toma_libras():
    libras = float(input("digitar la cantidad de libras que desea convertir a kilogramos: "))
    return libras

def convertir_kg(libras):
    kgs = libras / 2.205
    return kgs

def mostrar_resultado(kgs):
    print("La cantidad de libras que insertó, se traducen en", kgs, "kilogramos.")

# CÓDIGO PRINCIPAL.

libras = toma_libras() 

kgs = convertir_kg(libras) 

mostrar_resultado(kgs) 

