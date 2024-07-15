import customtkinter as ctk
from configuracion import *
from DyD_code import *

class Ventana_Puntos_Vida(ctk.CTkFrame):
    def __init__(ventana, master):
        super().__init__(master= master)

        # Crear la (Sub-ventana)
        frame = ctk.CTkFrame(ventana)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        # Datos
        ventana.texto = ctk.StringVar()
        ventana.mod_con= ctk.StringVar()
        ventana.mod_lv= ctk.StringVar()
        ventana.mod_static= ctk.StringVar()
        ventana.tipo= ctk.StringVar(value=VALORES_HIT_DICE[1])

        # Crear Frame para la clases
        ventana.clases = ctk.CTkFrame(frame, fg_color="transparent")
        ventana.clases.pack()
        ventana.crear_clase()
        # Crear Frame para opciones Generales
        ventana.opciones = ctk.CTkFrame(frame, fg_color="transparent")
        ventana.opciones.pack()

        frame1= ctk.CTkFrame(ventana.opciones, fg_color="transparent")
        frame1.pack(side="left", padx=10, pady=5)
        ctk.CTkLabel(frame1, text="Mod Constitución").pack()
        ctk.CTkEntry(frame1, textvariable= ventana.mod_con).pack()
        frame2= ctk.CTkFrame(ventana.opciones, fg_color="transparent")
        frame2.pack(side="left", padx=10)
        ctk.CTkLabel(frame2, text="Mod Vida por Nivel").pack()
        ctk.CTkEntry(frame2, textvariable= ventana.mod_lv).pack()
        frame3= ctk.CTkFrame(ventana.opciones, fg_color="transparent")
        frame3.pack(side="left", padx=10)
        ctk.CTkLabel(frame3, text="Mod Vida").pack()
        ctk.CTkEntry(frame3, textvariable= ventana.mod_static).pack()
        frame4= ctk.CTkFrame(ventana.opciones, fg_color="transparent")
        frame4.pack(side="left", padx=10)
        ctk.CTkLabel(frame4, text="Valor HD").pack()
        ctk.CTkOptionMenu(frame4,values=VALORES_HIT_DICE, variable= ventana.tipo).pack()

        # Crear Frame para los botones
        ventana.botones = ctk.CTkFrame(frame, fg_color="transparent")
        ventana.botones.pack()
        # Crear los botones
        ctk.CTkButton(ventana.botones, text= "Añadir Sub-Clase", command= ventana.crear_clase).pack(side="left", padx=10)
        ctk.CTkButton(ventana.botones, text= "Calcular Vida", command= ventana.calcular_vida).pack(side="left", padx=10)
        ctk.CTkButton(ventana.botones, text= "Borrar", command= ventana.borrar).pack(side="left", padx=10)
        # Crear Texto
        ctk.CTkLabel(frame, textvariable=ventana.texto).pack()

    def crear_clase(ventana):
        frame_clase = ctk.CTkFrame(ventana.clases, fg_color="transparent", border_width=3)
        frame_clase.pack(pady=5, ipadx=5, ipady=5)

        frame1 = ctk.CTkFrame(frame_clase, fg_color="transparent")
        frame1.pack()
        # Crear lista de Clases (Añadiendo personalizada)
        clases = ["Personalizado"]
        clases+= (list(DYD_HIT_DICE))
        ctk.CTkOptionMenu(frame1,values=clases).pack(side="left", padx=10)
        # Crear Espacio para el Hit Dice
        ctk.CTkLabel(frame1, text="Hit Dice").pack(side="left", padx=5)
        ctk.CTkEntry(frame1).pack(side="left")

        frame2 = ctk.CTkFrame(frame_clase, fg_color="transparent")
        frame2.pack()
        # Crear Espacio Numero de niveles
        ctk.CTkLabel(frame2, text="Niveles").pack(side="left", padx=5)
        ctk.CTkEntry(frame2).pack(side="left")
        # Crear Espacio para el Modificador de Vida
        ctk.CTkLabel(frame2, text="Mod Vida por nivel").pack(side="left", padx=5)
        ctk.CTkEntry(frame2).pack(side="left")

    def calcular_vida(ventana):
        clases = []

        regex_frame = compile('.*frame.*',dot)
        regex_optionmenu = compile('.*optionmenu.*',dot)
        regex_entry = compile('.*entry.*',dot)
        # Obtener los valores de las difentes clases
        for i1 in ventana.clases.children:
            if regex_frame.match(i1) != None:
                clase= []
                for i2 in ventana.clases.children[i1].children:
                    if regex_frame.match(i2) != None:
                        for i3 in ventana.clases.children[i1].children[i2].children:
                            if regex_entry.match(i3) != None or regex_optionmenu.match(i3):
                                clase.append(ventana.clases.children[i1].children[i2].children[i3].get())
                clases.append(clase)
        #print(clases)
        mod_con= 0
        mod_nivel= 0
        mod_estatico= 0
        try:
            for i in range( len(clases)):
                clases[i][1] = clases[i][1] if clases[i][1] != "" else "d0"
                clases[i][2] = int(clases[i][2]) if clases[i][2] != "" else 0
                clases[i][3] = int(clases[i][3]) if clases[i][3] != "" else 0

            mod_con= int(ventana.mod_con.get()) if ventana.mod_con.get()!="" else 0
            mod_nivel= int(ventana.mod_lv.get()) if ventana.mod_lv.get()!="" else 0
            mod_estatico= int(ventana.mod_static.get()) if ventana.mod_static.get()!="" else 0 
        except:
            ventana.texto.set("Los valores deben ser numeros")
        tipo= ventana.tipo.get()

        # clases [['Fighter', 0, 5, 0]]
        # clase [( Nombre Clase, Dado de Golpe, nº Niveles, Mod_lv)]
        hp= calcula_multiclase(clases, mod_con, mod_nivel, mod_estatico, tipo)
        ventana.texto.set(f"Vida = {hp}")

    def borrar(ventana):
        # Borrar clases
        elementos= list(ventana.clases.children)
        for i in elementos:
            ventana.clases.children[i].destroy()
        ventana.crear_clase()
        # Borrar los valores
        ventana.texto.set("")
        ventana.mod_con.set("")
        ventana.mod_lv.set("")
        ventana.mod_static.set("")