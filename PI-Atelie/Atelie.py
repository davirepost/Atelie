import tkinter as tk
from tkinter import ttk
import mysql.connector 
import style as st
from PIL import Image, ImageTk
import Cadastro_fun


def bem_vindo():
    from login import tela_login
    from Cadastro_fun import cadastrar
    tela_bem_vindo= tk.Tk()
    tela_bem_vindo.geometry('1000x600')
    tela_bem_vindo.title("BEM VINDO(A)")
    texto=ttk.Label (tela_bem_vindo, text="Seja Bem Vindo(a) ao Ateliê da Iara Reis!!")
    texto.grid(column=0, row=0)
  
    def chamar():
        tela_bem_vindo.withdraw()
        tela_login()

    botao= ttk.Button(tela_bem_vindo, text="Login", command= chamar)
    botao.grid(padx=10, pady=10)

    botao= ttk.Button(tela_bem_vindo, text="Cadastrar Novo Funcionário", command= cadastrar)
    botao.grid(padx=10, pady=10)


    tela_bem_vindo.mainloop()


def entrar():
    from Menu import menu_opcoes
    menu_opcoes()


def cadastrar_fun():
    #tela_bem_vindo.withdraw()
    cadastrar_fun()


def fechar():
    exit()
    






