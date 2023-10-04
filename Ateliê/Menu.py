import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Função para abrir a tela de clientes cadastrados
def abrir_clientes_cadastrados():
    messagebox.showinfo("Clientes Cadastrados", "Aqui estão os clientes cadastrados.")

# Função para abrir a tela de cadastro de clientes
def abrir_cadastrar_clientes():
    messagebox.showinfo("Cadastrar Clientes", "Abra a tela de cadastro de clientes aqui.")

# Função para abrir a tela de pedidos
def abrir_pedidos():
    messagebox.showinfo("Pedidos", "Aqui estão os pedidos.")

# Criar a janela principal
root = tk.Tk()
root.title("Menu de Pedidos")
root.geometry("400x200")  # Define o tamanho da tela para 400x200 pixels

# Criar a barra superior com o nome "Menu de Pedidos"
barra_superior = ttk.Label(root, text="Menu de Pedidos", font=("Helvetica", 14))
barra_superior.pack(side="top", fill="x")

# Botão para acessar "Clientes Cadastrados"
botao_clientes_cadastrados = ttk.Button(root, text="Clientes Cadastrados", command=abrir_clientes_cadastrados)
botao_clientes_cadastrados.pack(pady=20)

# Botão para acessar "Cadastrar Clientes"
botao_cadastrar_clientes = ttk.Button(root, text="Cadastrar Clientes", command=abrir_cadastrar_clientes)
botao_cadastrar_clientes.pack()

# Botão para acessar "Pedidos"
botao_pedidos = ttk.Button(root, text="Pedidos", command=abrir_pedidos)
botao_pedidos.pack(pady=20)

# Iniciar o loop principal da janela
root.mainloop()
