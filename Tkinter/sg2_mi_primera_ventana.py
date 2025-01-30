import tkinter as tk

def paroimpar():
    num1 = int(entrada.get())
    if (num1 % 2) == 0:
        resultado.config(text="El número es par")
    else:
        resultado.config(text="El número es impar")

ventana = tk.Tk()
ventana.title("Par o impar")

entrada = tk.Entry(ventana)
entrada.grid(row=0, column=0, padx=10, pady=10)

boton = tk.Button(ventana, text="Verificar", command=paroimpar)
boton.grid(row=1, column=0, padx=10, pady=10)

resultado = tk.Label(ventana, text="")
resultado.grid(row=2, column=0, padx=10, pady=10)

ventana.mainloop()