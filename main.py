import customtkinter as ctk

from configuracion import *
from componentes import *

import swade_ventanas as sw
import any_ventanas as anyr
import DyD_ventanas as dyd

class App(ctk.CTk):
    def __init__(app, titulo, tamaño):
        super().__init__()
    # Propiedades de la Ventana
        app.title(titulo)
        app.iconbitmap("d20-highlight.ico")
        app.geometry(f"{tamaño[0]}x{tamaño[1]}")

    # Definir la grid
        app.columnconfigure(0, weight=1, uniform="a")
        app.columnconfigure(1, weight=3, uniform="a")
        app.rowconfigure(0, weight=1, uniform="a")

    #Componentes
        lista_menu= [
            # Any System
            ["Nombre Aleatorio", lambda: app.cambiar_ventana(anyr.Ventana_Nombre, "any"), "any"],
            ["Lugar Aleatorio", lambda: app.cambiar_ventana(anyr.Ventana_Lugar, "any"), "any"],
            ["Personaje Aleatorio", lambda: app.cambiar_ventana(anyr.Ventana_Personaje, "any"), "any"],
            ["Conversores", lambda: app.cambiar_ventana(anyr.Ventana_Conversor, "any"), "any"],
            ["Tiempo de Guardia", lambda: app.cambiar_ventana(anyr.Ventana_Guardias, "any"), "any"],
            # SWADE
            ["Probabilidad Dado SWADE", lambda: app.cambiar_ventana(sw.Ventana_Probalidades, "swade"), "swade"],
            ["Atributo como Dado Salvaje", lambda: app.cambiar_ventana(sw.Ventana_Dados_Salvajes, "swade"), "swade"],
            ["Poner Habilidades Base", lambda: app.cambiar_ventana(sw.Ventana_Habilidades, "swade"), "swade"],
            ["Aumentos por Rango", lambda: app.cambiar_ventana(sw.Ventana_Avances, "swade"),"swade"], 
            
            # D&D
            ["Puntos de Vida", lambda: app.cambiar_ventana(dyd.Ventana_Puntos_Vida, "dyd"), "dyd"],
        ]
        Frame_Menu(app, opciones=lista_menu).colocar()

        app.main = Frame_Principal(app)
        app.main.colocar()
    
    # Ejecución
        app.mainloop()
    
    def cambiar_ventana(app, funcion, theme):
        # Eliminar las ventas que estubieran antes
        for i in app.grid_slaves(column=1, row=0):
            i.destroy()

        ventana = funcion(app, theme)
        ventana.grid(column=1, row=0, sticky="snew")

# Ejecutar el codigo para crear la ventanas
if __name__== "__main__":
    App(titulo="Ayudas de Roll",tamaño=(800,500)) 
