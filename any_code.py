import customtkinter as ctk
from configuracion import *

from random import randint
from re import compile, match, S as dot

class Ventana_Nombre(ctk.CTkFrame):
    def __init__(ventana, master):
        super().__init__(master= master)

        # Crear la (Sub-ventana)
        frame = ctk.CTkFrame(ventana)
        frame.place(relx=0.5, rely=0.5, anchor="center")
        # Datos
        ventana.nombre = ctk.StringVar(value="")
        ventana.opciones = ctk.StringVar(value="")
        # Componentes
        # Textos
        textos = ctk.CTkFrame(frame, fg_color="transparent")
        textos.pack(fill="x")
        ctk.CTkLabel(textos, textvariable= ventana.nombre,font=ctk.CTkFont(size=20)).pack(fill="x")
        ctk.CTkLabel(textos, textvariable= ventana.opciones).pack(fill="x")
        # Botones
        ventana.botones = ctk.CTkFrame(frame, fg_color="transparent")
        ventana.botones.pack()
        ctk.CTkButton(ventana.botones, text= "Nombre", command= ventana.nombre_aleatorio).pack()
    
    def nombre_aleatorio(ventana):
        ventana.opciones.set("")
        ventana.nombre.set("")
        for i in range(2):
            ventana.nueva_letra()

        ventana.cambiar_botones()
    
    def nueva_letra(ventana):
        letra, opcion = letra_aleatoria()
        if opcion!= None :
            # Compobar si hay Letras
            if ventana.nombre.get() == "":
                ventana.nombre.set(f'{letra}') 
            else:
                ventana.nombre.set(f'{ventana.nombre.get()} - {letra}') 
            # Compobar si hay Opciones
            if ventana.opciones.get() =="":
                ventana.opciones.set(f"({opcion})")
            else:
                ventana.opciones.set(f"{ventana.opciones.get()} - ({opcion})")
            
        else:
            if ventana.nombre.get() == "":
                ventana.nombre.set(f'"{letra}"') 
            else:
                ventana.nombre.set(f'{ventana.nombre.get()} - "{letra}"') 

    def borrar(ventana):
        # Datos
        ventana.nombre.set("")
        ventana.opciones.set("")

        ventana.elimina_botones()
        ctk.CTkButton(ventana.botones, text= "Nombre", command= ventana.nombre_aleatorio).pack()
    
    # Funciones Visuales
    def cambiar_botones(ventana):
        ventana.elimina_botones()

        ctk.CTkButton(ventana.botones, text= "Nueva Letra", command= ventana.nueva_letra).pack(side="left")
        ctk.CTkButton(ventana.botones, text= "Borrar", command= ventana.borrar).pack(side="left")
    
    def elimina_botones(ventana):
        regex = compile('.*button.*',dot)
        for i in ventana.botones.children :
            if regex.match(i) != None:
                ventana.botones.children[i].pack_forget()

class Ventana_Lugar(ctk.CTkFrame):
    def __init__(ventana, master):
        super().__init__(master= master)

        # Crear la (Sub-ventana)
        frame = ctk.CTkFrame(ventana)
        frame.place(relx=0.5, rely=0.5, anchor="center")
        # Datos
        ventana.nombre = ctk.StringVar(value="")
        # Componentes
        ctk.CTkButton(frame, text= "Lugar", command= ventana.nombre_lugar).pack()
        ctk.CTkLabel(frame, textvariable= ventana.nombre, font=ctk.CTkFont(size=20)).pack(fill="x")

    def nombre_lugar(ventana):
        nombre= RANDOM_PLACES_NAME[randint(0,len(RANDOM_PLACES_NAME)-1)]

        reg_ex_P= compile(r".*\[Place\].*",dot)     
        if reg_ex_P.match(nombre) != None:
            nombre= nombre.replace("[Place]",f"[{RANDOM_PLACES_ADJ[randint(0,len(RANDOM_PLACES_ADJ)-1)][0]}]")
        reg_ex_A= compile(r".*\[Adjective\].*",dot)
        if reg_ex_A.match(nombre) != None:
            nombre= nombre.replace("[Adjective]",f"[{RANDOM_PLACES_ADJ[randint(0,len(RANDOM_PLACES_ADJ)-1)][1]}]")
        reg_ex_N= compile(r".*\[Noun\].*",dot)
        if reg_ex_N.match(nombre) != None:
            nombre= nombre.replace("[Noun]",f"[{RANDOM_PLACES_ADJ[randint(0,len(RANDOM_PLACES_ADJ)-1)][2]}]")
        
        ventana.nombre.set(f"Nombre: {nombre}")
       

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


if __name__== "__main__":
    #letra_aleatoria()
    pass