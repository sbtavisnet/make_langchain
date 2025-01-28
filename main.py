from fastapi import FastAPI

from routes.status import router as status_router
from routes.webhook import router as webhook_router

app = FastAPI()

# Incluindo as rotas
app.include_router(status_router, prefix="/api")
app.include_router(webhook_router, prefix="/api")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
