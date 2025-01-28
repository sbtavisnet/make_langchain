from fastapi import FastAPI
import logging
import uvicorn

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


@app.get("/")
async def root():
    print("Root route accessed")
    return {"message": "Hello World"}


@app.get("/status")
async def status():
    print("Status route accessed")
    return {"status": "OK"}


if __name__ == "__main__":
    logger.info("Starting FastAPI application")
    uvicorn.run(app, host="127.0.0.1", port=8080, log_level="info")
