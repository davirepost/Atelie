from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import mysql.connector

def abrir_pedidos():
    conexao = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user='root',
        password='',
        database='atelie'
    )
    cursor = conexao.cursor()

    pedido = tk.Tk()
    pedido.geometry("1000x600")
    pedido.title('Pedidos')

    # Definir variáveis globais
    entry_descricao = ttk.Entry(pedido)
    entry_data_entrega = ttk.Entry(pedido)
    entry_status = ttk.Entry(pedido)

    def clique_2():
        # Acessar as variáveis globais
        descricao = entry_descricao.get()
        data_entrega = entry_data_entrega.get()
        status = entry_status.get()

        comando = "INSERT INTO `pedido`(`descricao`, `data_entrega`, `status`) VALUES (%s, %s, %s)"
        values = (descricao, data_entrega, status)
        cursor.execute(comando, values)
        conexao.commit()
        messagebox.showinfo("Sucesso", "Pedido cadastrado com sucesso!")

    def abrir_lista_pedidos():

        comando= "SELECT `descricao`, `data_entrega`, `status` FROM `pedido`"
        
        try:
            cursor.execute(comando)
            resultados= cursor.fetchall()

            for resultado in resultados:
                descricao, data_entrega, status= resultado
        finally:
            cursor.close()
            conexao.close()
    # Aqui você pode adicionar o código para abrir a lista de pedidos
   
    # Botão para cadastrar pedidos
    botao_cadastrar = tk.Button(pedido, text="Cadastrar Pedidos", command=clique_2)
    botao_cadastrar.grid(padx=10, pady=10)

    # Botão para listar pedidos
    botao_lista = tk.Button(pedido, text="Lista de Pedidos", command=abrir_lista_pedidos)
    botao_lista.grid(padx=10, pady=10)

    pedido.mainloop()

# Chamar a função para abrir a janela de pedidos
abrir_pedidos()
