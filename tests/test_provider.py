from __future__ import annotations

from ankr import AnkrAdvancedAPI, types


def test_provider_api_key():
    advanced_api = AnkrAdvancedAPI()
    assert advanced_api.provider.endpoint_uri == "https://rpc.ankr.com/multichain/"

    advanced_api = AnkrAdvancedAPI("my-test-api-key")
    assert (
        advanced_api.provider.endpoint_uri
        == "https://rpc.ankr.com/multichain/my-test-api-key"
    )


def test_get_logs():
    advanced_api = AnkrAdvancedAPI()
    logs = list(
        advanced_api.get_logs(
            blockchain=types.BlockchainName.ETH,
            from_block="0xdaf6b1",
            to_block=14350010,
            address=["0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"],
            topics=[
                [],
                ["0x000000000000000000000000def1c0ded9bec7f1a1670819833240f027b25eff"],
            ],
            decode_logs=True,
        )
    )

    assert len(logs) == 18
    assert logs[0].address == "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"
    assert logs[0].event.name == "Deposit"


def test_get_blocks():
    advanced_api = AnkrAdvancedAPI()
    blocks = advanced_api.get_blocks(
        blockchain=types.BlockchainName.ETH,
        from_block=14500001,
        to_block=14500001,
        desc_order=True,
        include_logs=True,
        include_txs=True,
        decode_logs=True,
    )

    assert len(blocks) == 1
    assert blocks[0].transactions
    assert len(blocks[0].transactions) == 99
    assert len(blocks[0].transactions[6].logs) == 1


def test_get_nfts():
    advanced_api = AnkrAdvancedAPI()
    nfts = list(
        advanced_api.get_nfts(
            blockchain=types.BlockchainName.ETH,
            wallet_address="0x0E11A192d574b342C51be9e306694C41547185DD",
            filter=[
                {"0x700b4b9f39bb1faf5d0d16a20488f2733550bff4": []},
                {"0xd8682bfa6918b0174f287b888e765b9a1b4dc9c3": ["8937"]},
            ],
        )
    )

    assert len(nfts) > 0
    assert nfts[0].blockchain == types.BlockchainName.ETH
    assert len(nfts[0].traits) > 0
