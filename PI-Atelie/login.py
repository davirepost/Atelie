
import tkinter as tk
import customtkinter as Ctk
from customtkinter import CTk
from tkinter import ttk


def tela_login():
    from Atelie import bem_vindo
    from Menu import criar_menu
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
    botao= ttk.Button(login, text="Voltar", command=fechar)
    botao.grid(padx=10, pady=10)

 

    login.mainloop()

def criar_menu():
    from Menu import criar_menu
   

def fechar():
    exit()

