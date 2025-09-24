import tkinter as tk

class Calculadora():
    def __init__(self):
        self.calculadoraText = []
        self.num1 = 0
        self.num2 = 0
        self.operadorchar = ""

        self.ventana = tk.Tk()
        self.canvas = tk.Text()
        self.b1 = tk.Button()
        self.b2 = tk.Button()
        self.b3 = tk.Button()
        self.b4 = tk.Button()
        self.b5 = tk.Button()
        self.b6 = tk.Button()
        self.b7 = tk.Button()
        self.b8 = tk.Button()
        self.b9 = tk.Button()
        self.b10 = tk.Button()
        self.b11 = tk.Button()
        self.b12 = tk.Button()
        self.b13 = tk.Button()
        self.b14 = tk.Button()
        self.b15 = tk.Button()
        self.b16 = tk.Button()

    def escribirEnCanva(self, num):
        self.calculadoraText.append(num)
        StringLabelText = ""

        for i in self.calculadoraText:
            StringLabelText += str(i)

        self.canvas.delete("1.0", tk.END)
        self.canvas.insert(tk.END, StringLabelText)

    def mostrar(self):
        self.ventana.title("Calculadora")

        self.canvas.config(width=30, height=3)
        self.canvas.grid(row=0, column=0, columnspan=4)

        self.b1.config(text="1", width=5, height=2, command=lambda: self.escribirEnCanva(1))
        self.b1.grid(row = 1, column=0, padx=4, pady=4)

        self.ventana.mainloop()


