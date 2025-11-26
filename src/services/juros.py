from datetime import datetime


def calcular_juros(valor, data_venc):
    try:
        data = datetime.strptime(data_venc, "%d/%m/%Y")
    except:
        return None, None, "Data Invalida, Use dd/mm/aaaa"

    hoje = datetime.now()
    dias = (hoje - data).days

    if dias <= 0:
        juros = 0
    else:
        juros = valor * (0.025 * dias)

    total = valor + juros
    return dias, juros, total
