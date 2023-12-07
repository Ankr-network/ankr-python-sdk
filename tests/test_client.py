from __future__ import annotations

import datetime

import pytest

from ankr.advanced_apis import AnkrAdvancedAPI
from ankr.types import *


def test_client_api_key() -> None:
    assert (
        AnkrAdvancedAPI("my-test-api-key").provider.endpoint_uri
        == "https://rpc.ankr.com/multichain/my-test-api-key"
    )


@pytest.mark.webtest
def test_get_logs(client: AnkrAdvancedAPI) -> None:
    logs = list(
        client.get_logs(
            request=GetLogsRequest(
                blockchain=Blockchain.Eth,
                fromBlock=14350001,
                toBlock=14350010,
                address=["0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"],
                topics=[
                    [],
                    [
                        "0x000000000000000000000000def1c0ded9bec7f1a1670819833240f027b25eff"
                    ],
                ],
                decodeLogs=True,
            )
        )
    )

    assert len(logs) == 18
    assert logs[0].address == "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"
    assert logs[0].event
    assert logs[0].event.name == "Transfer"


@pytest.mark.webtest
def test_get_blocks(client: AnkrAdvancedAPI) -> None:
    blocks = client.get_blocks(
        request=GetBlocksRequest(
            blockchain=Blockchain.Eth,
            fromBlock=14500001,
            toBlock=14500001,
            descOrder=True,
            includeLogs=True,
            includeTxs=True,
            decodeLogs=True,
        )
    )

    assert len(blocks) == 1
    assert blocks[0].transactions
    assert len(blocks[0].transactions) == 99
    assert blocks[0].transactions[6].logs
    assert len(blocks[0].transactions[6].logs) == 1


@pytest.mark.webtest
def test_get_nfts(client: AnkrAdvancedAPI) -> None:
    nfts = list(
        client.get_nfts(
            request=GetNFTsByOwnerRequest(
                blockchain=Blockchain.Eth,
                walletAddress="0x0E11A192d574b342C51be9e306694C41547185DD",
                filter=[
                    {"0x700b4b9f39bb1faf5d0d16a20488f2733550bff4": []},
                    {"0xd8682bfa6918b0174f287b888e765b9a1b4dc9c3": ["8937"]},
                ],
            ),
        )
    )

    assert len(nfts) > 0
    assert nfts[0].blockchain == Blockchain.Eth
    assert nfts[0].traits
    assert len(nfts[0].traits) > 0


@pytest.mark.webtest
def test_get_nft_metadata(client: AnkrAdvancedAPI) -> None:
    reply = client.get_nft_metadata(
        request=GetNFTMetadataRequest(
            blockchain=Blockchain.Eth,
            contractAddress="0x4100670ee2f8aef6c47a4ed13c7f246e621228ec",
            tokenId="4",
            forceFetch=False,
        )
    )

    assert reply.metadata
    assert reply.metadata.blockchain == Blockchain.Eth
    assert reply.metadata.contractType == "ERC1155"
    assert reply.attributes
    assert reply.attributes.name == "Overleveraged"


@pytest.mark.webtest
def test_get_nft_holders(client: AnkrAdvancedAPI) -> None:
    holders = list(
        client.get_nft_holders(
            request=GetNFTHoldersRequest(
                blockchain=Blockchain.Eth,
                contractAddress="0x4100670ee2f8aef6c47a4ed13c7f246e621228ec",
            ),
            limit=10,
        )
    )

    assert holders
    assert len(holders) == 10


