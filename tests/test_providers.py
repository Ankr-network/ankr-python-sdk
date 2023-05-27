from __future__ import annotations

from ankr.providers import (
    ArbitrumHTTPProvider,
    AvalancheHTTPProvider,
    BscHTTPProvider,
    CeloHTTPProvider,
    EthHTTPProvider,
    FantomHTTPProvider,
    GnosisHTTPProvider,
    HarmonyHTTPProvider,
    IotexHTTPProvider,
    MoonbeamHTTPProvider,
    MultichainHTTPProvider,
    NearHTTPProvider,
    NervosHTTPProvider,
    OptimismHTTPProvider,
    PolygonHTTPProvider,
    SolanaHTTPProvider,
    SyscoinHTTPProvider,
)


def test_provider_api_key() -> None:
    assert (
        MultichainHTTPProvider("my-test-api-key").endpoint_uri
        == "https://rpc.ankr.com/multichain/my-test-api-key"
    )


def test_chain_providers() -> None:
    assert ArbitrumHTTPProvider().endpoint_uri == "https://rpc.ankr.com/arbitrum/"
    assert AvalancheHTTPProvider().endpoint_uri == "https://rpc.ankr.com/avalanche/"
    assert BscHTTPProvider().endpoint_uri == "https://rpc.ankr.com/bsc/"
    assert CeloHTTPProvider().endpoint_uri == "https://rpc.ankr.com/celo/"
    assert EthHTTPProvider().endpoint_uri == "https://rpc.ankr.com/eth/"
    assert FantomHTTPProvider().endpoint_uri == "https://rpc.ankr.com/fantom/"
    assert GnosisHTTPProvider().endpoint_uri == "https://rpc.ankr.com/gnosis/"
    assert HarmonyHTTPProvider().endpoint_uri == "https://rpc.ankr.com/harmony/"
    assert IotexHTTPProvider().endpoint_uri == "https://rpc.ankr.com/iotex/"
    assert MoonbeamHTTPProvider().endpoint_uri == "https://rpc.ankr.com/moonbeam/"
    assert NearHTTPProvider().endpoint_uri == "https://rpc.ankr.com/near/"
    assert NervosHTTPProvider().endpoint_uri == "https://rpc.ankr.com/nervos/"
    assert OptimismHTTPProvider().endpoint_uri == "https://rpc.ankr.com/optimism/"
    assert PolygonHTTPProvider().endpoint_uri == "https://rpc.ankr.com/polygon/"
    assert SolanaHTTPProvider().endpoint_uri == "https://rpc.ankr.com/solana/"
    assert SyscoinHTTPProvider().endpoint_uri == "https://rpc.ankr.com/syscoin/"

    assert (
        ArbitrumHTTPProvider(api_key="123").endpoint_uri
        == "https://rpc.ankr.com/arbitrum/123"
    )
