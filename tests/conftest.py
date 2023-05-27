import os

import pytest

from ankr import AnkrAdvancedAPI


@pytest.fixture
def api_key() -> str:
    key = os.environ.get("ANKR_API_KEY")
    assert key
    return key


@pytest.fixture
def client(api_key: str) -> AnkrAdvancedAPI:
    return AnkrAdvancedAPI(api_key)
