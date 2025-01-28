# uvicorn app:app --reload --port 8080
# uvicorn main:app --reload
import os
from dotenv import load_dotenv


class Settings:
    load_dotenv()
    # GROQ_API_KEY = os.getenv("GROQ_API_KEY", "your_groq_api_key_here")
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    GROQ_MODEL = os.getenv("GROQ_MODEL")
    GROQ_URL = os.getenv("GROQ_URL")

    # Configuração de execução do Uvicorn
    APP_HOST = os.getenv("APP_HOST", "0.0.0.0")
    APP_PORT = int(os.getenv("APP_PORT", 8000))


settings = Settings()

# ------------------------------ #

# # Configurações de API
# GROQ_API_KEY = "sua-chave-de-api-groq"
# GROQ_API_URL = "https://api.groq.com/v1/generate"

# # Configurações gerais
# LOG_LEVEL = "INFO"

# # Banco de dados simulado de usuários e tokens
# USUARIOS = {
#     "token123": {"id": "1", "nome": "João Silva", "email": "joao@email.com"},
#     "token456": {"id": "2", "nome": "Maria Oliveira", "email": "maria@email.com"},
# }


## uvicorn app.main:app --port 8080
## uvicorn app.main:app --reload

# import os
# from dotenv import load_dotenv


# class Settings:
#     # Configuração da API Groq

#     load_dotenv()
#     # GROQ_API_KEY = os.getenv("GROQ_API_KEY", "your_groq_api_key_here")
#     GROQ_API_KEY = os.getenv("GROQ_API_KEY")
#     GROQ_MODEL = os.getenv("GROQ_MODEL")

#     # Configuração de execução do Uvicorn
#     APP_HOST = os.getenv("APP_HOST", "0.0.0.0")
#     APP_PORT = int(os.getenv("APP_PORT", 8000))


# settings = Settings()
