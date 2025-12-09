# Crea un algoritmo que pida al usuario dos números y calcule la resta del primero menos el segundo.


def prim_num():
    onenum = int(input("digitar un primer número: "))
    return onenum

def seg_num():
    secnum = int(input("digitar un segundo número, que se le restará al primero que insertó: "))
    return secnum

def resta(onenum, secnum):
    resta_nums = onenum - secnum
    return resta_nums

def mostrar_resultado(resta_nums):
    print("La resta del primer número y el segundo da como resultado:", resta_nums)

# CÓDIGO PRINCIPAL 

onenum = prim_num() 

secnum = seg_num() 

resta_nums = resta(onenum, secnum) 

mostrar_resultado(resta_nums) 

