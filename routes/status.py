from fastapi import APIRouter
from datetime import datetime


router = APIRouter()


@router.get("/status")
async def verificar_status():
    now = datetime.now()
    dia = now.day
    mes = now.month
    ano = now.year
    hours = now.hour
    minutes = now.minute
    seconds = now.second

    data = {
        "servico": "Api da plataforma MakeSales",
        "versao": "5.1.22",
        "razao": "Avisnet System Informatica Ltda",
        "endereco": "Rua Cisne, 60",
        "bairro": "Lagoa Santa",
        "cidade": "Governador Valadares - MG",
        "cnpj": "86.534.401.0001-47",
        "page": "www.avisnet.com.br",
        "email": "avisnet@avisnet.com.br",
        "data": f"{dia}/{mes}/{ano}",
        "hora": f"{hours}:{minutes}:{seconds}",
        "autor": "SBT",
    }
    result = {"result": data}

    return result
