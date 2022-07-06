# ⚓️ Ankr Python SDK

Compact Python library for interacting with Ankr's [Advanced APIs](https://www.ankr.com/advanced-api/).

## Get started in 2 minutes

#### 1. Install the package from PyPi

```bash
pip install ankr-sdk
```

#### 2. Initialize the SDK

```python3
from ankr import AnkrWeb3

ankr_w3 = AnkrWeb3()
```

#### 3. Use the sdk and call one of the supported methods

#### Node's API
```python3
eth_block = ankr_w3.eth.get_block("latest")
bsc_block = ankr_w3.bsc.get_block("latest")
polygon_block = ankr_w3.polygon.get_block("latest")
```

#### Ankr NFT API 

```python3
from ankr.types import Blockchain

nfts = ankr_w3.nft.get_nfts(
    blockchain=[Blockchain.ETH, Blockchain.BSC],
    wallet_address="0x0E11A192d574b342C51be9e306694C41547185DD",
    filter=[
        {"0x700b4b9f39bb1faf5d0d16a20488f2733550bff4": []},
        {"0xd8682bfa6918b0174f287b888e765b9a1b4dc9c3": ["8937"]},
    ],
)
```

#### Ankr Token API
```python3
assets = ankr_w3.token.get_account_balance(
    wallet_address="0x77A859A53D4de24bBC0CC80dD93Fbe391Df45527"
)
```

#### Ankr Query API
```python3
logs = ankr_w3.query.get_logs(
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

## Ankr Advanced APIs supported chains

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

- [`nft.get_nfts`](#get_nfts)
- [`nft.get_nft_metadata`](#get_nft_metadata)
- [`token.get_token_holders`](#get_token_holders)
- [`token.get_token_holders_count_history`](#get_token_holders_count_history)
- [`token.get_token_holders_count`](#get_token_holders_count)
- [`token.get_account_balance`](#get_account_balance)
- [`query.get_logs`](#get_logs)
- [`query.get_blocks`](#get_blocks)
- [`query.get_transaction`](#get_transaction)

#### `get_nfts`

Get data about all the NFTs (collectibles) owned by a wallet.

````python3
nfts = ankr_w3.nft.get_nfts(
    blockchain="eth",
    wallet_address="0x0E11A192d574b342C51be9e306694C41547185DD",
    filter=[
        {"0x700b4b9f39bb1faf5d0d16a20488f2733550bff4": []},
        {"0xd8682bfa6918b0174f287b888e765b9a1b4dc9c3": ["8937"]},
    ],
)
````

#### `get_nft_metadata`

Get metadata of NFT.

````python3
nfts = ankr_w3.nft.get_nft_metadata(
    blockchain="eth",
    contract_address="0x4100670ee2f8aef6c47a4ed13c7f246e621228ec",
    token_id="4",
)
````

#### `get_token_holders`

Get holders of a token.

````python3
holders = ankr_w3.token.get_token_holders(
    blockchain="bsc",
    contract_address="0xf307910A4c7bbc79691fD374889b36d8531B08e3",
    limit=10,
)
````

#### `get_token_holders_count_history`

Get token holders count daily history.

````python3
daily_holders_history = ankr_w3.token..get_token_holders_count_history(
    blockchain="bsc",
    contract_address="0xf307910A4c7bbc79691fD374889b36d8531B08e3",
    limit=10,  # last 10 days history
)
````

#### `get_token_holders_count`

Get token holders count at the latest block.

````python3
holders_count = ankr_w3.token..get_token_holders_count(
    blockchain="bsc",
    contract_address="0xf307910A4c7bbc79691fD374889b36d8531B08e3",
)
````

#### `get_account_balance`

Get account assets.

````python3
assets = ankr_w3.token..get_account_balance(
    wallet_address="0x77A859A53D4de24bBC0CC80dD93Fbe391Df45527",
    blockchain=["eth", "bsc"],
)
````

#### `get_logs`

Get logs matching the filter.

```python3
logs = ankr_w3.query.get_logs(
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
blocks = ankr_w3.query.get_blocks(
    blockchain="eth",
    from_block=14500001,
    to_block=14500001,
    desc_order=True,
    include_logs=True,
    include_txs=True,
    decode_logs=True,
)
```

#### `get_transaction`

Get Transaction by hash.

````python3
tx = ankr_w3.query.get_transaction(
    transaction_hash="0x82c13aaac6f0b6471afb94a3a64ae89d45baa3608ad397621dbb0d847f51196f",
    include_logs=True,
    decode_logs=True,
    decode_tx_data=True,
)
````


### About API keys

For now, Ankr is offering _free_ access to these APIs with no request limits i.e. you don't need an API key at this
time.

Later on, these APIs will become a part of Ankr Protocol's [Premium Plan](https://www.ankr.com/protocol/plan/).
