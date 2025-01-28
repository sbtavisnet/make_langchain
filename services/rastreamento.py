def rastrear_pedido(pedido_id):
    pedidos = {
        "123": {"status": "Em trânsito", "previsao_entrega": "2 dias"},
        "456": {"status": "Entregue", "data_entrega": "25/01/2025"},
        "789": {"status": "Aguardando retirada no depósito"},
    }
    return pedidos.get(pedido_id, {"error": "Pedido não encontrado."})
