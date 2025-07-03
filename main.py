import tkinter as tk
from tkinter import messagebox
from calculos import calcular_preco
from atualizador import verificar_atualizacao  

janela_ajustada = False

def str_para_float(valor_str):
    try:
        valor_str = valor_str.strip()
        if not valor_str:
            return 0.0
        return float(valor_str.replace(',', '.'))
    except:
        raise ValueError

def executar_calculo():
    global janela_ajustada
    try:
        horas = str_para_float(entries["horas"].get())
        valor_hora = str_para_float(entries["valor_hora"].get())
        peso_rolo = str_para_float(entries["peso_rolo"].get())
        valor_rolo = str_para_float(entries["valor_rolo"].get())
        linha_usada = str_para_float(entries["linha_usada"].get())
        margem = str_para_float(entries["margem"].get())

        papel = str_para_float(entries["papel"].get())
        brinde = str_para_float(entries["brinde"].get())
        tag = str_para_float(entries["tag"].get())
        cartoes = str_para_float(entries["cartoes"].get())

        resultado_calc = calcular_preco(
            horas, valor_hora, peso_rolo, valor_rolo,
            linha_usada, margem, papel, brinde, tag, cartoes
        )

        texto = (
            f"🧶 Mão de obra: R$ {resultado_calc['custo_mao_obra']:.2f}\n"
            f"🧵 Linha: R$ {resultado_calc['custo_linha']:.2f}\n"
            f"🎀 Adicionais:\n"
            f"   Papel: R$ {papel:.2f}\n"
            f"   Brinde: R$ {brinde:.2f}\n"
            f"   Tag: R$ {tag:.2f}\n"
            f"   Cartões: R$ {cartoes:.2f}\n"
            f"📦 Total produção: R$ {resultado_calc['custo_total']:.2f}\n"
            f"💖 Preço final (com lucro): R$ {resultado_calc['preco_final']:.2f}"
        )
        resultado_label.config(text=texto)

        if not janela_ajustada:
            largura = janela.winfo_width()
            altura = janela.winfo_height()
            nova_altura = altura + 100
            janela.geometry(f"{largura}x{nova_altura}")
            janela.update()
            janela_ajustada = True

    except ValueError:
        messagebox.showerror("Erro", "Preencha todos os campos corretamente com números válidos!")

def checar_versao():
    info = verificar_atualizacao()
    messagebox.showinfo("Verificação de versão", info)

# Janela principal
janela = tk.Tk()
janela.title("💖 Calculadora da Lami 💖")
janela.configure(bg="#fff0f5")
janela.geometry("420x680")
janela.minsize(420, 680)

label_font = ("Segoe UI", 10)
entry_font = ("Segoe UI", 10)
header_font = ("Segoe UI", 16, "bold")

titulo = tk.Label(janela, text="Calculadora da Lami", font=header_font, bg="#fff0f5", fg="#d63384")
titulo.grid(row=0, column=0, columnspan=2, pady=(20,15))

entries = {}

campos = [
    ("Horas trabalhadas:", "horas"),
    ("Valor da hora (R$):", "valor_hora"),
    ("Peso do rolo (g):", "peso_rolo"),
    ("Valor do rolo (R$):", "valor_rolo"),
    ("Linha usada (g):", "linha_usada"),
    ("Margem de lucro (%):", "margem"),
]

for i, (texto, chave) in enumerate(campos, start=1):
    lbl = tk.Label(janela, text=texto, font=label_font, bg="#fff0f5", anchor='w')
    lbl.grid(row=i, column=0, sticky='w', padx=20, pady=5)
    ent = tk.Entry(janela, font=entry_font, width=25, bg="white", relief="groove", borderwidth=2)
    ent.grid(row=i, column=1, padx=20, pady=5)
    entries[chave] = ent

linha_inicio = len(campos) + 1
header_extras = tk.Label(janela, text="Custos extras (opcional)", font=("Segoe UI", 11, "italic"),
                         bg="#fff0f5", fg="#a83270")
header_extras.grid(row=linha_inicio, column=0, columnspan=2, pady=(15, 5))

extras = [
    ("Valor do papel (R$):", "papel"),
    ("Valor do brinde (R$):", "brinde"),
    ("Valor da tag (R$):", "tag"),
    ("Valor dos cartões (R$):", "cartoes"),
]

for i, (texto, chave) in enumerate(extras, start=linha_inicio+1):
    lbl = tk.Label(janela, text=texto, font=label_font, bg="#fff0f5", anchor='w')
    lbl.grid(row=i, column=0, sticky='w', padx=20, pady=3)
    ent = tk.Entry(janela, font=entry_font, width=25, bg="white", relief="groove", borderwidth=2)
    ent.grid(row=i, column=1, padx=20, pady=3)
    entries[chave] = ent

linha_botoes = len(campos) + len(extras) + 2

botao = tk.Button(
    janela, text="Calcular 💰", command=executar_calculo,
    bg="#d63384", fg="white", font=("Segoe UI", 12, "bold"), width=20
)
botao.grid(row=linha_botoes, column=0, columnspan=2, pady=10)

resultado_label = tk.Label(
    janela, text="", font=("Segoe UI", 11), bg="#f9e6f0", fg="#2d6a4f",
    justify="left", wraplength=370, relief="solid", bd=1, padx=10, pady=10
)
resultado_label.grid(row=linha_botoes + 1, column=0, columnspan=2, padx=20, pady=(0, 20), sticky="ew")

botao_versao = tk.Button(
    janela, text="Verificar versão 🔍", command=checar_versao,
    bg="#d63384", fg="white", font=("Segoe UI", 10, "bold"), width=20
)
botao_versao.grid(row=linha_botoes + 2, column=0, columnspan=2, pady=(0, 20))

janela.mainloop()
