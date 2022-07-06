from __future__ import annotations

import datetime

import pytest

from ankr.advanced_apis import AnkrAdvancedAPI
from ankr.types import Blockchain, NftContractType


def test_client_api_key() -> None:
    client = AnkrAdvancedAPI()
    client_with_key = AnkrAdvancedAPI("my-test-api-key")

    assert client.provider.endpoint_uri == "https://rpc.ankr.com/multichain/"
    assert (
        client_with_key.provider.endpoint_uri
        == "https://rpc.ankr.com/multichain/my-test-api-key"
    )


@pytest.mark.webtest
def test_get_logs() -> None:
    client = AnkrAdvancedAPI()
    logs = list(
        client.get_logs(
            blockchain=Blockchain.ETH,
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
    assert logs[0].event
    assert logs[0].event.name == "Deposit"


@pytest.mark.webtest
def test_get_blocks() -> None:
    client = AnkrAdvancedAPI()
    blocks = client.get_blocks(
        blockchain=Blockchain.ETH,
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


@pytest.mark.webtest
def test_get_nfts() -> None:
    client = AnkrAdvancedAPI()
    nfts = list(
        client.get_nfts(
            blockchain=Blockchain.ETH,
            wallet_address="0x0E11A192d574b342C51be9e306694C41547185DD",
            filter=[
                {"0x700b4b9f39bb1faf5d0d16a20488f2733550bff4": []},
                {"0xd8682bfa6918b0174f287b888e765b9a1b4dc9c3": ["8937"]},
            ],
        )
    )

    assert len(nfts) > 0
    assert nfts[0].blockchain == Blockchain.ETH
    assert nfts[0].traits
    assert len(nfts[0].traits) > 0


@pytest.mark.webtest
def test_get_nft_metadata() -> None:
    client = AnkrAdvancedAPI()
    reply = client.get_nft_metadata(
        blockchain="eth",
        contract_address="0x4100670ee2f8aef6c47a4ed13c7f246e621228ec",
        token_id="4",
    )

    assert reply.metadata
    assert reply.metadata.blockchain == "eth"
    assert reply.metadata.contract_type == NftContractType.ERC1155
    assert reply.attributes
    assert reply.attributes.name == "Overleveraged"


@pytest.mark.webtest
def test_get_transactions() -> None:
    client = AnkrAdvancedAPI()
    tx = client.get_transaction(
        transaction_hash="0x82c13aaac6f0b6471afb94a3a64ae89d45baa3608ad397621dbb0d847f51196f",
        include_logs=True,
        decode_logs=True,
        decode_tx_data=True,
    )

    assert tx
    assert (
        tx.transaction_hash
        == "0x82c13aaac6f0b6471afb94a3a64ae89d45baa3608ad397621dbb0d847f51196f"
    )
    assert tx.to_address == "0x98767abab06e45a181ab73ae4cd0fecd0fbd0cd0"
    assert tx.from_address == "0x64aa6f93e0e1f49ff4958990c40d4bf17dafc0eb"
    assert tx.logs
    assert tx.logs[0].event
    assert tx.logs[0].event.name == "Transfer"


@pytest.mark.webtest
def test_get_token_holders() -> None:
    client = AnkrAdvancedAPI()
    holders = list(
        client.get_token_holders(
            blockchain="bsc",
            contract_address="0xf307910A4c7bbc79691fD374889b36d8531B08e3",
            limit=10,
        )
    )

    assert len(holders) == 10
    assert holders[0].holder_address.startswith("0x")
    assert "." in holders[0].balance
    assert holders[0].balance_raw_integer.isnumeric()


@pytest.mark.webtest
def test_get_token_holders_count_history() -> None:
    client = AnkrAdvancedAPI()
    daily_holders_counts = list(
        client.get_token_holders_count_history(
            blockchain="bsc",
            contract_address="0xf307910A4c7bbc79691fD374889b36d8531B08e3",
            limit=10,
        )
    )

    assert len(daily_holders_counts) == 10
    assert daily_holders_counts[0].holder_count > 0
    datetime.datetime.strptime(
        daily_holders_counts[0].last_updated_at, "%Y-%m-%dT%H:%M:%SZ"
    )


@pytest.mark.webtest
def test_get_token_holders_count() -> None:
    client = AnkrAdvancedAPI()
    holders_count = client.get_token_holders_count(
        blockchain="bsc",
        contract_address="0xf307910A4c7bbc79691fD374889b36d8531B08e3",
    )

    assert holders_count
    assert holders_count.holder_count > 0
    datetime.datetime.strptime(holders_count.last_updated_at, "%Y-%m-%dT%H:%M:%SZ")


@pytest.mark.webtest
def test_get_account_balance() -> None:
    client = AnkrAdvancedAPI()
    assets = list(
        client.get_account_balance(
            wallet_address="0x77A859A53D4de24bBC0CC80dD93Fbe391Df45527",
            blockchain=["eth", "bsc"],
        )
    )

    assert assets
    assert len(assets) > 0
