# Convertir kilómetros a millas

def obt_kilometros():
    kms = float(input("digite la cantidad de kilometros que desea convertir a millas: "))
    return kms

def calcular_mlls(kms):
    millas = kms / 1.609
    return millas

def imprimir_rslt(millas):
    print("La cantidad de kilometros que digito se traduce a", millas, "millas.")

# CÓDIGO PRINCIPAL 

kms = obt_kilometros() 

millas = calcular_mlls(kms) 

imprimir_rslt(millas) 

