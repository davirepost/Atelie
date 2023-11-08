import tkinter as tk  # Importa o módulo tkinter e renomeia-o como "tk"
from tkinter import Tk  # Importa a classe Tk do tkinter (não é necessário)

# Função para lidar com pedidos
def pedidos():
    # Importa a função "abrir_pedidos" do módulo "Menu"
    from Menu import abrir_pedidos 

    # Cria uma nova janela para pedidos
    pedido = tk.Tk()  # Cria uma instância da classe Tk do tkinter para a tela de pedidos
    pedido.geometry("1000x600")  # Define as dimensões da janela para 1000x600 pixels
    pedido.title('Pedidos')  # Define o título da janela

    texto = tk.Label(pedido, text="", font="Arial")  # Cria um rótulo vazio
    botao = tk.Button(pedido, text="Lista de Pedidos", command=clique)  # Cria um botão para exibir uma lista de pedidos e associa a função "clique" ao botão
    botao.grid(padx=10, pady=10)  # Coloca o botão na janela com preenchimento

    botao = tk.Button(pedido, text="Cadastrar Pedidos", command=clique_2)  # Cria um botão para cadastrar pedidos e associa a função "clique_2" ao botão
    botao.grid(padx=10, pady=10)  # Coloca o botão na janela com preenchimento

    pedido.mainloop()  # Inicia o loop principal da interface gráfica da tela de pedidos

# Função associada ao botão "Lista de Pedidos"
def clique():
    # Você pode adicionar a lógica para listar os pedidos aqui
    print("isso ai")

# Função associada ao botão "Cadastrar Pedidos"
def clique_2():
    # Você pode adicionar a lógica para cadastrar pedidos aqui
    print("isso ai 2")
