from fastapi import APIRouter

router = APIRouter()


@router.get("/status")
async def verificar_status():
    return {"status": "processando"}
