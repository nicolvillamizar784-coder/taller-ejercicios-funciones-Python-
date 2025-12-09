# Convertir pulgadas a centímetros.

def toma_pulgadas():
    pulgadas = float(input("digitar la cantidad de pulgadas que desea convertir a centímetros: "))
    return pulgadas

def conv_cm(pulgadas):
    cm = pulgadas * 2.64
    return cm

def mostrar_resultado(cm):
    print("La cantidad de pulgadas que insertó, se traducen a", cm, "centímetros.")

# CÓDIGO PRINCIPAL 

pulgadas=toma_pulgadas() 

cm=conv_cm(pulgadas) 

mostrar_resultado(cm) 
