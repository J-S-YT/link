import os
import tkinter as tk
from tkinter import filedialog, messagebox


# -----------------------------
# Selecionar arquivos
# -----------------------------

def selecionar_txt():
    arquivo = filedialog.askopenfilename(
        title="Selecionar TXT",
        filetypes=[("Arquivo TXT", "*.txt")]
    )
    txt_var.set(arquivo)


def selecionar_pasta():
    pasta = filedialog.askdirectory(
        title="Selecionar pasta de destino"
    )
    pasta_var.set(pasta)


# -----------------------------
# Gerar episódios
# -----------------------------

def gerar():

    nome_anime = anime_var.get().strip()
    capa = capa_var.get().strip()
    arquivo_txt = txt_var.get()
    pasta_destino = pasta_var.get()

    if not nome_anime or not capa or not arquivo_txt or not pasta_destino:
        messagebox.showerror(
            "Erro",
            "Preencha todos os campos!"
        )
        return


        # Ler template

    try:
        pasta_programa = os.path.dirname(
            os.path.abspath(__file__)
        )

        arquivo_template = os.path.join(
            pasta_programa,
            "template.html"
        )

        with open(
            arquivo_template,
            "r",
            encoding="utf-8"
        ) as f:
            template = f.read()

    except Exception as erro:
        messagebox.showerror(
            "Erro",
            f"Não encontrei o arquivo template.html\n\n{erro}"
        )
        return


    # Ler TXT

    with open(arquivo_txt, "r", encoding="utf-8") as f:
        linhas = [
            linha.strip()
            for linha in f
            if linha.strip()
        ]


    videos = []

    for i in range(0, len(linhas), 2):

        if i + 1 < len(linhas):

            nome = linhas[i]
            link = linhas[i + 1]

            videos.append(link)


    total = len(videos)


    # Criar arquivos

    for numero, link in enumerate(videos, start=1):

        html = template


        anterior = (
            f"episodio-{numero-1}.html"
            if numero > 1
            else "#"
        )


        proximo = (
            f"episodio-{numero+1}.html"
            if numero < total
            else "#EM-BREVE"
        )


        html = html.replace(
            "{{NOME_ANIME}}",
            nome_anime
        )

        html = html.replace(
            "{{CAPA_ANIME}}",
            capa
        )

        html = html.replace(
            "{{EPISODIO}}",
            str(numero)
        )

        html = html.replace(
            "{{BLOGGER}}",
            link
        )

        html = html.replace(
            "{{ANTERIOR}}",
            anterior
        )

        html = html.replace(
            "{{PROXIMO}}",
            proximo
        )


        nome_arquivo = (
            f"episodio-{numero}.html"
        )


        caminho = os.path.join(
            pasta_destino,
            nome_arquivo
        )


        with open(
            caminho,
            "w",
            encoding="utf-8"
        ) as f:
            f.write(html)



    messagebox.showinfo(
        "Concluído",
        f"{total} episódios criados!"
    )



# -----------------------------
# Interface
# -----------------------------

janela = tk.Tk()

janela.title(
    "Gerador de Episódios JSY ANIME"
)

janela.geometry(
    "500x350"
)


anime_var = tk.StringVar()
capa_var = tk.StringVar()
txt_var = tk.StringVar()
pasta_var = tk.StringVar()


tk.Label(
    janela,
    text="Nome do Anime"
).pack()

tk.Entry(
    janela,
    textvariable=anime_var,
    width=60
).pack()



tk.Label(
    janela,
    text="Link da Capa"
).pack()

tk.Entry(
    janela,
    textvariable=capa_var,
    width=60
).pack()



tk.Label(
    janela,
    text="Arquivo TXT"
).pack()

tk.Entry(
    janela,
    textvariable=txt_var,
    width=45
).pack()

tk.Button(
    janela,
    text="Selecionar TXT",
    command=selecionar_txt
).pack()



tk.Label(
    janela,
    text="Pasta destino"
).pack()

tk.Entry(
    janela,
    textvariable=pasta_var,
    width=45
).pack()

tk.Button(
    janela,
    text="Selecionar Pasta",
    command=selecionar_pasta
).pack()



tk.Button(
    janela,
    text="GERAR EPISÓDIOS",
    bg="orange",
    fg="white",
    font=("Arial",12),
    command=gerar
).pack(pady=20)



janela.mainloop()