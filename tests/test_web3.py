from __future__ import annotations

import pytest

from ankr.web3 import AnkrWeb3


@pytest.mark.webtest
@pytest.mark.parametrize(
    "blockchain",
    [
        "eth",
        "arbitrum",
        "avalanche",
        "bsc",
        "celo",
        "fantom",
        "gnosis",
        "harmony",
        "iotex",
        "moonbeam",
        "nervos",
        "optimism",
        "polygon",
        "syscoin",
    ],
)
def test_ankr_web3(blockchain: str, api_key: str) -> None:
    w3 = AnkrWeb3(api_key)

    block = getattr(w3, blockchain).get_block("latest")

    assert block
    assert block.get("number")
