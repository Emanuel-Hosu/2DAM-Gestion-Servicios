import tkinter as tk

def paroimpar():
    num1 = int(entrada1.get())
    num2 = int(entrada2.get())

    if (num1 > num2):
        mensaje.config(text = "Num1 es mayot")
    else:
        mensaje.config(text = "Num2 es mayot")


ventana = tk.Tk()
ventana.title("Mayor o menor")

entrada1 = tk.Entry(ventana)
entrada1.grid(row=0, column= 0, padx=10)

entrada2 = tk.Entry(ventana)
entrada2.grid(row=0, column= 2, padx=10)

boton = tk.Button(ventana, text="Confirmar", command=paroimpar)
boton.grid(row=1, column= 0, columnspan= 2, padx=10)

mensaje = tk.Label(ventana, text="")
mensaje.grid(row=2, column= 0, columnspan= 2, padx= 10)

ventana.mainloop()