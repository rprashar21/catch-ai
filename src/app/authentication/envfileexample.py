from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    api_key: str
    user_name: str
    db_password: str

    class Config:
        env_file = '.env'


settings = Settings()

print("api key is ---")
print(settings.api_key + " " + settings.user_name + " " + settings.db_password)
