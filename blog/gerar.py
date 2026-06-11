import os
from tkinter import Tk, filedialog, messagebox

# Oculta a janela principal do Tkinter

Tk().withdraw()

# Selecionar arquivo TXT

arquivo_txt = filedialog.askopenfilename(
title="Selecione o arquivo TXT",
filetypes=[("Arquivos TXT", "*.txt")]
)

if not arquivo_txt:
    print("Nenhum arquivo selecionado.")
    exit()

# Ler arquivo

with open(arquivo_txt, "r", encoding="utf-8") as f:
    linhas = [linha.strip() for linha in f if linha.strip()]

videos = []

for i in range(0, len(linhas), 2):
    if i + 1 < len(linhas):
        videos.append((linhas[i], linhas[i + 1]))

nome_html = os.path.splitext(os.path.basename(arquivo_txt))[0] + ".html"
PASTA_DESTINO = r"D:\GitHub\J-S-YT\link\blog"

caminho_html = os.path.join(
    PASTA_DESTINO,
    nome_html
)

html = f"""<!DOCTYPE html>

<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{os.path.splitext(os.path.basename(arquivo_txt))[0]}</title>

<style>
body {{
    background: #111;
    color: white;
    font-family: Arial, sans-serif;
    text-align: center;
    margin: 0;
    padding: 20px;
}}

h1 {{
    margin-bottom: 20px;
}}

.botao {{
    display: block;
    width: 320px;
    margin: 10px auto;
    padding: 15px;
    background: #ff6600;
    color: white;
    text-decoration: none;
    border-radius: 10px;
    font-size: 18px;
    transition: 0.2s;
}}

.botao:hover {{
    transform: scale(1.03);
}}
</style>

</head>
<body>

<h1>{os.path.splitext(os.path.basename(arquivo_txt))[0]}</h1>
"""

for nome, link in videos:
    html += f'<a class="botao" href="{link}" target="_blank">{nome}</a>\n'

html += """

</body>
</html>
"""

with open(caminho_html, "w", encoding="utf-8") as f:
    f.write(html)

messagebox.showinfo(
"Concluído",
f"Página criada com sucesso!\n\n{caminho_html}"
)

print("HTML criado:", caminho_html)
