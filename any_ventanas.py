import customtkinter as ctk

from configuracion import *
from componentes import *

from any_code import *

# Ventanas de Aplicaciones
class Ventana_Nombre(Frame_Ventana):
    def __init__(ventana, master, theme):
        super().__init__(master= master, theme=theme)
        # Crear la (Sub-ventana)
        frame = Frame_Ventana(ventana, theme)
        frame.colocar()

        # Colores
        ventana.theme= theme

        # Datos
        ventana.nombre = ctk.StringVar(value="")
        ventana.opciones = ctk.StringVar(value="")
        # Componentes
        # Textos
        textos = Div(frame)
        textos.pack(fill="x", padx=10, pady=5)
        Texto(textos, variable= ventana.nombre, font=ctk.CTkFont(size=20)).pack(fill="x")
        Texto(textos, variable= ventana.opciones).pack(fill="x")
        # Botones
        ventana.botones = Div(frame)
        ventana.botones.pack(padx=10, pady=5)
        Boton(ventana.botones, text= "Nombre", command= ventana.nombre_aleatorio, theme= ventana.theme).pack()
    
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
        Boton(ventana.botones, text= "Nombre", command= ventana.nombre_aleatorio, theme= ventana.theme).pack()
    
    # Funciones Visuales
    def cambiar_botones(ventana):
        ventana.elimina_botones()

        Boton(ventana.botones, text= "Nueva Letra", command= ventana.nueva_letra, theme= ventana.theme).pack(side="left", padx=10, pady=5)
        Boton(ventana.botones, text= "Borrar", command= ventana.borrar, theme= ventana.theme).pack(side="left", padx=10, pady=5)
    
    def elimina_botones(ventana):
        regex = compile('.*boton.*',dot)
        elementos= list(ventana.botones.children)
        for i in elementos :
            if regex.match(i) != None:
                ventana.botones.children[i].destroy()

class Ventana_Lugar(Frame_Ventana):
    def __init__(ventana, master, theme):
        super().__init__(master= master, theme=theme)
        # Crear la (Sub-ventana)
        ventana.frame = Frame_Ventana(ventana, theme)
        ventana.frame.colocar()

        # Colores
        ventana.theme= theme
        
        # Datos
        ventana.nombre = ctk.StringVar(value="")
        ventana.nombre_ref = ""
        ventana.descripcion_1 = ctk.StringVar(value="")
        ventana.descripcion_2 = ctk.StringVar(value="")
        # Componentes
        Texto(ventana.frame, variable= ventana.nombre, font=ctk.CTkFont(size=20)).pack(fill="x", padx=10, pady=5)
        Texto(ventana.frame, variable= ventana.descripcion_1).pack(fill="x", padx=10, pady=5)
        Texto(ventana.frame, variable= ventana.descripcion_2).pack(fill="x", padx=10, pady=5)
        
        Boton(ventana.frame, text= "Lugar", command= ventana.lugar_aleatorio, theme=ventana.theme).pack(padx=10, pady=5)

    def lugar_aleatorio(ventana):
        # Datos
        nombre= nombre_lugar_aleatorio()
        nombre, ref = adjetivos_lugar_aleatorio(nombre)
        ventana.nombre.set(f"Nombre: {nombre}")
        ventana.nombre_ref = ref
        desc_1 = descripción_lugar()
        ventana.descripcion_1.set(f'Descripción: "{desc_1[0]}" - "{desc_1[1]}"')
        desc_2 = descripción_aleatoria()
        ventana.descripcion_2.set(f'Descripción: "{desc_2[0]}" - "{desc_2[1]}"')
        # Componentes
        ventana.elimina_botones()
        Boton(ventana.frame, text= "Cambiar Adjetivos", command= ventana.cambiar_adj, theme=ventana.theme).pack(padx=10, pady=5)
        Boton(ventana.frame, text= "Cambiar Descripciones", command= ventana.cambiar_des, theme=ventana.theme).pack(padx=10, pady=5)
        Boton(ventana.frame, text= "Borrar", command= ventana.borrar, theme=ventana.theme).pack(padx=10, pady=5)

    def cambiar_adj(ventana):
        # Datos
        nombre, ref = adjetivos_lugar_aleatorio(ventana.nombre_ref)
        ventana.nombre.set(f"Nombre: {nombre}")
        ventana.nombre_ref = ref

    def cambiar_des(ventana):
        # Datos
        desc_1 = descripción_lugar()
        ventana.descripcion_1.set(f'Descripción: "{desc_1[0]}" - "{desc_1[1]}"')
        desc_2 = descripción_aleatoria()
        ventana.descripcion_2.set(f'Descripción: "{desc_2[0]}" - "{desc_2[1]}"')

    def borrar(ventana):
        # Datos
        ventana.nombre.set(value="")
        ventana.nombre_ref = ""
        ventana.descripcion_1.set(value="")
        ventana.descripcion_2.set(value="")
        # Componentes
        ventana.elimina_botones()
        Boton(ventana.frame, text= "Lugar", command= ventana.lugar_aleatorio, theme=ventana.theme).pack(padx=10, pady=5)

    # Funciones visuales
    def elimina_botones(ventana):
        regex = compile(r'.*boton.*',dot)
        elementos= list(ventana.frame.children)
        for i in elementos :
            if regex.match(i) != None:
                ventana.frame.children[i].destroy()

