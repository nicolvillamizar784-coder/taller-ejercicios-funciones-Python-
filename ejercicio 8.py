#  Convertir dólares a euros utilizando una tasa de cambio dada.

def tomar_tasacambio():
    dolar_cambio = float(input("digite el valor de un dólar en euros: "))
    return dolar_cambio

def tomar_conversion():
    dolares_cliente = float(input("¿Cuántos dólares desea convertir a euros?\n = "))
    return dolares_cliente

def conversion_dolareuro(dolar_cambio, dolares_cliente):
    euros_cliente = dolar_cambio * dolares_cliente
    return euros_cliente

def imprimir_resultado(euros_cliente):
    print("La cantidad de dólares que insertó, se traduce en", euros_cliente, "euros.")

# CÓDIGO PRINCIPAL.

dolar_cambio = tomar_tasacambio() 
dolares_cliente = tomar_conversion() 
euros_cliente = conversion_dolareuro(dolar_cambio, dolares_cliente) 

imprimir_resultado(euros_cliente) 