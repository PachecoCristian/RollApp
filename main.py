import customtkinter as ctk
from configuracion import *
import swade_code as sw
import any_code as anyR

class App(ctk.CTk):
    def __init__(app, titulo, tamaño):
        super().__init__()
        app.title(titulo)
        #self.geometry(f"{tamaño[0]}x{tamaño[1]}")

    # Definir la grid
        app.columnconfigure(0, weight=1, uniform="a")
        app.columnconfigure(1, weight=3, uniform="a")
        app.rowconfigure(0, weight=1, uniform="a")

    #Componentes
        lista_menu= {
            "Probabilidad Dado SWADE": lambda: app.cambiar_ventana(sw.Ventana_Probalidades),
            "Nombre Aleatorio": lambda: app.cambiar_ventana(anyR.Ventana_Nombre),
        }
        Frame_Menu(app,opciones=lista_menu).colocar()

        app.main = Frame_Principal(app)
        app.main.colocar()
    
    # Ejecución
        app.mainloop()
    
    def cambiar_ventana(app, funcion):
        # Eliminar las ventas que estubieran antes
        for i in app.grid_slaves(column=1, row=0) :
            i.grid_remove()

        ventana = funcion(app)
        ventana.grid(column=1, row=0, sticky="snew")
        


# Creación de los componentes
class Frame_Menu(ctk.CTkFrame):
    def __init__(menu, master, opciones):
        super().__init__(master, fg_color="gray", corner_radius= 0)
        menu.columnconfigure(0, weight=1, uniform="b")
        i=0
        for nombre, funcion in  opciones.items():
            menu.rowconfigure(i, weight=1, uniform="b")
            ctk.CTkButton(menu, text= nombre, command= funcion).grid(column=0, row=i, padx =10, pady=15)
            i+=1

    def colocar(self):
        self.grid(column=0, row=0, sticky="snew")

class Frame_Principal(ctk.CTkFrame):
    def __init__(self, master, ):
        super().__init__(master, fg_color="white", corner_radius= 0)

    def colocar(self):
        self.grid(column=1, row=0, sticky="snew")


# Ejecutar el codigo para crear la ventanas
if __name__== "__main__":
    App(titulo="Ayudas de Roll",tamaño=(500,500)) 



