# services/debitos.py


def listar_debitos(cliente_id):
    """
    Serviço para listar débitos pendentes de um cliente. Simula uma API financeira.
    """
    debitos = {
        "1": {"debitos": ["R$ 50,00 (vencida)", "R$ 100,00 (em aberto)"]},
        "2": {"debitos": ["R$ 300,00 (em aberto)"]},
    }
    return debitos.get(cliente_id, {"error": "Cliente sem débitos pendentes."})
