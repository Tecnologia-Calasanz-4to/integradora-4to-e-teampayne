# ===== PARTE B =====

def ClasificarArma(poder):
    # TODO: if/elif/else -> "Legendaria"/"Media"/"Debil"
    if poder>1000:
        print("El arma legendaria es mágica y capaz de destruir en pocos golpes al enemigo")
        devolver = "Legendaria"
    elif poder<1000 and poder > 500:
        print("El arma media posee una gran capacidad de ganar ventaja contra el enemigo, sin ser del todo mágica")
        devolver= "Media"
    elif poder < 500:
        print ("El armma débil no contiene magia pero si sos un guerrero nato, ganarías fácilmente")
        devolver= "Débil"
    return devolver

def EsCritico(es_magica, nivel):
    if es_magica or nivel>=10:
        devolver= True
    else:
        devolver= False
    return devolver
    

def dano_base(ataque, poder, defensa):
    dano= (ataque+poder)-defensa
    return  dano
def dano_total(ataque, poder, defensa, critico):
    if critico == True:
        devolver= dano_base(ataque, poder, defensa)
    elif critico == False:
        devolver = dano_base(ataque, poder, defensa)
    return devolver
