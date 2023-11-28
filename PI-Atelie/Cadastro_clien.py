import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

def confirmar_cadastro(nome_var, endereco_var, telefone_var, gola_var, busto_var, cintura_var, largura_ombro_var, manga_var, quadril_var, coxa_var, outros_var):
    # Inicializa a conexão com o banco de dados e o cursor
    conexao = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user='root',
        password='',
        database='atelie'
    )
    cursor = conexao.cursor()

    nome = nome_var.get()
    endereco = endereco_var.get()
    telefone = telefone_var.get()
    gola= gola_var.get()
    busto= busto_var.get()
    cintura= cintura_var.get()
    largura_ombro= largura_ombro_var.get()
    manga= manga_var.get()
    quadril= quadril_var.get()
    coxa= coxa_var.get()
    outros=outros_var.get()
    
    if not nome or not endereco or not telefone:
        messagebox.showerror("Erro", "Preencha todos os campos obrigatórios.")
        return

    try:
        comando = "INSERT INTO `cliente`(`nome`, `endereco`, `telefone`, `gola`, `busto`, `cintura`, `largura_ombro`, `manga`, `quadril`, `coxa`, `outros`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        values = (nome, endereco, telefone, gola, busto, cintura, largura_ombro, manga, quadril, coxa, outros)
        cursor.execute(comando, values)
        conexao.commit()
        messagebox.showinfo("Cadastro Confirmado", "Cadastro efetuado com sucesso.")
    except mysql.connector.Error as err:
        messagebox.showerror("Erro no Banco de Dados", f"Erro: {err}")

def abrir_medidas():
    medidas_window = tk.Toplevel()
    medidas_window.title("Medidas do Cliente")

    medidas_frame = ttk.Frame(medidas_window)
    medidas_frame.pack(padx=20, pady=20)

    labels = ["Gola", "Busto", "Cintura", "Largura do Ombro", "Manga", "Quadril", "Coxa", "Outros"]
    variables = [tk.StringVar() for _ in range(len(labels))]

    for row, label in enumerate(labels, start=1):
        ttk.Label(medidas_frame, text=f"{label}:").grid(row=row, column=0, sticky="w")
        ttk.Entry(medidas_frame, textvariable=variables[row-1]).grid(row=row, column=1, sticky="w")

    ttk.Button(medidas_window, text="Salvar", command=lambda: salvar_medidas(*variables)).pack(pady=10)

def salvar_medidas(*variables):
    # Adapte conforme necessário para processar e salvar as medidas
   messagebox.showerror("medidas salvas com sucesso")

def main():
    root = tk.Tk()
    root.title("Cadastro de Clientes")
    root.geometry("1000x600")

    frame_campos = ttk.Frame(root)
    frame_campos.pack(padx=20, pady=20)

    nome_var = tk.StringVar()
    endereco_var = tk.StringVar()
    telefone_var = tk.StringVar()

    gola_var = tk.StringVar()
    busto_var = tk.StringVar()
    cintura_var = tk.StringVar()
    largura_ombro_var = tk.StringVar()
    manga_var = tk.StringVar()
    quadril_var = tk.StringVar()
    coxa_var = tk.StringVar()
    outros_var = tk.StringVar()

    titulo_label = ttk.Label(frame_campos, text="Cadastro de Clientes", font=("Arial", 16))
    titulo_label.grid(row=0, column=0, columnspan=2, pady=10)

    campos = [
        ("Nome:", nome_var, 1),
        ("Endereço:", endereco_var, 3),
        ("Telefone:", telefone_var, 2),
    ]

    for label_text, var, row in campos:
        ttk.Label(frame_campos, text=label_text).grid(row=row, column=0, sticky="w")
        ttk.Entry(frame_campos, textvariable=var).grid(row=row, column=1, sticky="w")

    botao_medidas = ttk.Button(frame_campos, text="Medidas", command=abrir_medidas)
    botao_medidas.grid(row=4, column=0, columnspan=2, pady=10)

    botao_confirmar = ttk.Button(frame_campos, text="Confirmar Cadastro",
                                 command=lambda: confirmar_cadastro(nome_var, endereco_var, telefone_var,
                                                                    gola_var, busto_var, cintura_var,
                                                                    largura_ombro_var, manga_var, quadril_var,
                                                                    coxa_var, outros_var))
    botao_confirmar.grid(row=5, column=0, columnspan=2)

    botao_cancelar = ttk.Button(frame_campos, text="Cancelar Cadastro", command=root.destroy)
    botao_cancelar.grid(row=6, column=0, columnspan=2)

    root.mainloop()

if __name__ == "__main__":
    main()
