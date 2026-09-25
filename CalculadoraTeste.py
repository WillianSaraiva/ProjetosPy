import tkinter as tk
from tkinter import messagebox

def soma_numeros():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado = num1 + num2
        messagebox.showinfo("Resultado", f"0 quociente é: {resultado}")
    except ValueError:
        messagebox.showinfo("Erro", "Por favor, insira números válidos.")

def sub_numeros():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado = num1 - num2
        messagebox.showinfo("Resultado", f"0 quociente é: {resultado}")
    except ValueError:
        messagebox.showinfo("Erro", "Por favor, insira números válidos.")

def mult_numeros():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado = num1 * num2
        messagebox.showinfo("Resultado", f"0 quociente é: {resultado}")
    except ValueError:
        messagebox.showerror("Erro","Por favor, insira números válidos.")

def div_numeros():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado = num1 / num2
        messagebox.showinfo("Resultado", f"0 quociente é: {resultado}")
    except ValueError:
        messagebox.showerror("Erro","Por favor, insira números válidos.")
    except ZeroDivisionError:
        messagebox.showerror("Erro", "Divisão por zero não é permitida.")

janela = tk.Tk()
janela.title("Calculadora de Divisão")

label_num1 = tk.Label(janela, text="Numero1:")
label_num1.grid(row=0, column=0, padx=10, pady=5, sticky="e")

entry_num1 = tk.Entry(janela)
entry_num1.grid(row=0, column=1, padx=10, pady=5)

label_num2 = tk.Label(janela, text="Numero2: ")
label_num2.grid(row=1, column=0, padx=10, pady=5, sticky="e")

entry_num2 = tk.Entry(janela)
entry_num2.grid(row=1, column=1, padx=10, pady=5)

botao_div = tk.Button(janela, text="Dividir", command=div_numeros)
botao_div.grid(row=2, columnspan=2, padx=100, pady=1)

botao_mult = tk.Button(janela, text="Multiplicar", command=mult_numeros)
botao_mult.grid(row=2, columnspan=3, padx=250, pady=1)

botao_soma = tk.Button(janela, text="Soma", command=soma_numeros)
botao_soma.grid(row=3, columnspan=2, padx=10, pady=1)

janela.mainloop()
