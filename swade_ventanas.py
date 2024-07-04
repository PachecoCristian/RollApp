import customtkinter as ctk
from configuracion import *
from swade_code import *

import os

# Ventanas de Aplicaciones
class Ventana_Probalidades(ctk.CTkFrame):
    def __init__(ventana, master):
        super().__init__(master= master)

        # Crear la (Sub-ventana)
        frame = ctk.CTkFrame(ventana)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        frame.columnconfigure((0,1,2), weight=1, uniform="a")
        frame.rowconfigure((0,1,2,3,4), weight=1, uniform="a")

        # Datos
        ventana.valor = ctk.StringVar(value= "4")
        ventana.dado1 = ctk.StringVar(value= SWADE_DADOS[0])
        ventana.dado2 = ctk.StringVar(value= SWADE_DADOS[0])
        ventana.extra = ctk.StringVar(value= "0")
        ventana.resultado = ctk.StringVar(value= "Probabilidad: ")

        # Componentes
        ctk.CTkLabel(frame, text= "Valor Objetivo").grid(column=0, row=0, padx=10, pady=5)
        ctk.CTkEntry(frame, textvariable=  ventana.valor).grid(column=2, row=0, padx=10, pady=5)

        ctk.CTkLabel(frame, text=  "Dado 1").grid(column=0, row=1, padx=10, pady=5)
        ctk.CTkLabel(frame, text=  "Dado 2").grid(column=1, row=1, padx=10, pady=5)
        ctk.CTkLabel(frame, text=  "Modificador").grid(column=2, row=1, padx=10, pady=5)

        ctk.CTkComboBox(frame, values= SWADE_DADOS, variable= ventana.dado1).grid(column=0, row=2, padx=10, pady=5)
        ctk.CTkComboBox(frame, values= SWADE_DADOS, variable= ventana.dado2).grid(column=1, row=2, padx=10, pady=5)
        ctk.CTkEntry(frame, textvariable=  ventana.extra).grid(column=2, row=2, padx=10, pady=5)

        ctk.CTkButton(frame, text="Calcular", command=ventana.calcular_prob).grid(column=0, columnspan=3, row=3, padx=10, pady=5)

        ctk.CTkLabel(frame, textvariable= ventana.resultado).grid(column=0, columnspan=3, row=4, padx=10, pady=5)

    def calcular_prob(ventana):
        resultado = 0
        valor= int(ventana.valor.get())
        dado1= 0 if ventana.dado1.get() == SWADE_DADOS[0] else int(ventana.dado1.get().replace("D",""))
        dado2= 0 if ventana.dado2.get() == SWADE_DADOS[0] else int(ventana.dado2.get().replace("D",""))
        extra= int(ventana.extra.get())

        if dado1 != 0:
            resultado += expode_prob((valor-extra), dado1)
        
        if dado2 != 0:
            resultado += expode_prob((valor-extra), dado2)

        resultado = round(resultado*100,2)

        ventana.resultado.set(f"Probabilidad: {resultado}%")

