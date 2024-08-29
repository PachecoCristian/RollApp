import customtkinter as ctk

from configuracion import *
from componentes import *

from DyD_code import *


class Ventana_Puntos_Vida(Frame_Ventana):
    def __init__(ventana, master, theme):
        super().__init__(master= master, theme=theme)
        # Crear la (Sub-ventana)
        frame = Frame_Ventana(ventana, theme)
        frame.colocar()

        # Colores
        ventana.theme= theme

        # Datos
        ventana.texto = ctk.StringVar()
        ventana.mod_con= ctk.StringVar()
        ventana.mod_lv= ctk.StringVar()
        ventana.mod_static= ctk.StringVar()
        ventana.tipo= ctk.StringVar(value=VALORES_HIT_DICE[1])

        # Crear Frame para la clases
        ventana.clases = Div(frame)
        ventana.clases.pack()
        ventana.crear_clase()
        # Crear Frame para opciones Generales
        ventana.opciones = Div(frame)
        ventana.opciones.pack()

        frame1 = Div(ventana.opciones)
        frame1.pack(side="left", padx=10, pady=5)
        Texto(frame1, text="Mod Constitución").pack()
        Entrada(frame1, variable= ventana.mod_con).pack()
        frame2 = Div(ventana.opciones)
        frame2.pack(side="left", padx=10)
        Texto(frame2, text="Mod Vida por Nivel").pack()
        Entrada(frame2, variable= ventana.mod_lv).pack()
        frame3 = Div(ventana.opciones)
        frame3.pack(side="left", padx=10)
        Texto(frame3, text="Mod Vida").pack()
        Entrada(frame3, variable= ventana.mod_static).pack()
        frame4 = Div(frame)
        frame4.pack(pady=10)
        Texto(frame4, text="Valor HD").pack()
        DropDown(frame4, VALORES_HIT_DICE, theme, ventana.tipo).pack()

        # Crear Frame para los botones
        ventana.botones = Div(frame)
        ventana.botones.pack()
        # Crear los botones
        Boton(ventana.botones, text= "Añadir Sub-Clase", command= ventana.crear_clase, theme= ventana.theme).pack(side="left", padx=10)
        Boton(ventana.botones, text= "Calcular Vida", command= ventana.calcular_vida, theme= ventana.theme).pack(side="left", padx=10)
        Boton(ventana.botones, text= "Borrar", command= ventana.borrar, theme= ventana.theme).pack(side="left", padx=10)
        # Crear Texto
        Texto(frame, variable=ventana.texto).pack()

    def crear_clase(ventana):
        frame_clase = ctk.CTkFrame(ventana.clases, fg_color="transparent", border_width=3)
        frame_clase.pack(pady=5, ipadx=5, ipady=5)

        frame1 = Div(frame_clase)
        frame1.pack()
        # Crear lista de Clases (Añadiendo personalizada)
        clases = ["Personalizado"]
        clases+= (list(DYD_HIT_DICE))
        ComboBox(frame1, clases, ventana.theme).pack(side="left", padx=10)
        # Crear Espacio para el Hit Dice
        Texto(frame1, text="Hit Dice").pack(side="left", padx=5)
        Entrada(frame1).pack(side="left")

        frame2 = Div(frame_clase)
        frame2.pack()
        # Crear Espacio Numero de niveles
        Texto(frame2, text="Niveles").pack(side="left", padx=5)
        Entrada(frame2).pack(side="left")
        # Crear Espacio para el Modificador de Vida
        Texto(frame2, text="Mod Vida por nivel").pack(side="left", padx=5)
        Entrada(frame2).pack(side="left")

    def calcular_vida(ventana):
        clases = []

        regex_frame = compile('.*frame.*',dot)
        regex_div= compile('.*div.*',dot)
        regex_optionmenu = compile('.*combobox.*',dot)
        regex_entry = compile('.*entrada.*',dot)
        # Obtener los valores de las difentes clases
        for i1 in ventana.clases.children:
            if regex_frame.match(i1) != None:
                clase= []
                for i2 in ventana.clases.children[i1].children:
                    if regex_div.match(i2) != None:
                        for i3 in ventana.clases.children[i1].children[i2].children:
                            if regex_entry.match(i3) != None or regex_optionmenu.match(i3)!= None:
                                componente= ventana.clases.children[i1].children[i2].children[i3]
                                clase.append(componente.get())
                clases.append(clase)
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

