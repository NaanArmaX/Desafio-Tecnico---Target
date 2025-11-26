import uuid

def movimentar_estoque(item,quantidade,tipo):
    if tipo == "Entrada":
        item["estoque"] += quantidade
    else:
        if item["estoque"] < quantidade:
            return None, "Estoque Insuficiente"
        item["estoque"] -= quantidade

    id_mov = uuid.uuid4()

    return id_mov, None