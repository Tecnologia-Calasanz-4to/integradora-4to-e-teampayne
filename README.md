[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/RTVpv1sI)
# Actividad integradora de Tecnologías de la información — 4° año

## Proyecto: **"Dark Python"**

### La idea

Su grupo programará un videojuego de rol con **combate por turnos**.
El progama tiene que ser **interactivo**: le
pide datos al usuario (`input`), valida lo que ingresa, crea el personaje, calcula
el daño y resuelve un combate contra un enemigo cuya dificultad **elige el
usuario**.

El programa final es uno solo, dividido en **4 partes**. **Cada
integrante se hace cargo de una parte completa.** Las cuatro partes tienen la
misma estructura y dificultad, así cada uno trabaja y se evalúa por igual.

> **Lo más importante de la evaluación es el código y que cada uno entienda la
> totalidad del codigo.** En la defensa, cada integrante explica **su** parte línea por línea y como se integra en el código total.

> ✅ **Temas que hay que usar (todos vistos en clase):** tipos de datos (`str`,
> `int`, `float`, `bool`) y conversiones (`int()`, `float()`, `str()`); variables
> e `input()`; **cadenas** (concatenación, `len()`, índices, slices `[a:b]`,
> métodos como `.upper()`, `.capitalize()`, `.isalpha()`, `.isdigit()`);
> funciones con `def` / `return` y **que se llamen entre sí**; condicionales
> `if / elif / else`; operadores `+ - * ** / % //` y `and`,
> `or`, `not`.

---

## Estructura de cada parte

Cada integrante entrega **varias funciones** (no una sola), variables con su
tipo de dato anotado en un comentario, y **una decisión `if/elif/else`**. Recordá lo que
dice el apunte: las funciones que **calculan** deben recibir los datos por
parámetro y **devolver** (`return`) el resultado, no imprimirlo.

---

### PARTE A — Creación del personaje 🧙

- **`nombre_valido(nombre)`** → devuelve `True` si el nombre tiene al menos 2
  caracteres **y** son todas letras.**
- **`crear_codename(nombre, nivel)`** → arma un identificador con las **3 primeras
  letras en mayúscula** + el nivel.
- **`vida_maxima(nivel)`** → `100 + nivel ** 2 * 5`.

### PARTE B — Arma y daño ⚔️ ñ

- **`clasificar_arma(poder)`** → devuelve `"Legendaria"`, `"Media"` o `"Debil"`
  según la selección del usuario.
- **`es_critico(es_magica, nivel)`** → `True` si el arma es mágica **o** el nivel
  es 10 o más.
- **`dano_base(ataque, poder, defensa)`** → `(ataque + poder) - defensa`.
- **`dano_total(ataque, poder, defensa, critico)`** → si es crítico devuelve el
  **doble** del `dano_base(...)`; si no, el daño normal. *(esta función **llama a
  `dano_base`**)*

### PARTE C — Vida y pociones ❤️

- **`porcentaje_vida(actual, maxima)`** → `actual / maxima * 100`. *(`/`, `*`)*
- **`estado_vida(porcentaje)`** → devuelve `"CRITICO"` (≤25), `"HERIDO"` (≤50) o
  `"SANO"`. *(`if/elif/else` que devuelve un `str`)*
- **`comprar_pociones(monedas, precio)`** → devuelve **cuántas** pociones se pueden
  comprar (`//`) y el **vuelto** (`%`).

### PARTE D — Combate y resultado 🏆 

- **`puede_atacar(energia, esta_aturdido)`** → `True` si tiene energía **y no**
  está aturdido.
- **`vida_restante(vida, dano)`** → la vida después del golpe, pero **nunca menor
  que 0**
- **`gana(vida_heroe, vida_enemigo)`** → `True` si el héroe sigue vivo **y** el
  enemigo no.

> Si el grupo es de 3, repartan la Parte D entre todos.

---

En el programa principal:

1. Pedir el **nombre** con `input()` y validarlo con `nombre_valido(...)`. Si no
   sirve, usar un nombre por defecto. Después aplicarle `.capitalize()`.
