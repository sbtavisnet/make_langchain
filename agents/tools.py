from langchain.agents import Tool
from services.rastreamento import rastrear_pedido
from services.faturas import buscar_ultima_fatura
from services.debitos import listar_debitos

rastreamento_tool = Tool(
    name="RastreioPedido",
    func=rastrear_pedido,
    description="Use para rastrear um pedido com base no ID fornecido.",
)

fatura_tool = Tool(
    name="UltimaFatura",
    func=buscar_ultima_fatura,
    description="Use para buscar a última fatura do cliente com base no ID.",
)

debitos_tool = Tool(
    name="ListarDebitos",
    func=listar_debitos,
    description="Use para listar os débitos pendentes de um cliente com base no ID.",
)
