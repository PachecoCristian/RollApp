from configuracion import *

from re import compile, S as dot

def calcula_hp(dado, nivel, mod_con, mod_nivel, inicial=True, tipo=None):
    hp= 0
    for i in range(nivel):
        if i == 0 and inicial :
            hp+= dado 
        else:

            match tipo:
                case "Maximo":
                    hp+= dado
                case "Minimo":
                    hp+= 1
                case _:
                    hp+= (dado/2)+1
        hp+= + mod_con + mod_nivel

    return int(hp)

def calcula_multiclase(niveles, mod_con, mod_nivel, mod_estatico, tipo=None):
    # clase [( Nombre Clase, Dado de Golpe, nº Niveles, Mod_lv)]
    hp= 0
    hd_clases= DYD_HIT_DICE
    for clase in niveles:
        if clase[0] in hd_clases:
            hit_dice= int(hd_clases[clase[0]].replace("d",""))
        else:
            hit_dice= int(clase[1].replace("d",""))

        nivel_clase= clase[2]
        total_mod_nivel= mod_nivel + clase[3]
         
        if clase[0] == (niveles)[0][0]:
            hp +=  calcula_hp(dado=hit_dice, nivel=nivel_clase, mod_con=mod_con, mod_nivel=total_mod_nivel, inicial=True, tipo=tipo)
        else:
            hp +=  calcula_hp(dado=hit_dice, nivel=nivel_clase, mod_con=mod_con, mod_nivel=total_mod_nivel, inicial=False, tipo=tipo)

    hp += int(mod_estatico)
    return hp

if __name__== "__main__":
    # Pruebas
    #print(calcula_hp(dado=10, nivel=6, mod_con=2, mod_nivel=0, mod_estatico=0, inicial= False))
    #niveles= [(5,"Fighter"),(3,"Cleric")]
    #print(calcula_multiclase(niveles, mod_con=2, mod_nivel=0, mod_estatico=0))
    pass