import tkinter as tk
from tkinter import ttk
import mysql.connector 
import funcoes as f
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
    #imagem na tela de bem-vindo
    #img= file= "testeii.png"
    #label_img= ttk.Label(master=tela_bem_vindo, image=img)
    #label_img.place(x=5, y=65)
    # Carregar a imagem
    #image_url = "https://img.freepik.com/vetores-gratis/cartaz-publicitario-do-atelie-de-roupas-com-endereco-numero-de-telefone-e-data-de-inauguracao_98292-7821.jpg?w=2000"
    #image = Image.open("image.jpg")  # Salvar a imagem localmente (ou baixá-la para sua pasta de trabalho)

    # Redimensionar a imagem se necessário
    #image = image.resize((400, 400), Image.ANTIALIAS)

    # Converter a imagem para um formato adequado para exibição em Tkinter
    #tk_image = ImageTk.PhotoImage(image)

    # Criar um rótulo para a imagem e exibi-lo à direita
    #image_label = ttk.Label(tela_bem_vindo, image=tk_image)
    #image_label.image = tk_image
    #image_label.pack(side="right", padx=10, pady=10, fill="both", expand=True)

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
    from Cadastro_fun import cadastrar

def fechar():
     exit()








