# Crea un algoritmo que determine el residuo de la división entre dos números ingresados por el usuario.

def prim_num():
    onenum = int(input("digitar un primer número: "))
    return onenum

def seg_num():
    secnum = int(input("digitar un segundo número: "))
    return secnum

def residuo(onenum, secnum):
    resid_nums = onenum % secnum
    return resid_nums

def mostrar_resultado(resid_nums):
    print("El residuo entre ambos números da como resultado:", resid_nums)

# CÓDIGO PRINCIPAL 

onenum=prim_num()

secnum=seg_num() 

resid_nums=residuo(onenum, secnum) 

mostrar_resultado(resid_nums) 
