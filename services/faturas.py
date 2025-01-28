def buscar_ultima_fatura(cliente_id):
    faturas = {
        "1": {"fatura": "R$ 150,00", "vencimento": "10/01/2025", "status": "Paga"},
        "2": {"fatura": "R$ 200,00", "vencimento": "15/01/2025", "status": "Em aberto"},
    }
    return faturas.get(cliente_id, {"error": "Cliente não encontrado."})
