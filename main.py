import customtkinter as ctk
from configuracion import *

class App(ctk.CTk):
    def __init__(self, titulo, tamaño):
        super().__init__()
        self.title(titulo)
        #self.geometry(f"{tamaño[0]}x{tamaño[1]}")
    
    # Ejecución
        self.mainloop()

if __name__== "__main__":
    App(titulo="Ayudas de Roll",tamaño=(500,500)) 