class Ventana_Dados_Salvajes(ctk.CTkFrame):
    def __init__(ventana, master):
        super().__init__(master= master)

        # Crear la (Sub-ventana)
        frame = ctk.CTkFrame(ventana)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        # Datos
        ventana.ruta = ctk.StringVar()
        ventana.carpeta = ctk.StringVar()
        ventana.multiples = ctk.BooleanVar(value=False)

        # Componentes
            # Frame para poner mensajes y alertas
        ventana.mensaje1 = ctk.CTkFrame(frame, corner_radius=0, fg_color="transparent")
        ventana.mensaje1.pack(padx=10, pady=5)
        ventana.mensaje(ventana.mensaje1,["Selecciona el archivo"])
            # Frame para botones y el checkbox
        ventana.opciones = ctk.CTkFrame(frame, corner_radius=0, fg_color="transparent")
        ventana.opciones.pack()
        ventana.opciones_multiples()
        
    def ruta_origen(ventana):
        try:
            ventana.ruta.set(ctk.filedialog.askdirectory())
            ventana.mensaje(ventana.mensaje1,["Cambiando archivos de: ",ventana.ruta.get()])
        except AttributeError:
            pass

    def ruta_destino(ventana):
        try:
            ventana.carpeta.set(ctk.filedialog.askdirectory())
            ventana.mensaje(ventana.mensaje2,["Dejando ficheros en: ",ventana.carpeta.get()])
        except AttributeError:
            pass      

    def gestion_fichas(ventana):
        # Eliminar textos inferiores, si los hay
        try:
            ventana.textos.destroy()
        except:
            pass

        # Comprobar que modo se tiene selecionado:
            # 1 solo archivo
            # Carpeta entera
        if not ventana.multiples.get():
        # Si solo hay 1 ficha se pide al usuario que eliga el archivo
            try:
                # El usuario elige el archivo
                ruta = (ctk.filedialog.askopenfile().name)
                fichero= os.path.split(ruta)[1]+": "
                # Se ejcuta el cambio de valores. 
                    # Devuelbe un mensaje de Error o si se a compleatdo correctamente
                mensaje= ventana.cambiar_ficha(ruta)
                # Se muestra el mensaje en el Texto superior de la ventana
                ventana.mensaje(ventana.mensaje1,[fichero,mensaje[0]],mensaje[1])
            except AttributeError:
                # Esta excepción está por el el usuario no elige ninguna ventana
                    # Mirar de controlar excepciones expecificas
                pass
            # Borrando datos usados
            ventana.ruta.set("")
            ventana.carpeta.set("")
        else:
        # Si solo hay varias fichas se recorre la carpeta
            # Comprobar que haya carpeta de origen y destino
            if ventana.ruta.get() == "" or ventana.carpeta.get() == "":
                ventana.mensaje(ventana.mensaje1,["","Seleccione las carpetas de Origen y Destino"],"error")
                return
            
            # Crear Frame para los mensajes de los difreenetes archivos
            ventana.textos = ctk.CTkFrame(ventana.opciones, corner_radius=0, fg_color="transparent")
            ventana.textos.pack()
            ctk.CTkLabel(ventana.textos, text="")

            # Recorer los elemntos en la Carpeta Origen
            carpeta=  os.scandir(ventana.ruta.get())
            for i in carpeta:
                # Se recoren los archivos exeptuando "desktop.ini" que es pripio de windows
                if i.is_file() and i.name != "desktop.ini":
                    # Se crea un frame para poner el mensaje
                    frame = ctk.CTkFrame(ventana.textos, fg_color="transparent")
                    frame.pack(padx=10, pady=5)
                    fichero= i.name+" : "
                    # Se ejcuta el cambio de valores. 
                        # Devuelbe un mensaje de Error o si se a compleatdo correctamente
                    mensaje = ventana.cambiar_ficha(i.path)
                    # Se muestra el mensaje en el frame que se acaba de crear
                    ventana.mensaje(frame,[fichero, mensaje[0]],mensaje[1])
            
            # Borrar Datos
            ventana.ruta.set("")
            ventana.carpeta.set("")
            ventana.mensaje(ventana.mensaje1,["Cambiando archivos de: "])
            ventana.mensaje(ventana.mensaje2,["Dejando ficheros en: "])

    def cambiar_ficha(ventana, ruta):
        # Comprobar que es una ficha valida
        try:
            datos = abrir_ficha(ruta)
        except Exception as e:
            return (e, "error")

        # Comprobar No es comodin
        if not datos[1]:
            return ("Este personaje no tiene Dado Salvaje", "error")
        
        # Cambiar dados
        ficha= cambiar_dados(datos[0])

        # Guardar la nueva ficha 
        if not ventana.multiples.get():
            # Al lado de la antigua si es individual
            ruta_final= os.path.split(os.path.abspath(ruta))[0]
        else:
            # Ruta indicada ecaso de muchas
            ruta_final= os.path.abspath(ventana.carpeta.get())

        # Añadir Nombre del fichero= "Nombre del Personaje"(Dados).json
        ruta_final= f"{ruta_final}\\{ficha[0]["name"]}(Dados).json"

        # Guardar la ficha
        mensaje= guardar_ficha(ficha[0], ruta_final)

        # Comprobar si ventaja que cambia dados
        if ficha[1]:
            return ("El personaje tiene modificación de Dado Salvage", "alerta")
        
        return (mensaje, "correcto")
    
    # Funciones Visuales
    def mensaje(ventana, frame, textos, tipo=""):
        # Borrar posibles elementos en el frame
        try:
            for i in frame.children :
                frame.children[i].pack_forget()
        except:
            pass
        
        # Se recorren los elementos
        for texto in textos:
            # Si es el primero, siempre es un mensaje normal
            if texto == textos[0]:
                ctk.CTkLabel(frame, text=texto ).pack(side="left")
            # Al resto se les camba el color dependiendo 
            else:
                match tipo:
                    case "error":
                        ctk.CTkLabel(frame, text=texto, text_color="red").pack(side="left")
                    case "correcto":
                        ctk.CTkLabel(frame, text=texto, text_color="green").pack(side="left")
                    case "alerta":
                        ctk.CTkLabel(frame, text=texto, text_color="yellow").pack(side="left")
                    case _:
                        ctk.CTkLabel(frame, text=texto ).pack(side="left")

    def borrar_opciones(ventana):
        for i in ventana.opciones.children :
                ventana.opciones.children[i].pack_forget()
    
    def opciones_multiples(ventana):
        # Borrar Datos
        ventana.ruta.set("")
        ventana.carpeta.set("")
        
        try:
            ventana.mensaje2.destroy()
        except:
            pass

        if ventana.multiples.get():
            ventana.borrar_opciones()

            ventana.mensaje(ventana.mensaje1,[""])
            botones = ctk.CTkFrame(ventana.opciones, corner_radius=0, fg_color="transparent")
            botones.columnconfigure((0,1,2), weight=1, uniform="a")
            botones.pack()
            ctk.CTkCheckBox(botones, text="Varios Ficheros" , variable=ventana.multiples, command=ventana.opciones_multiples).grid(column=0, row=0, padx=10, pady=5)
            ctk.CTkButton(botones, text="Carpeta Origen", command=ventana.ruta_origen).grid(column=1, row=0, padx=10, pady=5)
            ctk.CTkButton(botones, text="Carpeta Destino", command=ventana.ruta_destino).grid(column=2, row=0, padx=10, pady=5)
            ctk.CTkButton(ventana.opciones, text="Cambiar Dados", command=ventana.gestion_fichas).pack(pady=5)
            ventana.mensaje2 = ctk.CTkFrame(ventana.opciones, corner_radius=0, fg_color="transparent")
            ventana.mensaje2.pack(padx=10, pady=5)
            ctk.CTkLabel(ventana.mensaje2, text="").pack()
            
        else:
            ventana.borrar_opciones()

            ventana.mensaje(ventana.mensaje1,["Selecciona el archivo"])
            ctk.CTkCheckBox(ventana.opciones, text="Varios Ficheros" , variable=ventana.multiples, command=ventana.opciones_multiples).pack(side="left", padx=10, pady=5)
            ctk.CTkButton(ventana.opciones, text="Cambiar Dados", command=ventana.gestion_fichas).pack(side="left", padx=10, pady=5)
            
