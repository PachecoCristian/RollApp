from configuracion import *

from fractions import Fraction
import json
import os
      
# Modulos / Metodos
def expode_prob(valor, dado):

    """ 
    (8,4): 3/4 + (1/4 * 3/4) = 3/4 + 3/16 = 12/16 +3/16 = 15/16
    (12,4): 3/4 + (1/4 * 3/4) + ([1/4*1/4] * 3/4) = 3/4 + 3/16 + (1/16 * 3/4)= 
    (8,6): 5/6 + (1/6 x* 1/6) = 5/6 + 1/36 = 30/36 + 1/36 = 31/36 = 
    """    
    div,resto= divmod(valor, dado)

    # Posibilidades de fallar Como Texto
    """ 
    resultado= ""
    if div <= 0:
        resultado+= str(Fraction(1-(resto/dado)))
    else : 
        i=0
        while i <= div:
            n_rep= i+1
            if i!= 0:
                resultado += " + "
            if i == div:
                if resto != 0:
                    resultado += f"{(resto-1)}/{(dado**n_rep)}"
                else:
                    resultado += "0"
            else:
                resultado += f"{dado-1}/{(dado**n_rep)}"
            i+=1 
    print(resultado) 
    """
    # Posibilidad de fallar
    fallo=0
    if div <= 0:
        fallo+= ((resto-1)/dado)
    else : 
        i=0
        while i <= div:
            n_rep= i+1
            if i == div:
                if resto != 0:
                    fallo += (resto-1)/(dado**n_rep)
            else:
                fallo += (dado-1)/(dado**n_rep)
            i+=1 

    # Las posibilidades de fallar son inversamente proporcionales a las de acertar
    return (1 - fallo)

def abrir_ficha(ruta):
    es_comodin= False
    # Abrir fichero
    try:
        fichero = open(ruta, encoding="utf8")
    except:
        raise Exception("Ruta de archivo incorrecta")
    # Convertir el fichero en json
    try:
        fichero = json.load(fichero)
    except:
        raise Exception("El archivo no es un JSON") 
   
    # Ver si es ficha de personaje
    if fichero["_stats"]["systemId"] != "swade":
        raise Exception("El archivo no es una ficha de personaje de Swade") 
    
    # Ver si es personaje con dado salvaje
    if fichero["type"] == "character" or (fichero["type"]== "npc" and fichero["system"]["wildcard"]):
        es_comodin= True
    
    return (fichero, es_comodin)
   

def cambiar_dados(ficha):
    # Datos
    datos={
    "agility": [0,0],
    "smarts": [0,0],
    "spirit": [0,0],
    "strength": [0,0],
    "vigor": [0,0]
    }
    datos["agility"][0]= ficha["system"]["attributes"]["agility"]["die"]["sides"]
    datos["agility"][1]= ficha["system"]["attributes"]["agility"]["die"]["modifier"]
    datos["smarts"][0]= ficha["system"]["attributes"]["smarts"]["die"]["sides"]
    datos["smarts"][1]= ficha["system"]["attributes"]["smarts"]["die"]["modifier"]
    datos["spirit"][0]= ficha["system"]["attributes"]["spirit"]["die"]["sides"]
    datos["spirit"][1]= ficha["system"]["attributes"]["spirit"]["die"]["modifier"]
    datos["strength"][0]= ficha["system"]["attributes"]["strength"]["die"]["sides"]
    datos["strength"][1]= ficha["system"]["attributes"]["strength"]["die"]["modifier"]
    datos["vigor"][0]= ficha["system"]["attributes"]["vigor"]["die"]["sides"]
    datos["vigor"][1]= ficha["system"]["attributes"]["vigor"]["die"]["modifier"]

    # Recorrer todos los "Objetos" de la ficha, selecionar las Habilidades, y cambiar el valor
    for i in ficha["items"]:
        if i["type"] == "skill": 
            try:
                i["system"]["wild-die"]["sides"] = datos[i["system"]["attribute"]][0]
            except:
                i["system"]["wild-die"]["sides"] = 6

    return ficha

def guardar_ficha(ficha, ruta):
    ruta_resultado= f"{ruta}\\{ficha["name"]}(Dados).json"
    ruta_resultado = os.path.abspath(ruta_resultado)
    with open(ruta_resultado,"w", encoding='utf-8') as f:
        json.dump(ficha, f, ensure_ascii=False, indent=4)

    # resultado
    return f"✅ {ruta_resultado} Completado correctamente"

    

# Ejecución pruebas
if __name__== "__main__":
    """     
    #expode_prob(4,8)       # OK: 1/2
            # OK: 1/2
        #print(expode_prob(4,8).as_integer_ratio())     # OK: 1/2
    #expode_prob(2,8)       # OK: 1/4
            # OK: 1/4
        #print(expode_prob(2,8).as_integer_ratio())     # OK: 3/4

    #expode_prob(8,4)       # OK: 3/4 + 3/16 + 0        
            # OK: 15/16
        #print(expode_prob(8,4).as_integer_ratio())     # OK: 1/16
    print (str(Fraction(3/4 + 3/16 + 3/64 + 2/256)))
    #expode_prob(15,4)      # OK: 3/4 + 3/16 + 3/64 + 2/256
            # OK: 127/128
        #print(expode_prob(15,4).as_integer_ratio())    # OK: 1/128
    
    #expode_prob(8,6)       # OK: 5/6 + 1/36
            # ¿OK?: 1939049839562297 / 2251799813685248
        #print(expode_prob(8,6).as_integer_ratio())     # ¿OK?: 312749974122951 / 2251799813685248
    #expode_prob(9,6)       # OK: 5/6 + 2/36 = 30/36 + 2/36
            # ¿OK?: 8006399337547549/ 9007199254740992
        #print(expode_prob(9,6).as_integer_ratio())     # ¿OK?: 1000799917193443 / 9007199254740992 
    """
pass

