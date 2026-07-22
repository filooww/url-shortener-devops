from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # SQLite по умолчанию (локальная разработка), в проде переопределим через env
    database_url: str = "sqlite:///./urls.db"
    base_url: str = "http://localhost:8000"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
