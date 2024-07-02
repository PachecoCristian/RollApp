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
        ctk.CTkEntry(frame, textvariable=  ventana.valor, insertofftime=1000).grid(column=2, row=0, padx=10, pady=5)

        ctk.CTkLabel(frame, text=  "Dado 1").grid(column=0, row=1, padx=10, pady=5)
        ctk.CTkLabel(frame, text=  "Dado 2").grid(column=1, row=1, padx=10, pady=5)
        ctk.CTkLabel(frame, text=  "Modificador").grid(column=2, row=1, padx=10, pady=5)

        ctk.CTkComboBox(frame, values= SWADE_DADOS, variable= ventana.dado1).grid(column=0, row=2, padx=10, pady=5)
        ctk.CTkComboBox(frame, values= SWADE_DADOS, variable= ventana.dado2).grid(column=1, row=2, padx=10, pady=5)
        ctk.CTkEntry(frame, textvariable=  ventana.extra, insertofftime=1000).grid(column=2, row=2, padx=10, pady=5)

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
        ventana.texto = ctk.StringVar(value= "Seleciona el archivo")
        ventana.ruta = ctk.StringVar()
        #ventana.carpeta = ctk.BooleanVar()

        # Componentes
        ctk.CTkLabel(frame, textvariable=ventana.texto).pack(padx=10, pady=5)
        ctk.CTkButton(frame, text="Cambiar Dados", command=ventana.cambiar_dados).pack(padx=10, pady=5)
        #ctk.CTkCheckBox(ventana,variable=ventana.carpeta)pack(padx=10, pady=5)
    
    def cambiar_dados(ventana):
        # Obtener fichero
        try:
            ventana.ruta= ctk.filedialog.askopenfile().name  
        except AttributeError:
            # Mirar de controlar excepciones expecificas
            pass
        # Comprobar que es una ficha valida
        try:
            datos = abrir_ficha(ventana.ruta)
        except Exception as e:
            ventana.texto.set(e)
            return

        # Comprobar si el comodin
        if datos[1]:
            # Cambiar dados
            ficha= cambiar_dados(datos[0])

            # Guardar la nueva ficha (Al lado de la antigua)
            ruta_final= os.path.split(os.path.abspath(ventana.ruta))
            mensaje= guardar_ficha(ficha, ruta_final[0])
        else:
            mensaje= "Este personaje no tiene Dado Salvaje"
        
        # Mensaje final
        ventana.texto.set(mensaje)

