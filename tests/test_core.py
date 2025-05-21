import pytest
from pedidos.core import calcular_total, processar_pedido, cadastrar_produto, finalizar_pedido

def test_calcular_total_sem_desconto():
    assert calcular_total(10, 2) == 20

def test_calcular_total_com_desconto():
    assert calcular_total(10, 2, desconto=0.1) == 18

def test_calcular_total_parametros_invalidos():
    with pytest.raises(ValueError):
        calcular_total(-5, 2)

def test_processar_pedido_sucesso():
    cadastrar_produto("produto_teste", 5)
    total = processar_pedido("produto_teste", 2, 15)
    assert total == 30

def test_processar_pedido_estoque_insuficiente():
    with pytest.raises(RuntimeError):
        processar_pedido("produto_2", 1, 10)

def test_cadastrar_produto():
    cadastrar_produto("produto_novo", 3)
    assert processar_pedido("produto_novo", 1, 10) == 10

def test_finalizar_pedido():
    assert finalizar_pedido() is True
