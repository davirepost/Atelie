import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import os

def cadastrar():
    conexao = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user='root',
        password='',
        database='atelie'
    )
    
    cursor = conexao.cursor()

    def confirmar_cadastro():
        nome = entry_nome.get()
        email = entry_email.get()
        senha = entry_senha.get()
        confirm_senha = entry_confirm_senha.get()

        if not nome:
            messagebox.showerror("Erro", "Insira seu nome!")
            return

        if not email:
            messagebox.showerror("Erro", "Digite seu email!")
            return

        if not senha:
            messagebox.showerror("Erro", "Digite sua senha!")
            return

        if senha != confirm_senha:
            messagebox.showerror("Erro", "A senha digitada não é compatível.")
            return
        
        try:

            comando = "INSERT INTO `funcionario` (`nome`, `email`, `senha`) VALUES (%s, %s, %s)"
            values = (nome, email, senha)
            cursor.execute(comando, values)
            conexao.commit()
            messagebox.showinfo("Cadastro Confirmado", "Cadastro efetuado com sucesso.")

        except mysql.connector.Error as err:
            messagebox.showerror("Erro no Banco de Dados", f"Erro: {err}")
        finally:
            cursor.close()
            conexao.close()

    def alternar_visibilidade_senha():
        if entry_senha.cget("show") == "":
            entry_senha.config(show="*")
        else:
            entry_senha.config(show="")

    root = tk.Tk()
    root.title("Cadastro de Funcionário")
    root.geometry("1000x600")

    titulo_label = ttk.Label(root, text="Cadastro de Funcionário", font=("Helvetica", 16))
    titulo_label.pack(pady=10)

    frame = ttk.Frame(root)
    frame.pack()

    label_nome = ttk.Label(frame, text="Nome:")
    label_nome.grid(row=0, column=0, sticky="w")
    entry_nome = ttk.Entry(frame)
    entry_nome.grid(row=0, column=1)

    label_email = ttk.Label(frame, text="Email:")
    label_email.grid(row=1, column=0, sticky="w")
    entry_email = ttk.Entry(frame)
    entry_email.grid(row=1, column=1)

    label_senha = ttk.Label(frame, text="Senha:")
    label_senha.grid(row=2, column=0, sticky="w")
    entry_senha = ttk.Entry(frame, show="*")
    entry_senha.grid(row=2, column=1)

    mostrar_senha_button = ttk.Button(frame, text="Mostrar Senha", command=alternar_visibilidade_senha)
    mostrar_senha_button.grid(row=2, column=2)

    label_confirm_senha = ttk.Label(frame, text="Confirmar Senha:")
    label_confirm_senha.grid(row=3, column=0, sticky="w")
    entry_confirm_senha = ttk.Entry(frame, show="*")
    entry_confirm_senha.grid(row=3, column=1)

    espaco_entre_widget = ttk.Label(root, text="", padding=6)
    espaco_entre_widget.pack()

    botao_confirmar = ttk.Button(root, text="Confirmar Cadastro", command=confirmar_cadastro)
    botao_confirmar.pack()


    root.mainloop()