class Ventana_Speed(Frame_Ventana):
    def __init__(ventana, master, theme):
        super().__init__(master= master, theme=theme)
        # Crear la (Sub-ventana)
        frame = Frame_Ventana(ventana, theme)
        frame.colocar()

        # Colores
        ventana.theme= theme

        # Datos
        ventana.speed = ctk.StringVar()
        ventana.feets_minute = ctk.StringVar()
        ventana.miles_hour = ctk.StringVar()
        ventana.miles_day_8 = ctk.StringVar()
        ventana.miles_day_24 = ctk.StringVar()

        # Tabla 
        ventana.tabla = Div(frame)
        ventana.tabla.columnconfigure([0], weight=2)
        ventana.tabla.columnconfigure([1,2,3,4,5], weight=1, uniform="a")
        ventana.tabla.rowconfigure([0,1,2,3,4,5], weight=1, uniform="a") 
        ventana.tabla.rowconfigure(6, weight=2) 
        ventana.tabla.pack()

        # Cabecera
        ventana.texto_tabla("",0,0)
        ventana.texto_tabla("Speed",0,1)
        ventana.texto_tabla("Feet\nPer Minute",0,2)
        ventana.texto_tabla("Miles\nper Hour",0,3)
        ventana.texto_tabla("Miles\nper Day (8)",0,4)
        ventana.texto_tabla("Miles\nper Day (24)",0,5)

        # Filas Estatica
        ventana.texto_tabla("Crawl (Travel)",1,0)
        ventana.texto_tabla("5",1,1)
        ventana.texto_tabla("50",1,2)
        ventana.texto_tabla("0.6",1,3)
        ventana.texto_tabla("4.5",1,4)
        ventana.texto_tabla("13.6",1,5)

        ventana.texto_tabla("Slow Travel",2,0)
        ventana.texto_tabla("20",2,1)
        ventana.texto_tabla("200",2,2)
        ventana.texto_tabla("2.3",2,3)
        ventana.texto_tabla("18.2",2,4)
        ventana.texto_tabla("54.6",2,5)

        ventana.texto_tabla("Normal Travel",3,0)
        ventana.texto_tabla("30",3,1)
        ventana.texto_tabla("300",3,2)
        ventana.texto_tabla("3.4",3,3)
        ventana.texto_tabla("27.3",3,4)
        ventana.texto_tabla("81.8",3,5)

        ventana.texto_tabla("Fast Travel",4,0)
        ventana.texto_tabla("40",4,1)
        ventana.texto_tabla("400",4,2)
        ventana.texto_tabla("4.6",4,3)
        ventana.texto_tabla("36.4",4,4)
        ventana.texto_tabla("109.1",4,5)

        ventana.texto_tabla("Gallop",5,0)
        ventana.texto_tabla("80",5,1)
        ventana.texto_tabla("800",5,2)
        ventana.texto_tabla("9.1",5,3)
        ventana.texto_tabla("---",5,4)
        ventana.texto_tabla("---",5,5)

        # Fila dinamica
        ventana.texto_tabla("Custom",6,0)

        cell1= Div(ventana.tabla)
        cell1.grid(row=6, column=1, sticky="nsew")
        ventana.e1= Entrada(cell1, ventana.speed)
        ventana.e1.configure(width=75)
        ventana.e1.bind('<Return>', lambda args: ventana.calcular_speeds(1))
        ventana.e1.pack()
        
        cell2= Div(ventana.tabla)
        cell2.grid(row=6, column=2, sticky="nsew")
        ventana.e2= Entrada(cell2, ventana.feets_minute)
        ventana.e2.configure(width=75)
        ventana.e2.bind('<Return>', lambda args: ventana.calcular_speeds(2))
        ventana.e2.pack()
        
        cell3= Div(ventana.tabla)
        cell3.grid(row=6, column=3, sticky="nsew")
        ventana.e3= Entrada(cell3, ventana.miles_hour)
        ventana.e3.configure(width=75)
        ventana.e3.bind('<Return>', lambda args: ventana.calcular_speeds(3))
        ventana.e3.pack()
        
        cell4= Div(ventana.tabla)
        cell4.grid(row=6, column=4, sticky="nsew")
        ventana.e4= Entrada(cell4, ventana.miles_day_8)
        ventana.e4.configure(width=75)
        ventana.e4.bind('<Return>', lambda args: ventana.calcular_speeds(4))
        ventana.e4.pack()
        
        cell5= Div(ventana.tabla)
        cell5.grid(row=6, column=5, sticky="nsew")
        ventana.e5= Entrada(cell5, ventana.miles_day_24)
        ventana.e5.configure(width=75)
        ventana.e5.bind('<Return>', lambda args: ventana.calcular_speeds(5))
        ventana.e5.pack()
        

    
    def texto_tabla(ventana, texto, fila, columna):
        div = Div(ventana.tabla)
        Texto(div,texto).pack()
        div.grid(row=fila, column=columna, sticky="nsew")
        return div
    
    def calcular_speeds(ventana, columna):
        match columna:
            case 1:
                velocidad = float(ventana.speed.get())
                speed, feets_minute, miles_hour, miles_day_8, miles_day_24 = calcula_speed(velocidad,1)
            case 2:
                velocidad = float(ventana.feets_minute.get())
                speed, feets_minute, miles_hour, miles_day_8, miles_day_24 = calcula_speed(velocidad,2)
            case 3:
                velocidad = float(ventana.miles_hour.get())
                speed, feets_minute, miles_hour, miles_day_8, miles_day_24 = calcula_speed(velocidad,3)
            case 4:
                velocidad = float(ventana.miles_day_8.get())
                speed, feets_minute, miles_hour, miles_day_8, miles_day_24 = calcula_speed(velocidad,4)
            case 5:
                velocidad = float(ventana.miles_day_24.get())
                speed, feets_minute, miles_hour, miles_day_8, miles_day_24 = calcula_speed(velocidad,5)
        
        ventana.speed.set(round(speed,1))
        ventana.feets_minute.set(round(feets_minute,1))
        ventana.miles_hour.set(round(miles_hour,1))
        ventana.miles_day_8.set(round(miles_day_8,1))
        ventana.miles_day_24.set(round(miles_day_24,1))
