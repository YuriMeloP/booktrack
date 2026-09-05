import tkinter as tk

janela = tk.Tk()
janela.title("BookTrack")
janela.geometry("700x500")
janela.configure(bg="#1a1919")

janela.columnconfigure(0, weight=1)

titulo_app = tk.Label(
    janela,
    text="BookTrack",
    font=("Arial", 24, "bold"),
    bg="#1a1919",
    fg="white"
)

titulo_app.grid(row=0, column=0, pady=15)


frame_cadastro = tk.Frame(
    janela,
    bg="#1a1919"
)

frame_cadastro.grid(row=1, column=0)


label_titulo = tk.Label(
    frame_cadastro,
    text="Livro:",
    bg="#1a1919",
    fg="white"
)

label_titulo.grid(row=0, column=0, padx=5, pady=5)

entrada_titulo = tk.Entry(frame_cadastro)
entrada_titulo.grid(row=0, column=1, padx=5, pady=5)


label_autor = tk.Label(
    frame_cadastro,
    text="Autor:",
    bg="#1a1919",
    fg="white"
)

label_autor.grid(row=1, column=0, padx=5, pady=5)

entrada_autor = tk.Entry(frame_cadastro)
entrada_autor.grid(row=1, column=1, padx=5, pady=5)


frame_lista = tk.Frame(
    janela,
    bg="#1a1919"
)

frame_lista.grid(row=1, column=0)
frame_lista.grid_remove()


def adicionar_livro():
    nome_livro = entrada_titulo.get()
    autor = entrada_autor.get()

    livro = f"{nome_livro} - {autor}"

    lista_livros.insert(tk.END, livro)


def ver_lista():
    frame_cadastro.grid_remove()
    frame_lista.grid()


def voltar():
    frame_lista.grid_remove()
    frame_cadastro.grid()


botao_adicionar = tk.Button(
    frame_cadastro,
    text="Adicionar livro",
    command=adicionar_livro
)

botao_adicionar.grid(
    row=2,
    column=0,
    columnspan=2,
    pady=(10, 5)
)


botao_ver_lista = tk.Button(
    frame_cadastro,
    text="Ver lista",
    command=ver_lista
)

botao_ver_lista.grid(
    row=3,
    column=0,
    columnspan=2,
    pady=5
)


botao_voltar = tk.Button(
    frame_lista,
    text="Voltar",
    command=voltar
)

botao_voltar.grid(row=0, column=0, pady=5)


lista_livros = tk.Listbox(
    frame_lista,
    width=50,
    height=10
)

lista_livros.grid(row=1, column=0, pady=5)


janela.mainloop()