class Ventana_Personaje(Frame_Ventana):
    def __init__(ventana, master, theme):
        super().__init__(master= master, theme=theme)
        # Crear la (Sub-ventana)
        ventana.frame = Frame_Ventana(ventana, theme)
        ventana.frame.colocar()
        
        # Colores
        ventana.theme= theme

        # Datos
        ventana.nombre = ctk.StringVar(value="")
        ventana.opciones = ctk.StringVar(value="")
        ventana.apariecia = ctk.StringVar(value="")
        ventana.personalidad = ctk.StringVar(value="")
        ventana.descripcion = ctk.StringVar(value="")
        # Componentes
        Texto(ventana.frame, variable= ventana.nombre, font=ctk.CTkFont(size=20)).pack(fill="x", padx=10, pady=5)
        Texto(ventana.frame, variable= ventana.opciones, font=ctk.CTkFont(size=10)).pack(fill="x")
        Texto(ventana.frame, variable= ventana.apariecia).pack(fill="x", padx=10, pady=5)
        Texto(ventana.frame, variable= ventana.personalidad).pack(fill="x", padx=10, pady=5)
        Texto(ventana.frame, variable= ventana.descripcion).pack(fill="x", padx=10, pady=5)
        
        ventana.botones= Div(ventana.frame)
        ventana.botones.columnconfigure((0,1), weight=1)
        ventana.botones.rowconfigure((0,1,2), weight=1)
        ventana.botones.pack(fill="x")
        Boton(ventana.botones, text= "Personaje", command= ventana.npc_aleatorio, theme= ventana.theme).grid(column=0, columnspan=2, row=1, padx=10, pady=5)

    def npc_aleatorio(ventana):

        ventana.cambiar_nombre()
        ventana.cambiar_apear()
        ventana.cambiar_perso()
        ventana.cambiar_des()

        # Componentes
        ventana.elimina_botones()
        Boton(ventana.botones, text= "Cambiar Nombre", command= ventana.cambiar_nombre, theme= ventana.theme).grid(column=0, row=0, padx=10, pady=5)
        Boton(ventana.botones, text= "Cambiar Apariencia", command= ventana.cambiar_apear, theme= ventana.theme).grid(column=1, row=0, padx=10, pady=5)
        Boton(ventana.botones, text= "Cambiar Personalidad", command= ventana.cambiar_perso, theme= ventana.theme).grid(column=0, row=1, padx=10, pady=5)
        Boton(ventana.botones, text= "Cambiar Descripción", command= ventana.cambiar_des, theme= ventana.theme).grid(column=1, row=1, padx=10, pady=5)
        Boton(ventana.botones, text= "Borrar", command= ventana.borrar, theme= ventana.theme).grid(column=0,columnspan=2, row=2, padx=10, pady=5)

    def cambiar_nombre(ventana):
        nombre = ""
        opciones= ""
        for i in range(2):
            letra = letra_aleatoria()
            if i == 0:
                nombre = f'"{letra[0]}"'
                opciones = f"({letra[1]})" if letra[1] != None else ""
            else:
                nombre += f' - "{letra[0]}"'
                if opciones != "":
                    opciones += f" - ({letra[1]})" if letra[1] != None else ""
                else:
                    opciones += f"({letra[1]})" if letra[1] != None else ""

        ventana.nombre.set(f"Nombre: {nombre}")
        ventana.opciones.set(opciones)

    def cambiar_apear(ventana):
        apariecia = apariecia_personaje_aleatorio()
        ventana.apariecia.set(f'Apariencia: "{apariecia[0]}" - "{apariecia[1]}"')

    def cambiar_perso(ventana):
        personalidad = personalidad_personaje_aleatorio()
        ventana.personalidad.set(f'Personalidad: "{personalidad[0]}" - "{personalidad[1]}"')

    def cambiar_des(ventana):
        descripcion = descripcion_personaje_aleatorio()
        ventana.descripcion.set(f'Descripción: "{descripcion[0]}" - "{descripcion[1]}"')

    def borrar(ventana):
        # Datos
        ventana.nombre.set(value="")
        ventana.opciones.set(value="")
        ventana.apariecia.set(value="")
        ventana.personalidad.set(value="")
        ventana.descripcion.set(value="")

        # Componentes
        ventana.elimina_botones()
        Boton(ventana.botones, text= "Personaje", command= ventana.npc_aleatorio, theme= ventana.theme).grid(column=0, columnspan=2, row=1, padx=10, pady=5)

    # Funciones visuales
    def elimina_botones(ventana):
        regex = compile(r'.*boton.*',dot)
        elementos= list(ventana.botones.children)
        for i in elementos :
            if regex.match(i) != None:
                ventana.botones.children[i].destroy()

