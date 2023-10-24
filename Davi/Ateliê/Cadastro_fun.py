import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os

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
    if senha_checkbox.get():
        entry_senha.config(show="")
    else:
        entry_senha.config(show="*")

# Criar a janela principal
root = tk.Tk()
root.title("Cadastro de Funcionário")

# Configurar a geometria para preencher toda a tela
root.geometry("800x400")

# Título
titulo_label = ttk.Label(root, text="Cadastro de Funcionário", font=("Arial", 16))
titulo_label.pack(pady=10)

# Frame para organizar os campos usando o gerenciador de layout 'grid'
frame = ttk.Frame(root)
frame.pack(pady=10)

# Labels e campos de entrada organizados com o gerenciador de layout 'grid'
label_nome = ttk.Label(frame, text="Nome:")
label_nome.grid(row=0, column=0, sticky="w")
entry_nome = ttk.Entry(frame)
entry_nome.grid(row=0, column=1, sticky="w")

label_email = ttk.Label(frame, text="Email:")
label_email.grid(row=1, column=0, sticky="w")
entry_email = ttk.Entry(frame)
entry_email.grid(row=1, column=1, sticky="w")

label_senha = ttk.Label(frame, text="Senha:")
label_senha.grid(row=2, column=0, sticky="w")
entry_senha = ttk.Entry(frame, show="*")
entry_senha.grid(row=2, column=1, sticky="w")

# Criar um IntVar para rastrear o estado do checkbox
senha_checkbox = tk.BooleanVar()

# Botão para alternar a visibilidade da senha
mostrar_senha_button = ttk.Checkbutton(frame, text="Mostrar Senha", variable=senha_checkbox, command=alternar_visibilidade_senha)
mostrar_senha_button.grid(row=3, column=0, columnspan=2, sticky="w")

label_confirm_senha = ttk.Label(frame, text="Confirmar Senha:")
label_confirm_senha.grid(row=4, column=0, sticky="w")
entry_confirm_senha = ttk.Entry(frame, show="*")
entry_confirm_senha.grid(row=4, column=1, sticky="w")

# Adicione espaço entre os widgets
espaco_entre_widget = ttk.Label(root, text="", padding=6)
espaco_entre_widget.pack()

# Botão para confirmar o cadastro com cor azul
botao_confirmar = ttk.Button(root, text="Confirmar Cadastro", command=confirmar_cadastro, style="TButton")
botao_confirmar.pack()

# Configure o estilo para tornar o botão azul
style = ttk.Style()
style.configure("TButton", background="blue")

# Configurar a coluna 1 para preencher a largura da tela
frame.columnconfigure(1, weight=1)

# Iniciar o loop principal da janela
root.mainloop()