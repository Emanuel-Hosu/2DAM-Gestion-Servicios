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
        
        for numero in self.calculadoraText:
            StringLabelText += str(numero)

        self.canvas.delete("1.0", tk.END)
        self.canvas.insert(tk.END, StringLabelText)

    def operador(self, operador):
        if operador == "+":
            self.operadorchar = "+"
        elif operador == "-":
            self.operadorchar = "-"
        elif operador == "*":
            self.operadorchar = "*"
        elif operador == "/":
            self.operadorchar = "/"
        if operador == "=":
            if self.operadorchar == "+":
                resultado = self.num1 + self.num2
            elif self.operadorchar == "-":
                resultado = self.num1 - self.num2
            elif self.operadorchar == "*":
                resultado = self.num1 * self.num2
            elif self.operadorchar == "/":
                resultado = self.num1 / self.num2

            self.canvas.insert(tk.END, resultado)

        StrArray = ""
        for numero in self.calculadoraText:
            StrArray += str(numero)
        if self.num1 == 0:
            self.num1 = int(StrArray)
            self.calculadoraText.clear()
            self.canvas.delete("1.0", tk.END)
        else:
            self.num2 = int(StrArray)
            self.calculadoraText.clear()
            self.canvas.delete("1.0", tk.END)

    def setSetting(self):
        self.ventana.title("Calculadora")

        self.canvas.config()
        self.canvas.grid(row=0, column=0, columnspan=4)

        self.b1.config(text="7", width=5, command=lambda: self.escribirEnCanva(7))
        self.b1.grid(row = 1, column=0, padx=4, pady=4)

        self.b2.config(text="8", width=5, command=lambda: self.escribirEnCanva(8))
        self.b2.grid(row = 1, column=1, padx=4, pady=4)

        self.b3.config(text="9", width=5, command=lambda: self.escribirEnCanva(9))
        self.b3.grid(row = 1, column=2, padx=4, pady=4)

        self.b4.config(text="*", width=5, command=lambda: self.operador('*'))
        self.b4.grid(row = 1, column=3, padx=4, pady=4)

        self.b5.config(text="4", width=5, command=lambda: self.escribirEnCanva(4))
        self.b5.grid(row = 2, column=0, padx=4, pady=4)

        self.b6.config(text="5", width=5, command=lambda: self.escribirEnCanva(5))
        self.b6.grid(row = 2, column=1, padx=4, pady=4)

        self.b7.config(text="6", width=5, command=lambda: self.escribirEnCanva(6))
        self.b7.grid(row = 2, column=2, padx=4, pady=4)

        self.b8.config(text="+", width=5, command=lambda: self.operador('+'))
        self.b8.grid(row = 2, column=3, padx=4, pady=4)

        self.b9.config(text="1", width=5, command=lambda: self.escribirEnCanva(1))
        self.b9.grid(row = 3, column=0, padx=4, pady=4)

        self.b10.config(text="2", width=5, command=lambda: self.escribirEnCanva(2))
        self.b10.grid(row = 3, column=1, padx=4, pady=4)

        self.b11.config(text="3", width=5, command=lambda: self.escribirEnCanva(3))
        self.b11.grid(row = 3, column=2, padx=4, pady=4)

        self.b12.config(text="-", width=5, command=lambda: self.escribirEnCanva(7))
        self.b12.grid(row = 3, column=3, padx=4, pady=4)

        self.b13.config(text="C", width=5, command=lambda: self.operador("-"))
        self.b13.grid(row = 4, column=0, padx=4, pady=4)

        self.b14.config(text="0", width=5, command=lambda: self.escribirEnCanva(0))
        self.b14.grid(row = 4, column=1, padx=4, pady=4)

        self.b15.config(text="/", width=5, command=lambda: self.operador("/"))
        self.b15.grid(row = 4, column=2, padx=4, pady=4)

        self.b16.config(text="=", width=5, command=lambda: self.operador("="))
        self.b16.grid(row = 4, column=3, padx=4, pady=4)

        self.ventana.mainloop()