#PARTE C
def porcentaje_vida(actual, maxima):
    r= actual / maxima * 100
    return r 
def estado_vida(porcentaje):
    if porcentaje <= 25:
        devolver="CRITICO"
    elif porcentaje <= 50:
        devolver="HERIDO"
    else:
        devolver="SANO"
    return devolver
def comprar_pociones(monedas, precio):
    cantidadpociones= monedas // precio
    vuelto= monedas % precio
    return cantidadpociones, vuelto
