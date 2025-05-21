from pedidos.estoque import verificar_estoque, adicionar_produto, reduzir_estoque
from pedidos.logger import logger


def calcular_total(preco_unitario, quantidade, desconto=0):
    if preco_unitario < 0 or quantidade <= 0:
        logger.error("Parâmetros inválidos para cálculo de total.")
        raise ValueError("Preço e quantidade devem ser positivos.")

    total_bruto = preco_unitario * quantidade
    total_final = total_bruto * (1 - desconto)

    logger.info(f"Total calculado: {total_final:.2f}")
    return total_final


def processar_pedido(produto_id, quantidade, preco_unitario, desconto=0):
    try:
        logger.info(f"Processando pedido de {quantidade} unidades de '{produto_id}'.")

        if not verificar_estoque(produto_id, quantidade):
            logger.warning(f"Estoque insuficiente para '{produto_id}'.")
            raise RuntimeError("Estoque insuficiente.")

        total = calcular_total(preco_unitario, quantidade, desconto)
        reduzir_estoque(produto_id, quantidade)

        logger.info(f"Pedido processado com sucesso. Total: R${total:.2f}")
        return total
    except Exception as e:
        logger.error(f"Erro ao processar pedido: {str(e)}")
        raise


def cadastrar_produto(produto_id, quantidade):
    try:
        adicionar_produto(produto_id, quantidade)
        logger.info(f"Produto '{produto_id}' cadastrado com {quantidade} unidades.")
    except Exception as e:
        logger.error(f"Erro ao cadastrar produto: {str(e)}")
        raise


def finalizar_pedido():
    try:
        logger.info("Pedido finalizado com sucesso.")
        return True
    except Exception as e:
        logger.error(f"Erro ao finalizar pedido: {str(e)}")
        raise