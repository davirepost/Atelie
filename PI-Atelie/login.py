
import tkinter as tk
import customtkinter as Ctk
from customtkinter import CTk
from tkinter import ttk
import mysql.connector


def tela_login():

    conexao = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user='root',
        password='',
        database='atelie'
    )
    
    cursor = conexao.cursor()

    def confirmar_login():
        comando= "SELECT * FROM `funcionario`"
        cursor.execute(comando)
        resultado= cursor.fetchall()
        conexao.commit()
           

        login=tk.Tk()
        login.geometry("1000x600")
        login.title ('Àrea de Login, Bem-VIndo!!')
        texto=ttk.Label(login, text="Faça seu Login", font="Arial")
        texto.grid(padx=10, pady=10)
        email= ttk.Entry(login, text="Digite seu email")
        email.grid(padx=10, pady=10)

        senha= ttk.Entry(login, text="Digite sua senha", show="*")
        senha.grid(padx=10, pady=10)
        checkbox= ttk.Checkbutton(login, text="Lembrar Login")
        checkbox.grid(padx=10, pady=10)
        
        botao= ttk.Button(login, text="Entrar", command=criar_menu)
        botao.grid(padx=10, pady=10)
        #botao= ttk.Button(login, text="Voltar", command=fechar)
        #botao.grid(padx=10, pady=10)
    
        
        conexao.close()
        login.mainloop()  

def chamar_tela():
        #tela_login.withdraw()
        criar_menu()
        
def criar_menu():
    from Menu import criar_menu
   

#def fechar():
 #   exit()

