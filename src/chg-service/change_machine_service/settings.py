from typing import Any

from pydantic_settings import BaseSettings


class ChangeMachineSettings(BaseSettings):
    algorithm: str = "greedy"
    return_coins_only: bool = True

    class Config:
        env_prefix = "CHG_"


class ServerSettings(BaseSettings):
    prefix: str = "/api/v1"
    host: str = "0.0.0.0"
    port: int = 8080
    log_file: str | None = None

    class Config:
        env_prefix = "SRV_"


def get_settings() -> dict[str, Any]:
    return {
        "server": ServerSettings(),
        "change_machine": ChangeMachineSettings(),
    }


SETTINGS = get_settings()
