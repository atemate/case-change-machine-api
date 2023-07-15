import pytest
from change_machine_service.api import app, get_chg_settings
from change_machine_service.settings import ChangeMachineSettings
from fastapi.testclient import TestClient


def get_chg_settings_override():
    return ChangeMachineSettings(
        algorithm="greedy",
        return_coins_only=True,
    )


@pytest.fixture
def client():
    app.dependency_overrides[get_chg_settings] = get_chg_settings_override
    with TestClient(app) as client:
        yield client
