import tkinter as tk

def tablaMultiplicar():
    num = int(entrada1.get())
    tempText = []
    index = 1
    while index <= 10:
        tempText += {f"{num} x {index} = {num * index}"}
        index += 1

    texto.config(text=tempText)

ventana = tk.Tk()
ventana.title("Multiplicar")

entrada1 = tk.Entry(ventana)
entrada1.grid(row=0, column= 0, padx= 10, pady=10)

boton = tk.Button(ventana, text="Confirmar", command=tablaMultiplicar)
boton.grid(row=1, column=0, padx= 10, pady=10)

texto = tk.Label(ventana, text="Insert num")
texto.grid(row=2, column=0, padx=10, pady=10)

ventana.mainloop()