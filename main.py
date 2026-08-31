import tkinter as tk

janela = tk.Tk()
janela.title("BookTrack")
janela.geometry("700x500")
janela.configure(bg="#1a1919")
titulo = tk.Label(
    janela,
    text="BookTrack",
    font=("Arial", 24, "bold"),
    bg="#1a1919",
    fg="white"
)
titulo.pack(pady=15)

label_titulo = tk.Label(
    janela,
    text="Livro:",
    bg="#1a1919",
    fg="white"
)
label_titulo.pack()

entrada_titulo = tk.Entry(janela)
entrada_titulo.pack()

label_autor = tk.Label(
    janela,
    text="Autor:",
    bg="#1a1919",
    fg="white"
)
label_autor.pack()

entrada_autor = tk.Entry(janela)
entrada_autor.pack()

def adicionar_livro():
    titulo = entrada_titulo.get()
    autor = entrada_autor.get()

    print(f"{titulo} - {autor}")

botao_adicionar = tk.Button(
    janela,
    text="Adicionar livro",
    command=adicionar_livro
)
botao_adicionar.pack(pady=10)

janela.mainloop()

