from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    pg_dsn: PostgresDsn = 'postgres://postgres:postgres@localhost:5432/postgres'


settings = Settings()
