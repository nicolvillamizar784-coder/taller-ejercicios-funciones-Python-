#  Escribe un programa que solicite dos números y calcule la división del primero entre el segundo.


def prim_num():
    onenum = int(input("digitar un primer número: "))
    return onenum

def seg_num():
    secnum = int(input("digitar un segundo número, que se dividirá con el primero que insertó: "))
    return secnum

def divis(onenum, secnum):
    divis_nums = onenum / secnum
    return divis_nums

def mostrar_resultado(divis_nums):
    print("La división del primer número entre el segundo da como resultado:", divis_nums)

# CÓDIGO PRINCIPAL 

onenum = prim_num() 

secnum = seg_num() 

divis_nums = divis(onenum, secnum) 

mostrar_resultado(divis_nums) 