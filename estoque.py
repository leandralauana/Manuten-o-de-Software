estoque = {
    "produto_1": 10,
    "produto_2": 0,   # Sem estoque
}

def verificar_estoque(produto_id, quantidade):
    return estoque.get(produto_id, 0) >= quantidade

def adicionar_produto(produto_id, quantidade):
    if quantidade < 0:
        raise ValueError("Quantidade deve ser positiva.")
    estoque[produto_id] = estoque.get(produto_id, 0) + quantidade

def reduzir_estoque(produto_id, quantidade):
    if not verificar_estoque(produto_id, quantidade):
        raise RuntimeError("Estoque insuficiente para reduzir.")
    estoque[produto_id] -= quantidade