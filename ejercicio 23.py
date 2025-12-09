#  Desarrolla un programa que requiera dos números y muestre el producto de dichos valores.


def prim_num():
    onenum = int(input("digitar un primer número: "))
    return onenum

def seg_num():
    secnum = int(input("digitar un segundo número, que se multiplicará con el primero que insertó: "))
    return secnum

def multip(onenum, secnum):
    multip_nums = onenum * secnum
    return multip_nums

def mostrar_resultado(multip_nums):
    print("La multiplicación del primer número con el segundo da como resultado:", multip_nums)

# CÓDIGO PRINCIPAL 

onenum = prim_num() 

secnum = seg_num() 

multip_nums = multip(onenum, secnum) 

mostrar_resultado(multip_nums) 