@pytest.mark.webtest
def test_get_transactions(client: AnkrAdvancedAPI) -> None:
    tx = client.get_transaction(
        request=GetTransactionsByHashRequest(
            transactionHash="0x82c13aaac6f0b6471afb94a3a64ae89d45baa3608ad397621dbb0d847f51196f",
            includeLogs=True,
            decodeLogs=True,
            decodeTxData=True,
        )
    )

    assert tx
    assert (
        tx.hash == "0x82c13aaac6f0b6471afb94a3a64ae89d45baa3608ad397621dbb0d847f51196f"
    )
    assert tx.to == "0x98767abab06e45a181ab73ae4cd0fecd0fbd0cd0"
    assert tx.from_ == "0x64aa6f93e0e1f49ff4958990c40d4bf17dafc0eb"
    assert tx.logs
    assert tx.logs[0].event
    assert tx.logs[0].event.name == "Transfer"


@pytest.mark.webtest
def test_get_token_holders(client: AnkrAdvancedAPI) -> None:
    holders = list(
        client.get_token_holders(
            request=GetTokenHoldersRequest(
                blockchain=Blockchain.Bsc,
                contractAddress="0xf307910A4c7bbc79691fD374889b36d8531B08e3",
            ),
            limit=10,
        )
    )

    assert len(holders) == 10
    assert holders[0].holderAddress.startswith("0x")
    assert "." in holders[0].balance
    assert holders[0].balanceRawInteger.isnumeric()


@pytest.mark.webtest
def test_get_token_holders_pagination(client: AnkrAdvancedAPI) -> None:
    holders = list(
        client.get_token_holders(
            request=GetTokenHoldersRequest(
                blockchain=Blockchain.Bsc,
                contractAddress="0xf307910A4c7bbc79691fD374889b36d8531B08e3",
            ),
            limit=None,
        )
    )

    assert len(holders) > 1000
    assert holders[0].holderAddress.startswith("0x")
    assert "." in holders[0].balance
    assert holders[0].balanceRawInteger.isnumeric()


@pytest.mark.webtest
def test_get_token_holders_count_history(client: AnkrAdvancedAPI) -> None:
    daily_holders_counts = list(
        client.get_token_holders_count_history(
            request=GetTokenHoldersCountRequest(
                blockchain=Blockchain.Bsc,
                contractAddress="0xf307910A4c7bbc79691fD374889b36d8531B08e3",
            ),
            limit=10,
        )
    )

    assert len(daily_holders_counts) == 10
    assert daily_holders_counts[0].holderCount > 0
    datetime.datetime.strptime(
        daily_holders_counts[0].lastUpdatedAt, "%Y-%m-%dT%H:%M:%SZ"
    )


@pytest.mark.webtest
def test_get_token_holders_count(client: AnkrAdvancedAPI) -> None:
    holders_count = client.get_token_holders_count(
        request=GetTokenHoldersCountRequest(
            blockchain=Blockchain.Bsc,
            contractAddress="0xf307910A4c7bbc79691fD374889b36d8531B08e3",
        )
    )

    assert holders_count
    assert holders_count.holderCount > 0
    datetime.datetime.strptime(holders_count.lastUpdatedAt, "%Y-%m-%dT%H:%M:%SZ")


@pytest.mark.webtest
def test_get_account_balance(client: AnkrAdvancedAPI) -> None:
    assets = list(
        client.get_account_balance(
            request=GetAccountBalanceRequest(
                walletAddress="0x77A859A53D4de24bBC0CC80dD93Fbe391Df45527",
                blockchain=[Blockchain.Eth, Blockchain.Bsc],
            )
        )
    )

    assert assets
    assert len(assets) > 0


@pytest.mark.webtest
def test_get_token_price(client: AnkrAdvancedAPI) -> None:
    price = client.get_token_price(
        request=GetTokenPriceRequest(
            contractAddress="0x8290333cef9e6d528dd5618fb97a76f268f3edd4",
            blockchain=Blockchain.Eth,
        )
    )

    assert price
    assert float(price) > 0


@pytest.mark.webtest
def test_get_token_price__no_price(client: AnkrAdvancedAPI) -> None:
    price = client.get_token_price(
        request=GetTokenPriceRequest(
            contractAddress="0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee",
            blockchain=Blockchain.Eth,
        )
    )

    assert price == "0"
