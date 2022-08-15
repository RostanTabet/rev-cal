from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    pg_dsn: PostgresDsn = 'postgresql://postgres:postgres@db:5432/postgres'


settings = Settings()
