import tkinter as tk #Importa o módulo tkinter e o renomeia como "tk"
from tkinter import ttk #Importa o módulo ttk do tkinter
from tkinter import messagebox #Importa a funcionalidade de caixas de diálogo de mensagem

#Função para criar o menu de opções
def criar_menu():
    #Importa a função "entrar" do módulo "Atelie"
    from Atelie import entrar
    
    #Função para abrir a tela de clientes cadastrados
    def abrir_clientes_cadastrados():
        messagebox.showinfo("Clientes Cadastrados", "Aqui estão os clientes cadastrados.")

    #Função para abrir a tela de cadastro de clientes
    def abrir_cadastrar_clientes():
        messagebox.showinfo("Cadastrar Clientes", "Abra a tela de cadastro de clientes aqui.")

    #Função para abrir a tela de pedidos
    def abrir_pedidos():
        #Importa a função "pedidos" do módulo "pedidos"
        from pedidos import pedidos
        messagebox.showinfo("Pedidos", "Aqui estão os pedidos.")

    #Criar a janela principal do menu
    menu_opcoes = tk.Tk()
    menu_opcoes.title("Menu de Pedidos") #Define o título da janela
    menu_opcoes.geometry("400x200")  #Define as dimensões da janela para 400x200 pixels

    #Criar a barra superior com o nome "Menu de Pedidos"
    barra_superior = ttk.Label(menu_opcoes, text="Menu de Pedidos", font=("Helvetica", 14))
    barra_superior.pack(side="top", fill="x") #Coloca a barra superior na parte superior da janela

    #Botão para acessar "Clientes Cadastrados"
    botao_clientes_cadastrados = ttk.Button(menu_opcoes, text="Clientes Cadastrados", command=abrir_clientes_cadastrados)
    botao_clientes_cadastrados.pack(pady=20) #Coloca o botão na janela com preenchimento abaixo

    #Botão para acessar "Cadastrar Clientes"
    botao_cadastrar_clientes = ttk.Button(menu_opcoes, text="Cadastrar Clientes", command=abrir_cadastrar_clientes)
    botao_cadastrar_clientes.pack()  # Coloca o botão na janela

    #Botão para acessar "Pedidos"
    botao_pedidos = ttk.Button(menu_opcoes, text="Pedidos", command=abrir_pedidos)
    botao_pedidos.pack(pady=20)  # Coloca o botão na janela com preenchimento abaixo

    #Iniciar o loop principal da janela
    menu_opcoes.mainloop()  # Inicia o loop principal da interface gráfica

# Esta parte do código não está em uso, então pode ser removida
# def fechar():
#     exit()
