import numpy as np
from sympy import symbols, Function, sympify, lambdify
import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt

# Método de Runge-Kutta de 2ª Ordem
def runge_kutta_2nd_order(f, x0, y0, x_max, n):
    h = (x_max - x0) / n
    x_values = np.linspace(x0, x_max, n+1)
    y_values = np.zeros(n+1)
    y_values[0] = y0

    for i in range(n):
        x = x_values[i]
        y = y_values[i]
        k1 = h * f(x, y)
        k2 = h * f(x + h, y + k1)
        y_values[i+1] = y + (k1 + k2) / 2

    return x_values, y_values

# Método de Runge-Kutta de 4ª Ordem
def runge_kutta_4th_order(f, x0, y0, x_max, n):
    h = (x_max - x0) / n
    x_values = np.linspace(x0, x_max, n+1)
    y_values = np.zeros(n+1)
    y_values[0] = y0

    for i in range(n):
        x = x_values[i]
        y = y_values[i]
        k1 = h * f(x, y)
        k2 = h * f(x + h/2, y + k1/2)
        k3 = h * f(x + h/2, y + k2/2)
        k4 = h * f(x + h, y + k3)
        y_values[i+1] = y + (k1 + 2*k2 + 2*k3 + k4) / 6

    return x_values, y_values

# Método de Runge-Kutta de 6ª Ordem
def runge_kutta_6th_order(f, x0, y0, x_max, n):
    h = (x_max - x0) / n
    x_values = np.linspace(x0, x_max, n+1)
    y_values = np.zeros(n+1)
    y_values[0] = y0

    for i in range(n):
        x = x_values[i]
        y = y_values[i]
        k1 = h * f(x, y)
        k2 = h * f(x + h/3, y + k1/3)
        k3 = h * f(x + h/3, y + k1/6 + k2/6)
        k4 = h * f(x + h/2, y + k1/8 + 3*k3/8)
        k5 = h * f(x + h, y + k1/2 - 3*k3/2 + 2*k4)
        k6 = h * f(x + h, y - 3*k1/2 + 3*k3/2 + k5)
        y_values[i+1] = y + (k1 + 4*k2 + k3 + k5 + 4*k6) / 10

    return x_values, y_values

# Método de Euler
def euler_method(f, x0, y0, x_max, n):
    h = (x_max - x0) / n
    x_values = np.linspace(x0, x_max, n+1)
    y_values = np.zeros(n+1)
    y_values[0] = y0

    for i in range(n):
        x = x_values[i]
        y = y_values[i]
        y_values[i+1] = y + h * f(x, y)

    return x_values, y_values

# Método de Heun
def heun_method(f, x0, y0, x_max, n):
    h = (x_max - x0) / n
    x_values = np.linspace(x0, x_max, n+1)
    y_values = np.zeros(n+1)
    y_values[0] = y0

    for i in range(n):
        x = x_values[i]
        y = y_values[i]
        k1 = h * f(x, y)
        k2 = h * f(x + h, y + k1)
        y_values[i+1] = y + (k1 + k2) / 2

    return x_values, y_values

# Função para resolver EDOs
def solve_edo1(equation_str, x0, y0, x_final, n, method):
    x, y = symbols('x y')
    derivative_expr = sympify(equation_str)
    f = lambdify((x, y), derivative_expr, modules=['numpy'])

    if method == 'RK4':
        return runge_kutta_4th_order(f, x0, y0, x_final, n)
    elif method == 'RK2':
        return runge_kutta_2nd_order(f, x0, y0, x_final, n)
    elif method == 'RK6':
        return runge_kutta_6th_order(f, x0, y0, x_final, n)
    elif method == 'Euler':
        return euler_method(f, x0, y0, x_final, n)
    elif method == 'Heun':
        return heun_method(f, x0, y0, x_final, n)
    else:
        raise ValueError("Método desconhecido")

# Função para plotar o gráfico
def plot_graph(x_values, y_values):
    plt.figure(figsize=(8, 6))
    plt.plot(x_values, y_values, label="y(x)")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Gráfico de y em função de x")
    plt.legend()
    plt.grid(True)
    plt.savefig("grafico.png")
    plt.show()

# Função para salvar os dados em um arquivo CSV
def save_data(x_values, y_values):
    data = np.column_stack((x_values, y_values))
    np.savetxt("dados.csv", data, delimiter=",", header="x,y", comments="")
    messagebox.showinfo("Salvar Dados", "Os dados foram salvos em 'dados.csv' e o gráfico em 'grafico.png'.")

# Função principal para executar o programa
def run():
    try:
        equation_str = equation_entry.get()
        x0 = float(x0_entry.get())
        y0 = float(y0_entry.get())
        x_final = float(x_final_entry.get())
        n = int(n_entry.get())
        method = method_var.get()
        
        if n <= 0:
            raise ValueError("O número de pontos deve ser maior que zero.")

        x_values, y_values = solve_edo1(equation_str, x0, y0, x_final, n, method)
        plot_graph(x_values, y_values)
        save_data(x_values, y_values)

    except Exception as e:
        messagebox.showerror("Erro", str(e))

# Configuração da interface gráfica
root = tk.Tk()
root.title("Método de Runge-Kutta para EDOs")

tk.Label(root, text="Digite a derivada de y (y'):").pack()
equation_entry = tk.Entry(root)
equation_entry.pack()

tk.Label(root, text="x0:").pack()
x0_entry = tk.Entry(root)
x0_entry.pack()

tk.Label(root, text="y0:").pack()
y0_entry = tk.Entry(root)
y0_entry.pack()

tk.Label(root, text="x final:").pack()
x_final_entry = tk.Entry(root)
x_final_entry.pack()

tk.Label(root, text="Número de pontos (n):").pack()
n_entry = tk.Entry(root)
n_entry.pack()

method_var = tk.StringVar(value='RK4')
tk.Radiobutton(root, text="Runge-Kutta 4ª Ordem", variable=method_var, value='RK4').pack()
tk.Radiobutton(root, text="Runge-Kutta 2ª Ordem", variable=method_var, value='RK2').pack()
tk.Radiobutton(root, text="Runge-Kutta 6ª Ordem", variable=method_var, value='RK6').pack()
tk.Radiobutton(root, text="Método de Euler", variable=method_var, value='Euler').pack()
tk.Radiobutton(root, text="Método de Heun", variable=method_var, value='Heun').pack()

tk.Button(root, text="Resolver e Plotar", command=run).pack()

root.mainloop()