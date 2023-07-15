from pydantic_settings import BaseSettings


class ChangeMachineSettings(BaseSettings):
    algorithm: str = "greedy"
    return_coins_only: bool = True

    class Config:
        env_prefix = "CHG__"
