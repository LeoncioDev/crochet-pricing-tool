# calculos.py

def calcular_preco(horas, valor_hora, peso_rolo, valor_rolo, linha_usada, margem, papel, brinde, tag, cartoes):
    custo_mao_obra = horas * valor_hora
    custo_linha = (linha_usada / peso_rolo) * valor_rolo
    custo_extra = papel + brinde + tag + cartoes
    custo_total = custo_mao_obra + custo_linha + custo_extra
    preco_final = custo_total * (1 + margem / 100)

    return {
        "custo_mao_obra": custo_mao_obra,
        "custo_linha": custo_linha,
        "custo_extra": custo_extra,
        "custo_total": custo_total,
        "preco_final": preco_final
    }
