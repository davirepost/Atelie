import tkinter as tk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from Menu import criar_menu
# Estabelece a conexão com o banco de dados MySQL
def tela_login():
    conexao = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user='root',
        password='',
        database='atelie'
    )

    cursor = conexao.cursor()  # Cria um cursor para executar comandos SQL

# Função para confirmar o login
    def confirmar_login():
        email_digitado = entry_email.get()
        senha_digitada = entry_senha.get()

        comando = "SELECT * FROM `funcionario` WHERE email = %s AND senha = %s"
        cursor.execute(comando, (email_digitado, senha_digitada))
        resultado = cursor.fetchall()

        if email_digitado in cursor:
            # Se houver resultados na consulta, o login é bem-sucedido
            messagebox.showinfo("Login bem-sucedido", "Bem-vindo!")
            login.withdraw()
            criar_menu()
        if email_digitado not in cursor:
            # Se não houver resultados, as credenciais são inválidas
            messagebox.showerror("Erro", "Credenciais inválidas")


    # Cria a janela de login
        login = tk.Tk()
        login.geometry("1000x600")
        login.title('Área de Login, Bem-Vindo!!')

        texto = ttk.Label(login, text="Faça seu Login", font="Arial")
        texto.grid(padx=10, pady=10)

        entry_email = ttk.Entry(login, text="Digite Seu Email")
        entry_email.grid(padx=10, pady=10)

        entry_senha = ttk.Entry(login,text= "Digite Sua Senha" ,show="*")
        entry_senha.grid(padx=10, pady=10)

        checkbox = ttk.Checkbutton(login, text="Lembrar Login")
        checkbox.grid(padx=10, pady=10)

        def entrar():
            login.withdraw()
            criar_menu()
        botao = ttk.Button(login, text="Entrar", command=entrar)
        botao.grid(padx=10, pady=10)

    

        login.mainloop()
