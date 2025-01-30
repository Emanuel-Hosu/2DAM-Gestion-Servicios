import tkinter as tkinter

def dia():
    num = int(entrada1.get())

    match num:
        case 1:
            texto.config(text="Lunes")
        case 2:
            texto.config(text="Martes")
        case 3:
            texto.config(text="Miercoles")
        case 4:
            texto.config(text="Jueves")
        case 5:
            texto.config(text="Viernes")
        case 6:
            texto.config(text="Sabado")
        case 7:
            texto.config(text="Domingo")


ventana = tkinter.Tk()
ventana.title("Dia de la semana")

entrada1 = tkinter.Entry(ventana)
entrada1.grid(row= 0, column=0, padx=10, pady=10)

buton = tkinter.Button(ventana, text="Confirmar", command=dia)
buton.grid(row=1, column=0, padx=10, pady=10)

texto = tkinter.Label(ventana, text="Insert a num")
texto.grid(row=2, column= 0, padx=10, pady=10)

ventana.mainloop()