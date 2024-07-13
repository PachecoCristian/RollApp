from configuracion import *

from random import randint
from re import compile, S as dot


     
# Modulos / Metodos
def letra_aleatoria():
    rango = len(RANDOM_NAME)-1
    valor = RANDOM_NAME[randint(0,rango)]
    opcion = None
    regex = compile('[a-zA-Z]+')
    if regex.match(valor) == None:
        desc= descripción_aleatoria()
        opcion = f"{desc[0]} - {desc[1]}"
    return valor,opcion

def descripción_aleatoria():
    valor1 = RANDOM_DESCRIPTOR_1[randint(0,len(RANDOM_DESCRIPTOR_1)-1)]
    valor2 = RANDOM_DESCRIPTOR_2[randint(0,len(RANDOM_DESCRIPTOR_2)-1)]

    return (valor1,valor2)

def descripción_lugar():
    valor1 = RANDOM_LOCATION[randint(0,len(RANDOM_LOCATION)-1)]
    valor2 = RANDOM_LOCATION[randint(0,len(RANDOM_LOCATION)-1)]

    return (valor1,valor2)

def nombre_lugar_aleatorio():
    nombre= RANDOM_PLACES_NAME[randint(0,len(RANDOM_PLACES_NAME)-1)]
    return nombre

def adjetivos_lugar_aleatorio(nombre):
    ref = nombre
    reg_ex_P= compile(r".*\[Place\].*",dot)     
    if reg_ex_P.match(nombre) != None:
        nombre= nombre.replace("[Place]",f"[{RANDOM_PLACES_ADJ[randint(0,len(RANDOM_PLACES_ADJ)-1)][0]}]")
    reg_ex_A= compile(r".*\[Adjective\].*",dot)
    if reg_ex_A.match(nombre) != None:
        nombre= nombre.replace("[Adjective]",f"[{RANDOM_PLACES_ADJ[randint(0,len(RANDOM_PLACES_ADJ)-1)][1]}]")
    reg_ex_N= compile(r".*\[Noun\].*",dot)
    if reg_ex_N.match(nombre) != None:
        nombre= nombre.replace("[Noun]",f"[{RANDOM_PLACES_ADJ[randint(0,len(RANDOM_PLACES_ADJ)-1)][2]}]")
    
    return nombre, ref

def apariecia_personaje_aleatorio():
    valor1 = RANDOM_CHAR_APPEARANCE[randint(0,len(RANDOM_CHAR_APPEARANCE)-1)]
    valor2 = RANDOM_CHAR_APPEARANCE[randint(0,len(RANDOM_CHAR_APPEARANCE)-1)]

    return (valor1,valor2)

def personalidad_personaje_aleatorio():
    valor1 = RANDOM_CHAR_PERSONALITY[randint(0,len(RANDOM_CHAR_PERSONALITY)-1)]
    valor2 = RANDOM_CHAR_PERSONALITY[randint(0,len(RANDOM_CHAR_PERSONALITY)-1)]

    return (valor1,valor2)

def descripcion_personaje_aleatorio():
    valor1 = RANDOM_CHAR_DESCRIPTOR[randint(0,len(RANDOM_CHAR_DESCRIPTOR)-1)]
    valor2 = RANDOM_CHAR_DESCRIPTOR[randint(0,len(RANDOM_CHAR_DESCRIPTOR)-1)]

    return (valor1,valor2)

# Ejecución pruebas
if __name__== "__main__":
    #letra_aleatoria()
    """
    a = apariecia_personaje_aleatorio()
    print(f"{a[0]}, {a[1]}")
    p = personalidad_personaje_aleatorio()
    print(f"{p[0]}, {p[1]}")
    d = descripcion_personaje_aleatorio()
    print(f"{d[0]}, {d[1]}")
    """
    pass