#  Escribe un programa que solicite dos números al usuario y muestre la suma de ambos. 

def prim_num():
    onenum = int(input("digitar un primer número: "))
    return onenum

def seg_num():
    secnum = int(input("digitar el segundo número para sumarlo con el primero: "))
    return secnum

def sumanum(onenum, secnum):
    suma = onenum + secnum
    return suma

def mostrar_resultado(suma):
    print("La suma de ambos números es:", suma)

# CÓDIGO PRINCIPAL.

onenum = prim_num()

secnum = seg_num() 

suma = sumanum(onenum, secnum) 

mostrar_resultado(suma)  