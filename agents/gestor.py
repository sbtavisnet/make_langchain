# agents/gestor.py
import re
import logging

logger = logging.getLogger(__name__)


def executar_agente(contexto_usuario: str) -> dict:
    try:
        # Extrair o tipo de consulta, ID do cliente ou número do pedido, e a query
        match = re.match(
            r"(Rastreamento do pedido|Consulta para o cliente) (\w+): (.+)",
            contexto_usuario,
        )
        if not match:
            raise ValueError("Formato de contexto inválido")

        tipo_consulta = match.group(1)
        id_ou_numero = match.group(2)
        query = match.group(3)

        # Lógica do agente (simulada aqui)
        if tipo_consulta == "Rastreamento do pedido":
            thought = f"Quero obter informações sobre o rastreamento do pedido {id_ou_numero}."
            action = "RastrearPedido"
            action_input = id_ou_numero
            # Simular uma resposta (você substituiria isso pela lógica real)
            observation = {
                "status": "Em trânsito",
                "localização": "Centro de distribuição",
            }
        else:  # Consulta para o cliente
            thought = (
                f"Quero obter informações para o cliente {id_ou_numero} sobre: {query}"
            )
            action = "ConsultarCliente"
            action_input = {"client_id": id_ou_numero, "query": query}
            # Simular uma resposta (você substituiria isso pela lógica real)
            if "fatura" in query.lower():
                observation = {
                    "status": "Fatura disponível",
                    "valor": "R$ 150,00",
                    "vencimento": "2023-06-15",
                }
            elif "débito" in query.lower():
                observation = {"status": "Sem débitos pendentes"}
            else:
                observation = {"status": "Cliente ativo", "última_compra": "2023-05-15"}

        result = {
            "Question": contexto_usuario,
            "Thought": thought,
            "Action": action,
            "Action Input": action_input,
            "Observation": observation,
        }

        logger.info(f"Resultado gerado pelo agente: {result}")
        return result
    except Exception as e:
        logger.error(f"Erro na execução do agente: {str(e)}")
        return {
            "error": f"Erro na execução do agente: {str(e)}",
            "Question": contexto_usuario,
            "Thought": "Ocorreu um erro ao processar a solicitação.",
            "Action": "ReportError",
            "Action Input": str(e),
            "Observation": {"error": str(e)},
        }
