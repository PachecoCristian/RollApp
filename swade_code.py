from fractions import Fraction

def expode_prob(valor, dado):

    """ 
    (8,4): 3/4 + (1/4 * 3/4) = 3/4 + 3/16 = 12/16 +3/16 = 15/16
    (12,4): 3/4 + (1/4 * 3/4) + ([1/4*1/4] * 3/4) = 3/4 + 3/16 + (1/16 * 3/4)= 
    (8,6): 5/6 + (1/6 x* 1/6) = 5/6 + 1/36 = 30/36 + 1/36 = 31/36 = 
    """    
    div,resto= divmod(valor, dado)
    resultado= ""

    # Posibilidades de fallar Como Texto
    """ 
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
        fallo+= (resto/dado)
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

