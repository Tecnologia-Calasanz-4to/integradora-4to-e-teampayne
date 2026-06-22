#PARTE A
def nombre_valido(nombre):   
    if len(nombre) >= 3 and nombre.isalpha():
        devolver=True
    else:
        devolver=False
    return devolver
def crear_codename(nombre, nivel):
  return nombre[0:3].upper() + "-Lv" + str(nivel)
def vida_maxima(nivel):
  r = 100 + nivel ** 2 * 5
  return r

#programa principal
nombre=str(input("ingrese nombre"))
nivel=int(input("ingrese nivel"))
C1=nombre[0:3].upper() 
if nombre_valido(nombre)==True:
    print(crear_codename(nombre, nivel))
    print(vida_maxima(nivel))
else:
    print("error")
