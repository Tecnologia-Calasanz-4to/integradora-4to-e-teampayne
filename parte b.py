# ===== PARTE B =====

def ClasificarArma():
    return    # TODO: if/elif/else -> "Legendaria"/"Media"/"Debil"
    print("1. Legendaria")
    print("2. Media")
    print("3. Débil")
    opción=int (input("Elige una opción"))
    if opción==1:
        print("El arma legendaria es mágica y capaz de destruir en pocos golpes al enemigo")
        devolver = "Legendaria"
    elif opción==2:
        print("El arma media posee una gran capacidad de ganar ventaja contra el enemigo, sin ser del todo mágica")
        devolver= "Media"
    elif opción==3:
        print ("El armma débil no contiene magia pero si sos un guerrero nato, ganarías fácilmente")
        devolver= "Débil"
    return devolver

def EsCritico(es_magica, nivel):

    return    # TODO: es_magica or nivel >= 10
    

def dano_base(ataque, poder, defensa):
    return    # TODO: (ataque + poder) - defensa
def dano_total(ataque, poder, defensa, critico):
    return    # TODO: si critico -> dano_base(...) * 2 ; si no -> dano_base(...)
