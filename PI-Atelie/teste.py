import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

def confirmar_cadastro():
    conexao = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user='root',
        password='',
        database='atelie'
    )
    cursor = conexao.cursor()

    def salvar_medidas():
        nome = entry_nome.get()
        endereco = entry_endereco.get()
        telefone = entry_telefone.get()
        gola = gola_var.get()
        busto = busto_var.get()
        cintura = cintura_var.get()
        largura_ombro = largura_ombro_var.get()
        manga = manga_var.get()
        quadril = quadril_var.get()
        coxa = coxa_var.get()
        outros = outros_var.get()
        if not nome:
                messagebox.showerror("Erro", "Insira seu nome!")
                return

        if not endereco:
                messagebox.showerror("Erro", "Digite seu endereço!")
                return

        if not telefone:
                messagebox.showerror("Erro", "Digite seu telefone!")
                return

        if not gola: 
                messagebox.showerror("Erro","Digite a gola")
                return
            
        if not busto: 
                messagebox.showerror("Erro","Digite o busto")
                return
            
        if not cintura: 
                messagebox.showerror("Erro","Digite a medida da cintura")
                return
            
        if not largura_ombro: 
                messagebox.showerror("Erro","Digite a medida da largura do ombro")
                return
            
        if not manga: 
                messagebox.showerror("Erro","Digite a medida da manga")
                return
            
        if not quadril: 
                messagebox.showerror("Erro","Digite a medida do quadril")
                return
            
        if not coxa: 
                messagebox.showerror("Erro","Digite a medida da coxa")
                return
            
        if not outros: 
                messagebox.showerror("Erro")
                return
            
        try:
                comando = "INSERT INTO `cliente`( `nome`, `endereco`, `telofone`, `gola`, `busto`, `cintura`, `largura_ombro`, `manga`, `quadril`, `coxa`, `outros`) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',%s'')"
                values = (nome, endereco, telefone, gola, busto, cintura, largura_ombro, manga, quadril, coxa, outros )
                cursor.execute(comando, values)
                conexao.commit()
                messagebox.showinfo("Cadastro Confirmado", "Cadastro efetuado com sucesso.")
        except mysql.connector.Error as err:
                messagebox.showerror("Erro no Banco de Dados", f"Erro: {err}")


    def abrir_medidas():
        global medidas_window
        medidas_window = tk.Toplevel()
        medidas_window.title("Medidas do Cliente")

        medidas_frame = ttk.Frame(medidas_window)
        medidas_frame.pack(padx=20, pady=20)

        ttk.Label(medidas_frame, text="Gola:").grid(row=1, column=0, sticky="w")
        ttk.Entry(medidas_frame, textvariable=gola_var).grid(row=1, column=1)

        ttk.Label(medidas_frame, text="Busto:").grid(row=2, column=0, sticky="w")
        ttk.Entry(medidas_frame, textvariable=busto_var).grid(row=2, column=1)

        ttk.Label(medidas_frame, text="Cintura:").grid(row=3, column=0, sticky="w")
        ttk.Entry(medidas_frame, textvariable=cintura_var).grid(row=3, column=1)

        ttk.Label(medidas_frame, text="Largura do Ombro:").grid(row=4, column=0, sticky="w")
        ttk.Entry(medidas_frame, textvariable=largura_ombro_var).grid(row=4, column=1)

        ttk.Label(medidas_frame, text=" Manga:").grid(row=5, column=0, sticky="w")
        ttk.Entry(medidas_frame, textvariable=manga_var).grid(row=5, column=1)

        ttk.Label(medidas_frame, text="Quadril:").grid(row=6, column=0, sticky="w")
        ttk.Entry(medidas_frame, textvariable=quadril_var).grid(row=6, column=1)

        ttk.Label(medidas_frame, text="Coxa:").grid(row=7, column=0, sticky="w")
        ttk.Entry(medidas_frame, textvariable=coxa_var).grid(row=7, column=1)
                

        ttk.Button(medidas_frame, text="Salvar", command=salvar_medidas).grid(row=8, column=0, columnspan=2, pady=10)

    def cancelar_cadastro():
        nome_var.set("")
        telefone_var.set("")
        endereco_var.set("")

    root = tk.Tk()
    root.title("Cadastro de Clientes")
    root.geometry("1000x600")

    frame_campos = ttk.Frame(root)
    frame_campos.place(relx=0.5, rely=0.5, anchor="center")

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

    label_nome = ttk.Label(frame_campos, text="Nome:")
    label_nome.grid(row=1, column=0, sticky="w")
    entry_nome = ttk.Entry(frame_campos, textvariable=nome_var)
    entry_nome.grid(row=1, column=1, sticky="w")

    label_endereco = ttk.Label(frame_campos, text="Endereço:")
    label_endereco.grid(row=3, column=0, sticky="w")
    entry_endereco = ttk.Entry(frame_campos, textvariable=endereco_var)
    entry_endereco.grid(row=3, column=1, sticky="w")

    label_telefone = ttk.Label(frame_campos, text="Telefone:")
    label_telefone.grid(row=2, column=0, sticky="w")
    entry_telefone = ttk.Entry(frame_campos, textvariable=telefone_var)
    entry_telefone.grid(row=2, column=1, sticky="w")

    label_gola = ttk.Label(frame_campos, text="Gola:")
    label_gola.grid(row=4, column=0, sticky="w")
    entry_gola = ttk.Entry(frame_campos, textvariable=gola_var)
    entry_gola.grid(row=4, column=1, sticky="w")

    # Repita o mesmo padrão para outras medidas

    botao_medidas = ttk.Button(frame_campos, text="Medidas", command=abrir_medidas)
    botao_medidas.grid(row=5, column=0, columnspan=2, pady=10)

    botao_confirmar = ttk.Button(frame_campos, text="Confirmar Cadastro", command=confirmar_cadastro)
    botao_confirmar.grid(row=6, column=0, columnspan=2)

    botao_cancelar = ttk.Button(frame_campos, text="Cancelar Cadastro", command=cancelar_cadastro)
    botao_cancelar.grid(row=7, column=0, columnspan=2)

    root.mainloop()