class Ventana_Conversor(Frame_Ventana):
    def __init__(ventana, master, theme):
        super().__init__(master= master, theme=theme)
        # Crear la (Sub-ventana)
        ventana.frame = Frame_Ventana(ventana, theme)
        ventana.frame.colocar()

        # Colores
        ventana.theme= theme

        # Datos
        ventana.m= ctk.StringVar()
        ventana.feet= ctk.StringVar()
        ventana.inch= ctk.StringVar()
        ventana.es_m= ctk.BooleanVar(value=False)

        ventana.kg= ctk.StringVar()
        ventana.lb= ctk.StringVar()
        ventana.oz= ctk.StringVar()
        ventana.es_kg= ctk.BooleanVar(value=False)

        ventana.l= ctk.StringVar()
        ventana.gal= ctk.StringVar()
        ventana.es_l= ctk.BooleanVar(value=False)

        # Distancia
        frame_distancia= Div(ventana.frame)
        frame_distancia.pack(expand=True, fill="x")
            # Titulo
        Texto(frame_distancia, text="Distancia", font=ctk.CTkFont(size=20)).pack()
            # 1º linea
        frame_d1= Div(frame_distancia)
        frame_d1.pack(expand=True, fill="x", pady=5)
        Entrada(frame_d1, variable= ventana.feet).pack(side="left")
        Texto(frame_d1, text="Feet").pack(side="left", padx=10)
        Entrada(frame_d1, variable= ventana.inch).pack(side="left")
        Texto(frame_d1, text="Inches").pack(side="left", padx=10)
            # 2º Linea
        frame_d2= Div(frame_distancia)
        frame_d2.pack(expand=True, pady=5)
        ventana.boton_distancia= Boton(frame_d2, text= "⬇", command= ventana.calcular_distancia, theme=ventana.theme)
        ventana.boton_distancia.pack(side="left")
        CheckBox(frame_d2, text= "Cambiar", variable=ventana.es_m, command= ventana.cambiar_distancia, theme=ventana.theme).pack(side="left", padx=10)
            # 3º Linea
        frame_d3= Div(frame_distancia)
        frame_d3.pack(expand=True, pady=5)
        Entrada(frame_d3, variable= ventana.m).pack(side="left")
        Texto(frame_d3, text="Metros").pack(side="left", padx=10)

        # Peso
        frame_peso= Div(ventana.frame)
        frame_peso.pack(expand=True, fill="x", pady=10)
            # Titulo
        Texto(frame_peso, text="Peso", font=ctk.CTkFont(size=20)).pack()
            # 1º linea
        frame_p1= Div(frame_peso)
        frame_p1.pack(expand=True, fill="x", pady=5)
        Entrada(frame_p1, variable= ventana.lb).pack(side="left")
        Texto(frame_p1, text="Pound").pack(side="left", padx=10)
        Entrada(frame_p1, variable= ventana.oz).pack(side="left")
        Texto(frame_p1, text="Ounces").pack(side="left", padx=10)
            # 2º Linea
        frame_p2= Div(frame_peso)
        frame_p2.pack(expand=True, pady=5)
        ventana.boton_peso= Boton(frame_p2, text= "⬇", command= ventana.calcular_peso, theme=ventana.theme)
        ventana.boton_peso.pack(side="left")
        CheckBox(frame_p2, text= "Cambiar", variable=ventana.es_kg, command= ventana.cambiar_peso, theme=ventana.theme).pack(side="left", padx=10)
            # 3º Linea
        frame_p3= Div(frame_peso)
        frame_p3.pack(expand=True, pady=5)
        Entrada(frame_p3, variable= ventana.kg).pack(side="left")
        Texto(frame_p3, text="Kilos").pack(side="left", padx=10)
            
        # Cantidad
        frame_cantidad= Div(ventana.frame)
        frame_cantidad.pack(expand=True, fill="x")
            # Titulo
        Texto(frame_cantidad, text="Cantidad", font=ctk.CTkFont(size=20)).pack()
            # 1º linea
        frame_c1= Div(frame_cantidad)
        frame_c1.pack(expand=True, pady=5)
        Entrada(frame_c1, variable= ventana.gal).pack(side="left")
        Texto(frame_c1, text="Gallon").pack(side="left", padx=10)
            # 2º Linea
        frame_c2= Div(frame_cantidad)
        frame_c2.pack(expand=True, pady=5)
        ventana.boton_cantidad= Boton(frame_c2, text= "⬇", command= ventana.calcular_cantidad, theme=ventana.theme)
        ventana.boton_cantidad.pack(side="left")
        CheckBox(frame_c2, text= "Cambiar", variable=ventana.es_l, command= ventana.cambiar_cantidad, theme=ventana.theme).pack(side="left", padx=10)
            # 3º Linea
        frame_c3= Div(frame_cantidad)
        frame_c3.pack(expand=True, pady=5)
        Entrada(frame_c3, variable= ventana.l).pack(side="left")
        Texto(frame_c3, text="Litros").pack(side="left", padx=10)
    
    def calcular_distancia(ventana):
        if ventana.es_m.get():
            feet= 0
            inch= 0
            try:
                m = float(ventana.m.get()) if ventana.m.get()!= "" else 0
            except:
                print("No es un numero")
            feet, inch = conversor_m_pies(m, 0, True)
            ventana.feet.set(str(feet))
            ventana.inch.set(str(inch))
        else:
            m= 0
            try:
                feet = int(ventana.feet.get()) if ventana.feet.get()!= "" else 0
                inch = int(ventana.inch.get()) if ventana.inch.get()!= "" else 0
            except:
                print("No es un numero")
            m = conversor_m_pies(feet, inch, False)[0]
            ventana.m.set(str(m))
            
    def cambiar_distancia(ventana):
        if ventana.es_m.get():
            ventana.boton_distancia.configure(text="⬆")
        else:
            ventana.boton_distancia.configure(text="⬇")
    
    def calcular_peso(ventana):
        if ventana.es_kg.get():
            lb= 0
            oz= 0
            try:
                kg = float(ventana.kg.get()) if ventana.kg.get()!= "" else 0
            except:
                print("No es un numero")
            lb, oz = conversor_lb_kg(kg, 0, True)
            ventana.lb.set(str(lb))
            ventana.oz.set(str(oz))
        else:
            kg= 0
            try:
                lb = int(ventana.lb.get()) if ventana.lb.get()!= "" else 0
                oz = int(ventana.oz.get()) if ventana.oz.get()!= "" else 0
            except:
                print("No es un numero")
            kg = conversor_lb_kg(lb, oz, False)[0]
            ventana.kg.set(str(kg))

    def cambiar_peso(ventana):
        if ventana.es_kg.get():
            ventana.boton_peso.configure(text="⬆")
        else:
            ventana.boton_peso.configure(text="⬇")
    
    def calcular_cantidad(ventana):
        if ventana.es_l.get():
            gal= 0
            try:
                l = float(ventana.l.get()) if ventana.l.get()!= "" else 0
            except:
                print("No es un numero")
            gal = conversor_l_gal(l, True)
            ventana.gal.set(str(gal))
        else:
            l= 0
            try:
                gal = float(ventana.gal.get()) if ventana.gal.get()!= "" else 0
            except:
                print("No es un numero")
            l = conversor_l_gal(gal, False)
            ventana.l.set(str(l))

    def cambiar_cantidad(ventana):
        if ventana.es_l.get():
            ventana.boton_cantidad.configure(text="⬆")
        else:
            ventana.boton_cantidad.configure(text="⬇")

