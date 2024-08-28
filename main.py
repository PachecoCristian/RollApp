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
        app.active_menu= False
        app.open_menu= False
    
    # Cambio de tamaño del menu
        app.bind("<Configure>", app.comprueba_tamaño)

    # Definir la grid
        app.columnconfigure(0, weight=MENU_RATIO[0], uniform="a")
        app.columnconfigure(1, weight=MENU_RATIO[1], uniform="a")
        app.rowconfigure(0, weight=1, uniform="a")

        any_apps=[
            ["Nombre Aleatorio", lambda: app.cambiar_ventana(anyr.Ventana_Nombre, "any"), "any"],
            ["Lugar Aleatorio", lambda: app.cambiar_ventana(anyr.Ventana_Lugar, "any"), "any"],
            ["Personaje Aleatorio", lambda: app.cambiar_ventana(anyr.Ventana_Personaje, "any"), "any"],
            ["Distancia / Peso", lambda: app.cambiar_ventana(anyr.Ventana_Conversor, "any"), "any"],
            ["Volumen/ Temperatura", lambda: app.cambiar_ventana(anyr.Ventana_Conversor2, "any"), "any"],
            ["Tiempo de Guardia", lambda: app.cambiar_ventana(anyr.Ventana_Guardias, "any"), "any"],
        ]
        swade_apps=[
            ["Probabilidad Dado SWADE", lambda: app.cambiar_ventana(sw.Ventana_Probalidades, "swade"), "swade"],
            ["Atributo como Dado Salvaje", lambda: app.cambiar_ventana(sw.Ventana_Dados_Salvajes, "swade"), "swade"],
            ["Poner Habilidades Base", lambda: app.cambiar_ventana(sw.Ventana_Habilidades, "swade"), "swade"],
            ["Aumentos por Rango", lambda: app.cambiar_ventana(sw.Ventana_Avances, "swade"),"swade"], 
        ]
        dyd_apps=[
            ["Puntos de Vida", lambda: app.cambiar_ventana(dyd.Ventana_Puntos_Vida, "dyd"), "dyd"],
        ]
        lista_menu= [
            ["Any System", lambda: app.cambiar_menu(any_apps, "any"), "any"],
            ["Swade", lambda: app.cambiar_menu(swade_apps, "swade"), "swade"],
            ["Any System", lambda: app.cambiar_menu(dyd_apps, "dyd"), "dyd"],
        ]
            
    #Componentes
        # Menu con opciones
        app.menu= Frame_Menu(app)
        app.menu.colocar()
        # Ventana principal
        main = Frame_Principal(app)
        main.colocar()
        # Crear el menú movil
        app.menu_desplazable= Frame_MenuD(app, lista_menu)
        # Calcular posición del menú movil
        app.update()
        rel= MENU_RATIO[0]/( MENU_RATIO[0] + MENU_RATIO[1] )
        pos_menu=int((-(app.winfo_width()*rel))+MENU_DESP)
        # Coloar el Menu desplazable
        app.menu_desplazable.place(x=pos_menu, y=0, relheight=1, relwidth=rel)
        # Añadir un evento al entrar en el menu desplazable
        app.menu_desplazable.bind("<Enter>", app.desplegar_menu)
        # Como no adminte bind_all no se puede cerrar al salir del menu
    
    # Ejecución
        app.mainloop()
    
    def cambiar_menu(app, lista, theme):
        # Eliminar el menú que estubiera antes
        elemntos= list(app.menu.children)
        for i in elemntos:
            app.menu.children[i].destroy()

        # Cargar los botones indicados
        app.menu.cargar_botones(opciones=lista)

        # Cerrar el menú desplegable
        app.cerrar_menu()
    
    def cambiar_ventana(app, funcion, theme):
        # Eliminar las ventas que estubieran antes
        for i in app.grid_slaves(column=1, row=0):
            i.destroy()

        ventana = funcion(app, theme)
        ventana.grid(column=1, row=0, sticky="snew")
    
    def desplegar_menu(app,*args):
        if not app.active_menu:
            app.active_menu = True
            app.animar()
            
    def cerrar_menu(app,*args):
        if not app.active_menu:
            app.active_menu = True
            app.animar_inv()
            
    def animar(app):
        if app.menu_desplazable.winfo_x()<= -MENU_DESP:
            distancia= app.menu_desplazable.winfo_x()+ MENU_DESP
            app.menu_desplazable.place(x=distancia, rely=0, relheight=1, relwidth=0.25)
            app.after(10, app.animar)
        else:
            app.active_menu = False
            app.open_menu= True

    def animar_inv(app):
        rel= MENU_RATIO[0]/( MENU_RATIO[0] + MENU_RATIO[1] )
        pos_menu=int((-(app.winfo_width()*rel)) + MENU_DESP) +1

        if app.menu_desplazable.winfo_x()>= pos_menu :
            distancia= app.menu_desplazable.winfo_x()-MENU_DESP
            app.menu_desplazable.place(x=distancia, rely=0, relheight=1, relwidth=0.25)
            app.after(10, app.animar_inv)
        else:
            app.active_menu = False
            app.open_menu= False

    def comprueba_tamaño(app, evento):
        #print("Cambio tamaño")
        if evento.widget == app:
            rel= MENU_RATIO[0]/( MENU_RATIO[0] + MENU_RATIO[1] )
            pos_menu=int((-(app.winfo_width()*rel)) + MENU_DESP) -1

            if app.open_menu:
                app.menu_desplazable.place(x=0, rely=0, relheight=1, relwidth=0.25)
            else:
                app.menu_desplazable.place(x=pos_menu, rely=0, relheight=1, relwidth=0.25)
                


# Ejecutar el codigo para crear la ventanas
if __name__== "__main__":
    App(titulo="Ayudas de Roll",tamaño=(800,500)) 
