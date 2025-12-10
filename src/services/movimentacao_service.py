import uuid
from src.database.estoque_repository import get_produto, att_produtos
from src.database.movimentacao_repository import reg_mov


def movimentar_estoque(id_produto, quantidade, tipo):
    produto = get_produto(id_produto)

    if produto is None:
        return None, "Produto Não Encontrado"

    estoque_atual = produto["quantidade"]

    if tipo == "Entrada":
        novo_estoque = estoque_atual + quantidade

    elif tipo == "Saida":
        if estoque_atual < quantidade:
            return None, "Estoque Insuficiente"
        novo_estoque = estoque_atual - quantidade

    else:
        return None, "Tipo inválido"

    att_produtos(id_produto, produto["nome"], novo_estoque, produto["preco"])

    id_mov = str(uuid.uuid4())
    reg_mov(id_mov, id_produto, tipo, quantidade)

    return id_mov, None
