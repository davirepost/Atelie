import tkinter as tk  # Importa o módulo tkinter e o renomeia como "tk"
from tkinter import ttk #Importa o módulo ttk do tkinter
import mysql.connector #Importa o módulo mysql.connector para interagir com o MySQL

#Função para criar a tela de login
def tela_login():
    #Estabelece a conexão com o banco de dados MySQL
    conexao = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user='root',
        password='',
        database='atelie'
    )
    
    cursor = conexao.cursor() #Cria um cursor para executar comandos SQL

    #Função para confirmar o login
    def confirmar_login():
        comando = "SELECT * FROM `funcionario`"
        cursor.execute(comando)
        resultado = cursor.fetchall()
        conexao.commit()

        login = tk.Tk() #Cria uma instância da classe Tk do tkinter para a tela de login
        login.geometry("1000x600") #Define as dimensões da janela de login
        login.title('Área de Login, Bem-Vindo!!') #Define o título da janela

        texto = ttk.Label(login, text="Faça seu Login", font="Arial") #Cria um rótulo com um texto
        texto.grid(padx=10, pady=10) #Coloca o rótulo na janela

        email = ttk.Entry(login, text="Digite seu email") #Cria um campo de entrada para o email
        email.grid(padx=10, pady=10) #Coloca o campo de entrada na janela

        senha = ttk.Entry(login, text="Digite sua senha", show="*") #Cria um campo de entrada para a senha com visibilidade mascarada
        senha.grid(padx=10, pady=10) #Coloca o campo de entrada na janela

        checkbox = ttk.Checkbutton(login, text="Lembrar Login") #Cria uma caixa de seleção para lembrar o login
        checkbox.grid(padx=10, pady=10) #Coloca a caixa de seleção na janela

        botao = ttk.Button(login, text="Entrar", command=chamar_tela) #Cria um botão "Entrar" com a ação de chamar a tela do menu
        botao.grid(padx=10, pady=10) #Coloca o botão na janela

        conexao.close() #Fecha a conexão com o banco de dados
        login.mainloop() #Inicia o loop principal da interface gráfica da tela de login

#Função para chamar a tela do menu
def chamar_tela():
    criar_menu()

def criar_menu():
    from Menu import criar_menu  #Importa a função "criar_menu" do módulo "Menu"

#def fechar():
#exit()
