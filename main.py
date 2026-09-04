import tkinter as tk

janela = tk.Tk()

janela.title("BookTrack")
janela.geometry("700x500")
janela.configure(bg="#1a1919")

titulo_app = tk.Label(
    janela,
    text="BookTrack",
    font=("Arial", 24, "bold"),
    bg="#1a1919",
    fg="white"
)

titulo_app.pack(pady=15)

frame_cadastro = tk.Frame(
    janela,
    bg="#1a1919"
)

frame_cadastro.pack()

frame_lista = tk.Frame(
    janela,
    bg="#1a1919"
)

label_titulo = tk.Label(
    frame_cadastro,
    text="Livro:",
    bg="#1a1919",
    fg="white"
)

label_titulo.pack()

entrada_titulo = tk.Entry(frame_cadastro)
entrada_titulo.pack()

label_autor = tk.Label(
    frame_cadastro,
    text="Autor:",
    bg="#1a1919",
    fg="white"
)

label_autor.pack()

entrada_autor = tk.Entry(frame_cadastro)
entrada_autor.pack()

def adicionar_livro():
    nome_livro = entrada_titulo.get()
    autor = entrada_autor.get()

    livro = f"{nome_livro} - {autor}"

    lista_livros.insert(tk.END, livro)

def ver_lista():
    frame_cadastro.pack_forget()
    frame_lista.pack()

def voltar():
    frame_lista.pack_forget()
    frame_cadastro.pack()

botao_adicionar = tk.Button(
    frame_cadastro,
    text="Adicionar livro",
    command=adicionar_livro
)

botao_ver_lista = tk.Button(
    frame_cadastro,
    text="Ver lista",
    command=ver_lista
)

botao_voltar = tk.Button(
    frame_lista,
    text="Voltar",
    command=voltar
)

botao_voltar.pack()
botao_ver_lista.pack()
botao_adicionar.pack(pady=10)

lista_livros = tk.Listbox(
    frame_lista,
    width=50,
    height=10
)

lista_livros.pack()

janela.mainloop()