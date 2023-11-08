import tkinter as tk  # Importa o módulo tkinter e o renomeia como "tk"
from tkinter import ttk  # Importa o módulo ttk do tkinter
import mysql.connector  # Importa o módulo mysql.connector para interagir com o MySQL
import style as st  # Importa um módulo chamado "style" como "st"
from PIL import Image, ImageTk  # Importa as classes Image e ImageTk do módulo PIL
import Cadastro_fun  # Importa o módulo "Cadastro_fun"

def bem_vindo(): #Função Login
    from login import tela_login  # Importa a função "tela_login" do módulo "login"
    from Cadastro_fun import cadastrar  # Importa a função "cadastrar" do módulo "Cadastro_fun"
    tela_bem_vindo = tk.Tk()  # Cria uma instância da classe Tk do tkinter e atribui a ela a variável "tela_bem_vindo"
    tela_bem_vindo.geometry('1000x600')  # Define a geometria da janela para 1000x600 pixels
    tela_bem_vindo.title("BEM VINDO(A)")  # Define o título da janela como "BEM VINDO(A)"
    texto = ttk.Label(tela_bem_vindo, text="Seja Bem Vindo(a) ao Ateliê da Iara Reis!!")  # Cria um rótulo com o texto especificado
    texto.grid(column=0, row=0)  #Coloca o rótulo na janela usando o sistema de grade
  
    def chamar():
        tela_bem_vindo.withdraw() #Esconde a janela de boas-vindas
        tela_login() #Chama a função "tela_login" do módulo "login"

    botao = ttk.Button(tela_bem_vindo, text="Login", command=chamar) # Cria um botão com o texto "Login" e define a função a ser chamada quando o botão for clicado
    botao.grid(padx=10, pady=10) #Coloca o botão na janela com preenchimento nas margens

    botao = ttk.Button(tela_bem_vindo, text="Cadastrar Novo Funcionário", command=cadastrar) #Cria um botão com o texto "Cadastrar Novo Funcionário" e define a função a ser chamada quando o botão for clicado
    botao.grid(padx=10, pady=10) #Coloca o botão na janela com preenchimento nas margens

    tela_bem_vindo.mainloop() #Inicia o loop principal da interface gráfica

def entrar():
    from Menu import menu_opcoes #Importa a função "menu_opcoes" do módulo "Menu"
    menu_opcoes() #Chama a função "menu_opcoes"

def cadastrar_fun():
    #tela_bem_vindo.withdraw() #Ttentativa de ocultar a janela de boas-vindas
    cadastrar_fun() #Chama a função "cadastrar_fun" (potencialmente recursão infinita, deve ser revisada) #ATENÇÃO

def fechar():
    exit()  #Fecha o programa quando chamado
    
#ATENÇÃO NA LINHA 35 
