import customtkinter as ctk
from configuracion import *
from any_code import *

# Ventanas de Aplicaciones
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
        textos.pack(fill="x", padx=10, pady=5)
        ctk.CTkLabel(textos, textvariable= ventana.nombre,font=ctk.CTkFont(size=20)).pack(fill="x")
        ctk.CTkLabel(textos, textvariable= ventana.opciones).pack(fill="x")
        # Botones
        ventana.botones = ctk.CTkFrame(frame, fg_color="transparent")
        ventana.botones.pack(padx=10, pady=5)
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

        ctk.CTkButton(ventana.botones, text= "Nueva Letra", command= ventana.nueva_letra).pack(side="left", padx=10, pady=5)
        ctk.CTkButton(ventana.botones, text= "Borrar", command= ventana.borrar).pack(side="left", padx=10, pady=5)
    
    def elimina_botones(ventana):
        regex = compile('.*button.*',dot)
        for i in ventana.botones.children :
            if regex.match(i) != None:
                ventana.botones.children[i].pack_forget()

class Ventana_Lugar(ctk.CTkFrame):
    def __init__(ventana, master):
        super().__init__(master= master)

        # Crear la (Sub-ventana)
        ventana.frame = ctk.CTkFrame(ventana)
        ventana.frame.place(relx=0.5, rely=0.5, anchor="center")
        # Datos
        ventana.nombre = ctk.StringVar(value="")
        ventana.nombre_ref = ""
        ventana.descripcion_1 = ctk.StringVar(value="")
        ventana.descripcion_2 = ctk.StringVar(value="")
        # Componentes
        ctk.CTkLabel(ventana.frame, textvariable= ventana.nombre, font=ctk.CTkFont(size=20)).pack(fill="x", padx=10, pady=5)
        ctk.CTkLabel(ventana.frame, textvariable= ventana.descripcion_1).pack(fill="x", padx=10, pady=5)
        ctk.CTkLabel(ventana.frame, textvariable= ventana.descripcion_2).pack(fill="x", padx=10, pady=5)
        
        ctk.CTkButton(ventana.frame, text= "Lugar", command= ventana.lugar_aleatorio).pack(padx=10, pady=5)

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
        ctk.CTkButton(ventana.frame, text= "Cambiar Adjetivos", command= ventana.cambiar_adj).pack(padx=10, pady=5)
        ctk.CTkButton(ventana.frame, text= "Cambiar Descripciones", command= ventana.cambiar_des).pack(padx=10, pady=5)
        ctk.CTkButton(ventana.frame, text= "Borrar", command= ventana.borrar).pack(padx=10, pady=5)

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
        ctk.CTkButton(ventana.frame, text= "Lugar", command= ventana.lugar_aleatorio).pack(padx=10, pady=5)


    # Funciones visuales
    def elimina_botones(ventana):
        regex = compile(r'.*button.*',dot)
        for i in ventana.frame.children :
            if regex.match(i) != None:
                ventana.frame.children[i].pack_forget()
  