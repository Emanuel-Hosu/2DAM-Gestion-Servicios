import os
os.environ['TK_SILENCE_DEPRECATION'] = '1'

import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Emanuel Hosu")

def saludar():
    messagebox.showinfo("Saludo", "¿Qué pasa, tío?") 

boton = tk.Button(ventana, text="Confirmar", command=saludar)
boton.pack(pady=40)
boton.pack(padx=40)

ventana.mainloop()
