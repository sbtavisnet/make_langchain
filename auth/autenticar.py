# auth/autenticar.py

from fastapi import HTTPException, Header
from settings import USUARIOS


def autenticar_token(authorization: str = Header(None)):
    """
    Serviço que autentica o usuário com base no token enviado no cabeçalho Authorization.
    """
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=401, detail="Cabeçalho Authorization inválido ou ausente."
        )

    # Extrair o token do cabeçalho
    token = authorization.split(" ")[1]
    usuario = USUARIOS.get(token)

    if not usuario:
        raise HTTPException(
            status_code=401, detail="Token inválido ou usuário não encontrado."
        )

    return usuario
