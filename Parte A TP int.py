def nombre_valido(nombre):
  return len(nombre) >= 2 and nombre.isalpha() 
def crear_codename(nombre, nivel):
  return nombre[0:3].upper() + "-Lv" + str(nivel)
def vida_maxima(nivel):
  r = 100 + nivel ** 2 * 5
  return r


nombre=str(input("ingrese nombre"))
nivel=int(input("ingrese nivel"))
C1=nombre[0:3].upper() 
print(C1 + " " + nivel)
print(vida_maxima(nivel))