class Ventana_Avances(ctk.CTkFrame):
    def __init__(ventana, master):
        super().__init__(master= master)

        # Crear la (Sub-ventana)
        frame = ctk.CTkFrame(ventana)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        # Datos
        ventana.aumentos_actu = ctk.StringVar()
        ventana.n_aumentos = ctk.StringVar()

        # Componetes
        ctk.CTkLabel(frame, textvariable= ventana.aumentos_actu).pack(padx=10, pady=5)
        ventana.aumentos_actuales()
        ctk.CTkEntry(frame, textvariable= ventana.n_aumentos ).pack(padx=10, pady=5)
        ctk.CTkButton(frame, text="Calcular", command=ventana.cambiar_aumentos).pack( padx=10, pady=5)
    
    def aumentos_actuales(ventana):
        archivo= abrir_js(SWADE_FILE)
        valor= valor_avances(archivo)
        match valor:
            case "f":
                respuesta= " un valor personalizado"
            case "d":
                respuesta= " el valor por defecto de SAWDE"
            case _:
                respuesta= f" a {valor} aumentos por nivel"
                
        ventana.aumentos_actu.set(f"Actualmente está {respuesta}")
    
    def cambiar_aumentos(ventana):
        # Compobar que el valor sea correcto
        if ventana.n_aumentos.get().lower() == "d" or ventana.n_aumentos.get().lower() == "default":
            valor= 0
        else:
            try:
                valor = int(ventana.n_aumentos.get())
            except:
                ventana.aumentos_actu.set("El valor debe ser un numero")
        # Modificar el fichero
        ruta = SWADE_FILE
        archivo = abrir_js(ruta)
        archivo = cambiar_avance(archivo, valor)
        guardar_archivo(archivo, ruta) 
        # Actualizar el numero de avances actuales
        avances = valor_avances(archivo)
        match avances:
            case "f":
                avances= "Error"
            case "d":
                avances= "Defecto"

        ventana.aumentos_actu.set(f"Valor cambiado a {avances}")

