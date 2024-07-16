import customtkinter as ctk

from configuracion import *
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
            ["Nombre Aleatorio", lambda: app.cambiar_ventana(anyr.Ventana_Nombre),"any"],
            ["Lugar Aleatorio", lambda: app.cambiar_ventana(anyr.Ventana_Lugar),"any"],
            ["Personaje Aleatorio", lambda: app.cambiar_ventana(anyr.Ventana_Personaje),"any"],
            ["Conversores", lambda: app.cambiar_ventana(anyr.Ventana_Conversor),"any"],
            ["Tiempo de Guardia", lambda: app.cambiar_ventana(anyr.Ventana_Guardias),"any"],
            # SWADE
            ["Probabilidad Dado SWADE", lambda: app.cambiar_ventana(sw.Ventana_Probalidades),"swade"],
            ["Atributo como Dado Salvaje", lambda: app.cambiar_ventana(sw.Ventana_Dados_Salvajes),"swade"],
            ["Poner Habilidades Base", lambda: app.cambiar_ventana(sw.Ventana_Habilidades),"swade"],
            ["Aumentos por Rango", lambda: app.cambiar_ventana(sw.Ventana_Avances),"swade"],
            # D&D
            ["Puntos de Vida", lambda: app.cambiar_ventana(dyd.Ventana_Puntos_Vida),"dyd"],
        ]
        Frame_Menu(app, opciones=lista_menu).colocar()

        app.main = Frame_Principal(app)
        app.main.colocar()
    
    # Ejecución
        app.mainloop()
    
    def cambiar_ventana(app, funcion):
        # Eliminar las ventas que estubieran antes
        for i in app.grid_slaves(column=1, row=0):
            i.destroy()

        ventana = funcion(app)
        ventana.grid(column=1, row=0, sticky="snew")

# Creación de los componentes
class Frame_Menu(ctk.CTkFrame):
    def __init__(menu, master, opciones):
        super().__init__(master, fg_color="transparent", corner_radius= 0)
        menu.columnconfigure(0, weight=1, uniform="b")
        i=0
        for opc in opciones:
            menu.rowconfigure(i, weight=1, uniform="b")
            Boton_Menu(menu, text= opc[0], command= opc[1], theme=opc[2]).grid(column=0, row=i, padx =10, pady=15)
            i+=1

    def colocar(self):
        self.grid(column=0, row=0, sticky="snew")

class Frame_Principal(ctk.CTkFrame):
    def __init__(self, master, ):
        super().__init__(master, corner_radius= 0)

    def colocar(self):
        self.grid(column=1, row=0, sticky="snew")

class Boton(ctk.CTkButton):
    def __init__(self, master, text, command, theme):
        super().__init__(master, text= text, command=command, fg_color=THEMES[theme][1])

class Boton_Menu(Boton):
    def __init__(self, master, text, command, theme):
        super().__init__(master, text, command, theme)
        self.configure(fg_color=THEMES[theme][0])
        self.configure(corner_radius=0)

    


# Ejecutar el codigo para crear la ventanas
if __name__== "__main__":
    App(titulo="Ayudas de Roll",tamaño=(800,500)) 