class Ventana_Guardias(Frame_Ventana):
    def __init__(ventana, master, theme):
        super().__init__(master= master, theme=theme)
        # Crear la (Sub-ventana)
        ventana.frame = Frame_Ventana(ventana, theme)
        ventana.frame.colocar()
        
        # Colores
        ventana.theme= theme

        # Datos
        ventana.texto = ctk.StringVar(value="")

        # Crear Frame para "personajes"
        ventana.personajes= Div(ventana.frame)
        ventana.personajes.pack()

        # Crear hueco para el primer Personaje
        ventana.crea_personaje()

        # Crear un frame para las opciones que no se borran
        opciones= Div(ventana.frame)
        opciones.pack()
        # Frame para los botones
        botones= Div(opciones)
        botones.pack()
        # Crear botones para añadir personajes y calcultar total
        Boton(botones, text="Añadir Personaje", command=ventana.crea_personaje, theme= ventana.theme).pack(side="left", padx=10)
        Boton(botones, text="Calcular Total", command=ventana.calcula_total, theme= ventana.theme).pack(side="left", padx=10)
        Boton(botones, text="Borrar", command=ventana.borrar_pjs, theme= ventana.theme).pack(side="left", padx=10)

        # Crear un texto donde saldran los resultados
        Texto(opciones, variable=ventana.texto).pack()

    def crea_personaje(ventana):
        pj= Div(ventana.personajes)
        pj.pack( pady=5)
        
        Texto(pj, text="Horas de Sueño").pack(side="left", padx=10)
        Entrada(pj).pack(side="left")

        ventana.personajes.update()
    
    def calcula_total(ventana):
        personajes= []
        # Obtener información de todos los Entry de ventana.personajes
        regex_frame = compile('.*div.*',dot)
        regex_entry = compile('.*entrada.*',dot)
        for i in ventana.personajes.children:
            if regex_frame.match(i) != None:
                for e in ventana.personajes.children[i].children:
                    if regex_entry.match(e) != None:
                        horas= 0
                        try:
                            horas = float(ventana.personajes.children[i].children[e].get())
                        except:
                            ventana.texto.set("Valor introducido invalido")
                        personajes.append(horas)

        result =calcula_guardias(personajes)
        ventana.texto.set(result)
    
    def borrar_pjs(ventana):
        regex_frame = compile('.*div.*',dot)
        elementos= list(ventana.personajes.children)
        for i in elementos:
            if regex_frame.match(i) != None:
                ventana.personajes.children[i].destroy()
        ventana.crea_personaje()