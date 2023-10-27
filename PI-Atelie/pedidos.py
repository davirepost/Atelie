import tkinter as tk
from tkinter import Tk



def pedidos():
    from Menu import abrir_pedidos 
    pedido= tk.Tk()
    pedido.geometry("1000x600")
    pedido.title('Pedidos')
    texto=tk.Label(pedido, text="", font="Arial")
    botao= tk.Button(pedido, text="Lista de Pedidos", command= clique)
    botao.grid(padx=10, pady=10)
    botao= tk.Button(pedido, text="Cadastrar Pedidos", command= clique_2)
    botao.grid(padx=10, pady=10)
    
    pedido.mainloop ()

def clique():
    #todos os pedidos aqui
    print ("isso ai")

def clique_2():
    #estrutura de cadastro de pedido
    print ("isso ai 2")




