# ⚓️ Ankr Python SDK

Compact Python library for interacting with Ankr's [Advanced APIs](https://www.ankr.com/advanced-api/).

## Get started in 2 minutes

#### 1. Install the package from PyPi

```bash
pip install ankr-sdk
```

#### 2. Initialize the SDK

```python3
from ankr import AnkrAdvancedAPI, types

ankr_api = AnkrAdvancedAPI()
```

#### 3. Use the sdk and call one of the supported methods

```python3
from ankr.types import BlockchainName

nfts = ankr_api.get_nfts(
    blockchain=BlockchainName.ETH,
    wallet_address="0x0E11A192d574b342C51be9e306694C41547185DD",
    filter=[
        {"0x700b4b9f39bb1faf5d0d16a20488f2733550bff4": []},
        {"0xd8682bfa6918b0174f287b888e765b9a1b4dc9c3": ["8937"]},
    ],
)
```

## Supported chains

`ankr-sdk` supports the following chains at this time:

- ETH: `"eth"`
- BSC: `"bsc"`
- Polygon: `"polygon"`
- Fantom: `"fantom"`
- Arbitrum: `"arbitrum"`
- Avalanche: `"avalanche"`
- Syscoin NEVM: `"syscoin"`

## Available methods

`ankr-sdk` supports the following methods:

- [`get_nfts`](#get_nfts)
- [`get_logs`](#get_logs)
- [`get_blocks`](#get_blocks)

#### `get_logs`

Get logs matching the filter.

```python3
logs = ankr_api.get_logs(
    blockchain="eth",
    from_block="0xdaf6b1",
    to_block=14350010,
    address=["0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"],
    topics=[
        [],
        ["0x000000000000000000000000def1c0ded9bec7f1a1670819833240f027b25eff"],
    ],
    decode_logs=True,
)
```

#### `get_blocks`

Query data about blocks within a specified range.

```python3
blocks = ankr_api.get_blocks(
    blockchain="eth",
    from_block=14500001,
    to_block=14500001,
    desc_order=True,
    include_logs=True,
    include_txs=True,
    decode_logs=True,
)
```

#### `get_nfts`

Get data about all the NFTs (collectibles) owned by a wallet.

````python3
nfts = ankr_api.get_nfts(
    blockchain="eth",
    wallet_address="0x0E11A192d574b342C51be9e306694C41547185DD",
    filter=[
        {"0x700b4b9f39bb1faf5d0d16a20488f2733550bff4": []},
        {"0xd8682bfa6918b0174f287b888e765b9a1b4dc9c3": ["8937"]},
    ],
)
````


### About API keys

For now, Ankr is offering _free_ access to these APIs with no request limits i.e. you don't need an API key at this time.

Later on, these APIs will become a part of Ankr Protocol's [Premium Plan](https://www.ankr.com/protocol/plan/).
