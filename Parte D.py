def puede_atacar(energia, esta_aturdido):
    return energia > 0 and not esta_aturdido

def vida_restante(vida, dano):
    if vida - dano < 0:
        return 0
    else:
        return vida - dano

def gana(vida_heroe, vida_enemigo):
    return vida_heroe > 0 and vida_enemigo <= 0

print(puede_atacar(10, False))
print(puede_atacar(0, False)) 
print(puede_atacar(5, True)) 

print(vida_restante(100, 30)) 
print(vida_restante(20, 50)) 

print(gana(50, 0))
print(gana(50, -10))
print(gana(0, 0)) 

