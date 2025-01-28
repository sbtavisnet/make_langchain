from agents.gestor import executar_agente


def test_rastrear_pedido(capfd):
    resultado = executar_agente("Rastrear pedido 123")
    assert "Em trânsito" in resultado
    print("Pedido:", resultado)
    captured = capfd.readouterr()
    assert "Pedido:" in captured.out


def test_ultima_fatura():
    resultado = executar_agente("Minha última fatura")
    assert "R$ 150,00" in resultado


def test_listar_debitos():
    resultado = executar_agente("Quais são meus débitos?")
    assert "R$ 50,00" in resultado
