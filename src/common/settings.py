from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    openapi_url: str = "/openapi.json"
    api_v1_prefix: str = "/api/v1"
    project_name: str = "FastAPI Template"
    description: str = "This is the documentation of the FastAPI template project."
    logger_name: str = "server"
    db_dsn: str = ""
    db_host: str = ""


settings = Settings()
