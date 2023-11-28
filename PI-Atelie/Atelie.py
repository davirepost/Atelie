import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from login import tela_login
from Cadastro_fun import cadastrar


def bem_vindo():
    tela_bem_vindo = tk.Tk()
    tela_bem_vindo.geometry('1000x600')
    tela_bem_vindo.title("BEM VINDO(A)")
    texto = ttk.Label(tela_bem_vindo, text="Seja Bem Vindo(a) ao Ateliê da Iara Reis!!")
    texto.grid(column=0, row=0)
    #img= ttk.PhotoImage (file= "iara.jpg")
    #label_imagem= ttk.Label(tela_bem_vindo, image=img).pack()


    def chamar():
        tela_bem_vindo.withdraw()
        tela_login()

    def abrir_cadastro():
       # tela_bem_vindo.destroy()  # Fecha a tela de boas-vindas
        cadastrar()


    botao = ttk.Button(tela_bem_vindo, text="Login", command=chamar)
    botao.grid(padx=10, pady=10)

    botao_cadastrar = ttk.Button(tela_bem_vindo, text="Cadastrar Novo Funcionário", command=abrir_cadastro)
    botao_cadastrar.grid(padx=10, pady=10)

    tela_bem_vindo.protocol("WM_DELETE_WINDOW", fechar)
    tela_bem_vindo.mainloop()

def entrar():
    from Menu import menu_opcoes
    menu_opcoes()

def fechar():
    exit()

bem_vindo()
