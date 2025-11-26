def calc_comi(vendas):
    comissoes = {}

    for i in vendas:
        vendedor = i["vendedor"]
        valor = i["valor"]

        if valor < 100:
            comissao = 0 
        elif valor < 500:
            comissao = valor * 0.01
        else:
            comissao = valor * 0.05
        
        comissoes[vendedor] = comissoes.get(vendedor, 0) + comissao

    return comissoes