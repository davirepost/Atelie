import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

def criar_menu():
    def abrir_clientes_cadastrados():
        messagebox.showinfo("Clientes Cadastrados", "Aqui estão os clientes cadastrados.")

    def cadas_clientes():
        from Cadastro_clien import confirmar_cadastro
        menu_opcoes.withdraw()
        confirmar_cadastro()

    def abrir_pedidos2():
        from pedidos import abrir_pedidos
        menu_opcoes.withdraw()
        abrir_pedidos()

    # Criar a janela principal do menu
    menu_opcoes = tk.Tk()
    menu_opcoes.title("Menu de Pedidos")
    menu_opcoes.geometry("1000x600")

    barra_superior = ttk.Label(menu_opcoes, text="Menu de Pedidos", font=("Helvetica", 14))
    barra_superior.pack(side="top", fill="x")

    botao_clientes_cadastrados = ttk.Button(menu_opcoes, text="Clientes Cadastrados", command=abrir_clientes_cadastrados)
    botao_clientes_cadastrados.pack(pady=20)

    botao_cadastrar_clientes = ttk.Button(menu_opcoes, text="Cadastrar Clientes", command=cadas_clientes)
    botao_cadastrar_clientes.pack()

    botao_pedidos = ttk.Button(menu_opcoes, text="Pedidos", command=abrir_pedidos2)
    botao_pedidos.pack(pady=20)

    menu_opcoes.mainloop()

# Chamada da função para criar o menu
criar_menu()
