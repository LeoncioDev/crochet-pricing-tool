import requests

VERSAO_URL = "https://raw.githubusercontent.com/LeoncioDev/crochet-pricing-tool/main/versao.txt"
LINK_RELEASE = "https://github.com/LeoncioDev/crochet-pricing-tool/releases"

def ler_versao_local():
    try:
        with open("versao.txt", "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        return "0.0.0"

def ler_versao_remota():
    try:
        resposta = requests.get(VERSAO_URL, timeout=5)
        if resposta.status_code == 200:
            return resposta.text.strip()
        else:
            return None
    except Exception as e:
        print(f"Erro ao acessar versão remota: {e}")
        return None

def comparar_versoes(local, remoto):
    return local != remoto

# 🔹 ESSA É A FUNÇÃO QUE VAMOS IMPORTAR NO main.py
def verificar_atualizacao():
    versao_local = ler_versao_local()
    versao_remota = ler_versao_remota()

    if not versao_remota:
        return f"⚠️ Não foi possível verificar atualizações.\nVersão local: {versao_local}"

    if comparar_versoes(versao_local, versao_remota):
        return (
            f"🚨 Nova versão disponível!\n"
            f"Versão local: {versao_local}\n"
            f"Versão no GitHub: {versao_remota}\n\n"
            f"🔗 Baixe aqui:\n{LINK_RELEASE}"
        )
    else:
        return f"✅ Você já está usando a versão mais recente ({versao_local})."

# Deixa o main para rodar via terminal se quiser testar
if __name__ == "__main__":
    print(verificar_atualizacao())
