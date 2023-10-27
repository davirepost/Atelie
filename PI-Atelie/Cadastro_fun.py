import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os

def fun_bem_vindo():

    from Atelie import bem_vindo

def cadastrar():
    
    
# Função para confirmar o cadastro
    def confirmar_cadastro():
        nome = entry_nome.get()
        email = entry_email.get()
        senha = entry_senha.get()
        confirm_senha = entry_confirm_senha.get()

        # Validação do nome
        if not nome:
            messagebox.showerror("Erro", "Insira seu nome!")
            return

        # Validação do email
        if not email:
            messagebox.showerror("Erro", "Digite seu email!")
            return

        # Validação da senha
        if not senha:
            messagebox.showerror("Erro", "Digite sua senha!")
            return

        # Validação da confirmação de senha
        if senha != confirm_senha:
            messagebox.showerror("Erro", "A senha digitada não é compatível.")
            return

        # Se todas as validações passarem, exibir mensagem de sucesso
        messagebox.showinfo("Cadastro Confirmado", "Cadastro efetuado com sucesso.")

        # Redirecionar para a tela "Menu.py" (simulado)
        os.system("python Menu.py")
        root.destroy()

    # Função para alternar a visibilidade da senha
    def alternar_visibilidade_senha():
        if entry_senha.cget("show") == "":
            entry_senha.config(show="*")  # Ocultar senha
        else:
            entry_senha.config(show="")  # Mostrar senha

    # Criar a janela principal
    root = tk.Tk()
    root.title("Cadastro de Funcionário")
    root.geometry("1000x600")  # Define o tamanho da tela para 1000x600 pixels

    # Título
    titulo_label = ttk.Label(root, text="Cadastro de Funcionário", font=("Helvetica", 16))
    titulo_label.pack(pady=10)  # Adicione algum espaço vertical

    # Criação do frame para organizar os campos
    frame = ttk.Frame(root)
    frame.pack()

    # Labels e campos de entrada organizados em grid
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

    # Botão para alternar a visibilidade da senha dentro do campo de senha
    mostrar_senha_button = ttk.Button(frame, text="Mostrar Senha", command=alternar_visibilidade_senha)
    mostrar_senha_button.grid(row=2, column=2)

    label_confirm_senha = ttk.Label(frame, text="Confirmar Senha:")
    label_confirm_senha.grid(row=3, column=0, sticky="w")
    entry_confirm_senha = ttk.Entry(frame, show="*")
    entry_confirm_senha.grid(row=3, column=1)

    # Adicione espaço entre os widgets
    espaco_entre_widget = ttk.Label(root, text="", padding=6)
    espaco_entre_widget.pack()

    # Botão para confirmar o cadastro com bordas arredondadas
    botao_confirmar = ttk.Button(root, text="Confirmar Cadastro", command=confirmar_cadastro)
    botao_confirmar.pack()

    # Iniciar o loop principal da janelaa
    root.mainloop()