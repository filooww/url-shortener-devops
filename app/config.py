from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: str = "sqlite:///./urls.db"
    base_url: str = "http://localhost:8000"
    # если не задан — кэш просто отключён (приложение работает без Redis)
    redis_url: str | None = None

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
