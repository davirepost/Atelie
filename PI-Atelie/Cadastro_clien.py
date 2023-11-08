import tkinter as tk  #Importa o módulo tkinter e o renomeia como "tk"
from tkinter import ttk  #Importa o módulo ttk do tkinter
from tkinter import messagebox  #Importa a funcionalidade de caixas de diálogo de mensagem

# Função para salvar medidas
def salvar_medidas():
    from Menu import abrir_cadastrar_clientes  #Importa a função "abrir_cadastrar_clientes" do módulo "Menu"
    global medidas_window  #Declara a variável "medidas_window" como global
    medidas_window.destroy()  #Fecha a janela de medidas

# Função para abrir a janela de medidas
def abrir_medidas():
    global medidas_window #Declara a variável "medidas_window" como global
    medidas_window = tk.Toplevel()  #Cria uma nova janela de nível superior
    medidas_window.title("Medidas do Cliente") #Define o título da janela

    # Labels e campos de entrada para medidas
    medidas_frame = ttk.Frame(medidas_window) #Cria um frame para organizar os widgets
    medidas_frame.pack(padx=10, pady=10) #coloca o frame na janela com preenchimento nas margens

    # Labels e campos de entrada para medidas
    ttk.Label(medidas_frame, text="Gola:").grid(row=0, column=0, sticky="w") #Cria um rótulo e um campo de entrada para "Gola"
    ttk.Entry(medidas_frame).grid(row=0, column=1) #Cria um campo de entrada para "Gola"

    # Repita o mesmo padrão para outros campos de medidas (Busto, Cintura, Largura do Ombro, Manga, Quadril, Coxa, Outros)

    ttk.Button(medidas_window, text="Salvar", command=salvar_medidas).pack(pady=10)  # Cria um botão "Salvar" na janela de medidas

#Função para confirmar o cadastro
def confirmar_cadastro():
    nome = entry_nome.get()
    telefone = entry_telefone.get()
    endereco = entry_endereco.get()

    #Validação dos campos
    if not nome:
        messagebox.showerror("Erro", "Insira o nome do cliente!")
        return

    if not telefone:
        messagebox.showerror("Erro", "Insira o telefone do cliente!")
        return

    if not endereco:
        messagebox.showerror("Erro", "Insira o endereço do cliente!")
        return

    #Se todas as validações passarem, exibir mensagem de sucesso
    messagebox.showinfo("Cadastro Confirmado", "Cadastro de cliente efetuado com sucesso.")

#Função para cancelar o cadastro
def cancelar_cadastro():
    nome_var.set("")
    telefone_var.set("")
    endereco_var.set("")

#Criar a janela principal
root = tk.Tk()
root.title("Cadastro de Clientes")

#Definir a dimensão da tela
root.geometry("1000x600")

#Centralizar os campos de preenchimento
frame_campos = ttk.Frame(root)
frame_campos.place(relx=0.5, rely=0.5, anchor="center")

#Variáveis de controle para os campos
nome_var = tk.StringVar()
telefone_var = tk.StringVar()
endereco_var = tk.StringVar()

#Título
titulo_label = ttk.Label(frame_campos, text="Cadastro de Clientes", font=("Arial", 16))
titulo_label.grid(row=0, column=0, columnspan=2, pady=10)

# Labels e campos de entrada
label_nome = ttk.Label(frame_campos, text="Nome:")
label_nome.grid(row=1, column=0, sticky="w")
entry_nome = ttk.Entry(frame_campos, textvariable=nome_var)
entry_nome.grid(row=1, column=1, sticky="w")

label_telefone = ttk.Label(frame_campos, text="Telefone:")
label_telefone.grid(row=2, column=0, sticky="w")
entry_telefone = ttk.Entry(frame_campos, textvariable=telefone_var)
entry_telefone.grid(row=2, column=1, sticky="w")

label_endereco = ttk.Label(frame_campos, text="Endereço:")
label_endereco.grid(row=3, column=0, sticky="w")
entry_endereco = ttk.Entry(frame_campos, textvariable=endereco_var)
entry_endereco.grid(row=3, column=1, sticky="w")

# Botão de medidas
botao_medidas = ttk.Button(frame_campos, text="Medidas", command=abrir_medidas)
botao_medidas.grid(row=4, column=0, columnspan=2, pady=10)

# Botões de ação
botao_confirmar = ttk.Button(frame_campos, text="Confirmar Cadastro", command=confirmar_cadastro)
botao_confirmar.grid(row=5, column=0, columnspan=2)

botao_cancelar = ttk.Button(frame_campos, text="Cancelar Cadastro", command=cancelar_cadastro)
botao_cancelar.grid(row=6, column=0, columnspan=2)

# Iniciar o loop principal da janela
root.mainloop()
