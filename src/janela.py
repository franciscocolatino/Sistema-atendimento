import customtkinter
import tkinter
from Fila import Fila
 
fila = Fila()

def iniciar_tela():
    janela.mainloop()

def mostrar_proximo():
    proximo = fila.remover()
    if not proximo.__contains__("error"):
        label_proximo.configure(text=f"Posição: {proximo['posição']}")
        label_nome.configure(text=f"Nome: {proximo['nome']}")
        label_cpf.configure(text=f"Cpf: {proximo['cpf']}")
    else:
        label_proximo.configure(text=f"Próximo: {proximo['error']}")
        label_nome.configure(text="")
        label_cpf.configure(text="")

def abrir_modal_cadastro():
    modal = customtkinter.CTkToplevel(janela)
    modal.geometry("300x200")
    modal.title("Cadastrar Nova Chegada")
    
    label_nome = customtkinter.CTkLabel(modal, text="Nome:")
    label_nome.pack(pady=(10,5))
    
    entry_nome = customtkinter.CTkEntry(modal, width=200, placeholder_text="Insira o nome")
    entry_nome.pack()
    
    label_cpf = customtkinter.CTkLabel(modal, text="CPF:")
    label_cpf.pack(pady=(10,5))
    
    entry_cpf = customtkinter.CTkEntry(modal, width=200, placeholder_text="Insira o CPF")
    entry_cpf.pack()
    
    def confirmar_cadastro():
        nome = entry_nome.get()
        cpf = entry_cpf.get()
        dados = {"nome": nome, "cpf": cpf}
        result = fila.inserir(dados)
        label_cadastro_nome.configure(text=f"Nome: {result['nome']}")
        modal.destroy()
    
    botao_confirmar = customtkinter.CTkButton(modal, text="Confirmar", command=confirmar_cadastro)
    botao_confirmar.pack(pady=20)

def abrir_modal_todos():
    modal = customtkinter.CTkToplevel(janela)
    modal.geometry("400x300")
    modal.title("Lista de Espera")

    frame = customtkinter.CTkFrame(modal)
    frame.pack(fill="both", expand=True)

    scrollbar = customtkinter.CTkScrollbar(frame, orientation="vertical")
    scrollbar.pack(side="right", fill="y")

    lista_espera = tkinter.Listbox(frame, yscrollcommand=scrollbar.set)
    scrollbar.configure(command=lista_espera.yview)

    for item in fila.nao_atendidos(): 
        lista_espera.insert("end", f"{item['posição']} - Nome: {item['nome']}, CPF: {item['cpf']}")

    lista_espera.pack(side="left", fill="both", expand=True)

janela = customtkinter.CTk()
janela.geometry("600x400") 
janela.title("Sistema de Atendimento")

texto = customtkinter.CTkLabel(janela, text="Sistema de Atendimento", font=("Roboto", 16))
texto.pack(pady=20)

botao_proximo = customtkinter.CTkButton(janela, text="Próximo", command=mostrar_proximo, width=200, height=40) 
botao_proximo.pack(pady=(0,10))

label_proximo = customtkinter.CTkLabel(janela, text="Próximo: ")
label_nome = customtkinter.CTkLabel(janela, text="Nome: ")
label_cpf = customtkinter.CTkLabel(janela, text="CPF: ")
label_proximo.pack()
label_nome.pack()
label_cpf.pack()

botao_cadastro = customtkinter.CTkButton(janela, text="Cadastrar Chegada", command=abrir_modal_cadastro, width=200, height=40)  
botao_cadastro.pack(pady=(20,10))

label_cadastro = customtkinter.CTkLabel(janela, text="Último Cadastrado: ")
label_cadastro_nome = customtkinter.CTkLabel(janela, text="")
label_cadastro.pack()
label_cadastro_nome.pack()

botao_mostrar_todos = customtkinter.CTkButton(janela, text="Mostrar Todos", command=abrir_modal_todos, width=200, height=40)
botao_mostrar_todos.pack(pady=(20,10))