2. Pedir el **nivel** con `int(input(...))` y calcular la vida máxima.
3. Mostrar el **codename** y la **clasificación del arma**.
4. Pedir la **dificultad** del enemigo (`"facil"` / `"dificil"`) y, con un
   `if/else`, asignarle vida, defensa y ataque.

### El combate (2 turnos)

Usando **todas las funciones del grupo**:

1. **Turno 1:** solo si `puede_atacar(...)`, calcular si es crítico, el daño total
   y la vida que le queda al enemigo (con `vida_restante`).
2. **Turno 2:** solo `if` el enemigo sigue vivo, el enemigo contraataca; mostrar
   la vida del héroe, su **porcentaje** y su **estado** (`estado_vida`).
3. Mostrar el resultado final con `if / elif / else`: héroe gana, héroe derrotado
   o el combate sigue.

Prueben con **dos casos distintos** (por ejemplo: nombre válido + enemigo difícil,
y un nombre inválido + enemigo fácil) para mostrar que las validaciones y la
lógica responden bien.

---

## Esqueleto para arrancar

```python
# ===== PARTE A =====
def nombre_valido(nombre):
    pass    # TODO: len(nombre) >= 2 and nombre.isalpha()
def crear_codename(nombre, nivel):
    pass    # TODO: nombre[0:3].upper() + "-Lv" + str(nivel)
def vida_maxima(nivel):
    pass    # TODO: 100 + nivel ** 2 * 5

# ===== PARTE B =====
def clasificar_arma(poder):
    pass    # TODO: if/elif/else -> "Legendaria"/"Media"/"Debil"
def es_critico(es_magica, nivel):
    pass    # TODO: es_magica or nivel >= 10
def dano_base(ataque, poder, defensa):
    pass    # TODO: (ataque + poder) - defensa
def dano_total(ataque, poder, defensa, critico):
    pass    # TODO: si critico -> dano_base(...) * 2 ; si no -> dano_base(...)

# ===== PARTE C =====
def porcentaje_vida(actual, maxima):
    pass    # TODO: actual / maxima * 100
def estado_vida(porcentaje):
    pass    # TODO: if/elif/else -> "CRITICO"/"HERIDO"/"SANO"
def comprar_pociones(monedas, precio):
    pass    # TODO: monedas // precio  y  monedas % precio

# ===== PARTE D =====
def puede_atacar(energia, esta_aturdido):
    pass    # TODO: energia > 0 and not esta_aturdido
def vida_restante(vida, dano):
    pass    # TODO: si vida - dano < 0 -> 0 ; si no -> vida - dano
def gana(vida_heroe, vida_enemigo):
    pass    # TODO: vida_heroe > 0 and vida_enemigo <= 0

# ===== PROGRAMA PRINCIPAL=====
# TODO: pedir nombre y nivel, validar, crear el heroe.
# TODO: elegir dificultad del enemigo con if/else.
# TODO: turno 1, turno 2 y resultado final.
```

---

## Cómo se evalúa (por alumno)

| Criterio | Puntos |
|---|---|
| **El código funciona** (todas sus funciones devuelven lo correcto) | 25 |
| **Explica su código** en la defensa (qué hace cada línea y por qué) | 30 |
| Tipos de datos y conversiones usados correctamente | 15 |
| Operadores y/o manejo de cadenas usados con sentido | 15 |
| Una función que **llame a otra** o un `if/elif/else` bien resuelto | 10 |
| Código legible: nombres claros y comentarios| 5 |
| **Total individual** | **100** |

> El combate final (integración de las 4 partes) suma como **nota grupal aparte**.
> Si un alumno no puede explicar su propia parte, esa parte no se aprueba aunque el
> código funcione.

## Desafíos extra:

- Validar que el **nivel** ingresado sea un número con `.isdigit()` antes de
  convertirlo.
- Que el codename incluya también la **última letra** del nombre (`nombre[-1]`).
- Agregar un **tercer turno** o un segundo enemigo con otra dificultad.
