from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
import re
import logging
from typing import Dict, Any
from agents.gestor import executar_agente

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

router = APIRouter()


class InputData(BaseModel):
    context: str = Field(..., description="O contexto da solicitação do usuário")
    client_id: int | None = Field(
        None, description="ID do cliente extraído do contexto"
    )
    order_number: str | None = Field(
        None, description="Número do pedido extraído do contexto"
    )
    original_query: str | None = Field(
        None, description="Consulta original sem o ID do cliente ou número do pedido"
    )

    @classmethod
    def process_context(cls, context: str) -> Dict[str, Any]:
        client_match = re.search(r"\b(?:cliente|id)\s*(\d+)\b", context, re.IGNORECASE)
        order_match = re.search(
            r"\b(?:pedido|rastreamento)\s*(?:do\s+pedido)?\s*(\w+)\b",
            context,
            re.IGNORECASE,
        )

        client_id = int(client_match.group(1)) if client_match else None
        order_number = order_match.group(1) if order_match else None

        original_query = context
        if client_id:
            original_query = re.sub(
                r"\b(?:cliente|id)\s*\d+\b", "", original_query, flags=re.IGNORECASE
            )
        if order_number:
            original_query = re.sub(
                r"\b(?:pedido|rastreamento)\s*(?:do\s+pedido)?\s*\w+\b",
                "",
                original_query,
                flags=re.IGNORECASE,
            )

        original_query = original_query.strip()

        logger.debug(
            f"Extracted client_id={client_id}, order_number={order_number}, original_query={original_query}"
        )

        return {
            "context": context,
            "client_id": client_id,
            "order_number": order_number,
            "original_query": original_query,
        }

    @classmethod
    def model_validate(cls, obj: Any) -> "InputData":
        if isinstance(obj, dict) and "context" in obj:
            processed_data = cls.process_context(obj["context"])
            obj.update(processed_data)
        return super().model_validate(obj)


@router.post("/processar")
async def processar_solicitacao(input_data: Dict[str, Any]):
    try:
        processed_input = InputData.model_validate(input_data)

        logger.info(f"Received request: context={processed_input.context}")
        logger.info(
            f"Processed request: client_id={processed_input.client_id}, "
            f"order_number={processed_input.order_number}, "
            f"original_query={processed_input.original_query}"
        )

        if processed_input.order_number:
            contexto_usuario = f"Rastreamento do pedido {processed_input.order_number}: {processed_input.context}"
        elif processed_input.client_id is not None:
            contexto_usuario = f"Consulta para o cliente {processed_input.client_id}: {processed_input.context}"
        else:
            raise HTTPException(
                status_code=400,
                detail="Tipo de solicitação não reconhecido ou informações insuficientes",
            )

        logger.info(f"Contexto processado: {contexto_usuario}")

        resultado = executar_agente(contexto_usuario)
        return {"result": resultado}
    except HTTPException as he:
        logger.error(f"Erro de validação: {str(he)}")
        raise he
    except Exception as e:
        logger.error(f"Erro ao processar solicitação: {str(e)}")
        raise HTTPException(
            status_code=500, detail=f"Erro ao processar solicitação: {str(e)}"
        )
