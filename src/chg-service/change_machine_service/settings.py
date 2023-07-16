from typing import Any

from pydantic_settings import BaseSettings


class ChangeMachineSettings(BaseSettings):
    algorithm: str = "greedy"
    return_coins_only: bool = True

    class Config:
        env_prefix = "CHG__"


class ServerSettings(BaseSettings):
    prefix: str = "/api/v1"
    host: str = "0.0.0.0"
    port: int = 8080

    class Config:
        env_prefix = "SRV__"


def get_settings() -> dict[str, Any]:
    return {
        "server": ServerSettings(),
        "change_machine": ChangeMachineSettings(),
    }
