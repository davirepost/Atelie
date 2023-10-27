import tkinter as tk
from tkinter import ttk

# Função para realizar a pesquisa de clientes

def pesquisar_cliente():
    termo_pesquisa = entry_pesquisa.get()
    resultados = {}

    # Simulação de busca em um banco de dados (substitua isso com sua lógica de busca real)
    # Neste exemplo, usaremos uma lista simulada de clientes
    clientes = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah"]
    #colocar botão de voltar e etc.
    for cliente in clientes:
        if termo_pesquisa.lower() in cliente.lower():
            inicial = cliente[0].upper()  # Obter a letra inicial do nome do cliente
            if inicial not in resultados:
                resultados[inicial] = []
            resultados[inicial].append(cliente)

    atualizar_lista(resultados)

# Função para atualizar a lista de clientes
def atualizar_lista(clientes):
    lista_clientes.delete(0, "end")
    for inicial, nomes in clientes.items():
        lista_clientes.insert("end", inicial)
        for nome in nomes:
            lista_clientes.insert("end", f" - {nome}")

# Criar a janela principal
root = tk.Tk()
root.title("Clientes Cadastrados")
root.geometry("1000x600")

# Título
titulo_label = ttk.Label(root, text="Clientes Cadastrados", font=("Arial", 16))
titulo_label.pack(pady=10)

# Barra de pesquisa
frame_pesquisa = ttk.Frame(root)
frame_pesquisa.pack(pady=10)

entry_pesquisa = ttk.Entry(frame_pesquisa)
entry_pesquisa.grid(row=0, column=0)

botao_pesquisa = ttk.Button(frame_pesquisa, text="Pesquisar", command=pesquisar_cliente)
botao_pesquisa.grid(row=0, column=1)

# Lista de clientes
lista_clientes = tk.Listbox(root)
lista_clientes.pack(fill="both", expand=True)

# Inicializar a lista com todos os clientes
clientes_iniciais = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah"]
clientes_iniciais_ordenados = {}
for cliente in clientes_iniciais:
    inicial = cliente[0].upper()
    if inicial not in clientes_iniciais_ordenados:
        clientes_iniciais_ordenados[inicial] = []
    clientes_iniciais_ordenados[inicial].append(cliente)

atualizar_lista(clientes_iniciais_ordenados)

# Iniciar o loop principal da janela
root.mainloop()
