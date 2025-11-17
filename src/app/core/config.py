import os
from dotenv import load_dotenv

load_dotenv()  # this will locate for the file .env

print(os.getenv("API_KEY"))


class Settings:
    API_KEY = os.getenv("API_KEY")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")
    REDIS_URL = os.getenv("REDIS_URL")
    MODEL_PATH = ''


settings = Settings()  # we can access all these setting using config
