import os
from dotenv import load_dotenv

load_dotenv()


class Settings:

    DATABASE_URL: str = os.getenv("DATABASE_URL")
    RABBITMQ_URL: str = os.getenv("RABBITMQ_URL")

    PROJECT_NAME: str = "Document Processing API"
    VERSION: str = "1.0.0"


settings = Settings()

