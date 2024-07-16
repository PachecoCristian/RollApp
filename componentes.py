from tkinter.constants import NORMAL
from typing import Any, Tuple
import customtkinter as ctk

from configuracion import *


class Frame_Menu(ctk.CTkFrame):
    def __init__(menu, master, opciones):
        super().__init__(master, fg_color="transparent", corner_radius= 0)
        menu.columnconfigure(0, weight=1, uniform="b")
        i=0
        for opc in opciones:
            menu.rowconfigure(i, weight=1, uniform="b")
            Boton_Menu(menu, text= opc[0], command= opc[1], theme=opc[2]).grid(column=0, row=i, padx =10, pady=5)
            i+=1

    def colocar(self):
        self.grid(column=0, row=0, sticky="snew")

class Frame_Principal(ctk.CTkFrame):
    def __init__(self, master, ):
        super().__init__(master, corner_radius= 0, fg_color="black")

    def colocar(self):
        self.grid(column=1, row=0, sticky="snew")

class Frame_Ventana(ctk.CTkFrame):
    def __init__(self, master, theme):
        super().__init__(master, corner_radius= 0, fg_color=THEMES[theme][3])

    def colocar(self):
        self.place(relx=0.5, rely=0.5, anchor="center")

class Div(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, corner_radius= 0, fg_color="transparent")


class Boton(ctk.CTkButton):
    def __init__(self, master, text, command, theme):
        super().__init__(master, text= text, command=command, fg_color=THEMES[theme][1], hover_color=THEMES[theme][2])
    def colocar(self, side="top"):
        self.pack(side=side, padx=10, pady=5)

class Boton_Menu(Boton):
    def __init__(self, master, text, command, theme):
        super().__init__(master, text, command, theme)
        self.configure(fg_color=THEMES[theme][0])
        self.configure(hover_color=THEMES[theme][1])
        self.configure(corner_radius=0)

class Texto(ctk.CTkLabel):
    def __init__(self, master, text=None, variable=None, font=None, text_color=None):
        super().__init__(master)
        if text != None:
            self.configure(text= text)
        if font != None:
            self.configure(font= font)
        if variable != None:
            self.configure(textvariable= variable)
        if text_color != None:
            self.configure(text_color= text_color)


class Entrada(ctk.CTkEntry):
    def __init__(self, master, variable=None):
        super().__init__(master)
        if variable != None:
            self.configure(textvariable= variable)

class DropDown(ctk.CTkOptionMenu):
    def __init__(self, master, values, theme, variable=None):
        super().__init__(master, values=values, fg_color=THEMES[theme][1], button_color=THEMES[theme][1], button_hover_color=THEMES[theme][2])
        if variable != None:
            self.configure(variable= variable)

class ComboBox (ctk.CTkComboBox):
    def __init__(self, master, values, theme, variable=None):
        super().__init__(master, values=values, fg_color=THEMES[theme][1], button_color=THEMES[theme][1], button_hover_color=THEMES[theme][2])
        if variable != None:
            self.configure(variable= variable)

class CheckBox (ctk.CTkCheckBox):
    def __init__(self, master, theme, text=None, variable=None, command=None ):
        super().__init__(master, fg_color= THEMES[theme][1], hover_color= THEMES[theme][1])
        if text != None:
            self.configure(text= text)
        if variable != None:
            self.configure(variable= variable)
        if command != None:
            self.configure(command= command)