import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

def atualizar_f():
    conexao = mysql.connector.connect(
            host="127.0.0.1",
            port=3306,
            user='root',
            password='',
            database='atelie'
)

    def atualizar_fun(novo_email, nova_senha, id_funcionario):
        
            cursor = conexao.cursor()
        
        # Execute a instrução SQL para atualizar os dados do funcionário
            comando = "UPDATE funcionario SET email = %s, senha = %s WHERE id_funcionario = %s"
            cursor.execute(comando, (novo_email, nova_senha, id_funcionario))
            conexao.commit()
            resultado = cursor.fetchall()

            if resultado:
                messagebox.showinfo("Dados do Funcionário Atualizados", "Os dados do funcionário foram atualizados com sucesso.")
    
            
                cursor.close()


# Crie a janela principal
    root = tk.Tk()
    root.title("Atualizar Dados do Funcionário")
    root.geometry("1000x600")

    # Crie um botão para atualizar os dados do funcionário
    botao_atualizar_funcionario = ttk.Button(root, text="Atualizar Dados do Funcionário", command=atualizar_fun)
    botao_atualizar_funcionario.pack(pady=20)

    # Inicie o loop principal da janela
    root.mainloop()