# ⚓️ Ankr Python SDK

Compact Python library for interacting with Ankr's [Advanced APIs](https://www.ankr.com/advanced-api/).

## Get started in 2 minutes

#### 1. Install the package from PyPi

```bash
pip install ankr-sdk
```

#### 2. Initialize the SDK

_Note: to use Advanced API for free starting from May 29th, 2023 you have to register on the platform._

Get your individual endpoint here https://www.ankr.com/rpc/advanced-api and provide it to the `AnkrWeb3` class.

```python3
from ankr import AnkrWeb3

ankr_w3 = AnkrWeb3("YOUR-TOKEN")
```

#### 3. Use the sdk and call one of the supported methods

#### Node's API
```python3
from ankr import AnkrWeb3
ankr_w3 = AnkrWeb3("YOUR-TOKEN")

eth_block = ankr_w3.eth.get_block("latest")
bsc_block = ankr_w3.bsc.get_block("latest")
polygon_block = ankr_w3.polygon.get_block("latest")
```

#### Ankr NFT API 

```python3
from ankr import AnkrWeb3
from ankr.types import Blockchain, GetNFTsByOwnerRequest

ankr_w3 = AnkrWeb3("YOUR-TOKEN")

nfts = ankr_w3.nft.get_nfts(
    request=GetNFTsByOwnerRequest(
        blockchain=Blockchain.Eth,
        walletAddress="0x0E11A192d574b342C51be9e306694C41547185DD"
    )
)
```

#### Ankr Token API
```python3
from ankr import AnkrWeb3
from ankr.types import GetAccountBalanceRequest

ankr_w3 = AnkrWeb3("YOUR-TOKEN")

assets = ankr_w3.token.get_account_balance(
    request=GetAccountBalanceRequest(
        walletAddress="0x77A859A53D4de24bBC0CC80dD93Fbe391Df45527"
    )
)
```

#### Ankr Query API
```python3
from ankr import AnkrWeb3
from ankr.types import Blockchain, GetLogsRequest

ankr_w3 = AnkrWeb3("YOUR-TOKEN")

logs = ankr_w3.query.get_logs(
    request=GetLogsRequest(
        blockchain=[Blockchain.Eth],
        fromBlock=1181739,
        toBlock=1181739,
        address=["0x3589d05a1ec4af9f65b0e5554e645707775ee43c"],
        topics=[
            [],
            ["0x000000000000000000000000feb92d30bf01ff9a1901666c5573532bfa07eeec"],
        ],
        decodeLogs=True,
    ),
    limit=10
)
```

## Ankr Advanced APIs supported chains

`ankr-sdk` supports the following chains at this time:

Mainnet

- Ethereum: `"eth"`
- BNB Smart Chain: `"bsc"`
- Polygon: `"polygon"`
- Fantom: `"fantom"`
- Arbitrum: `"arbitrum"`
- Avalanche: `"avalanche"`
- Syscoin NEVM: `"syscoin"`
- Optimism: `"optimism"`
- Polygon zkEVM: `"polygon_zkevm"`
- Rollux: `"rollux"`
- Base: `"base"`
- Flare: `"flare"`
- Gnosis Chain: `"gnosis"`
- Scroll: `"scroll"`
- Linea: `"linea"`

Testnet

- Ethereum Goerli: `"eth_goerli"`
- Avalanche Fuji: `"avalanche_fuji"`
- Polygon Mumbai: `"polygon_mumbai"`
- Optimism Testnet: `"optimism_testnet"`

Appchain

- META Apes: `"bas_metaapes"`

Appchain Testnet

- META Apes Testnet: `"bas_metaapes_testnet"`

When passing blockchain, you can use one available from `types.py` (preferred) or just a string value.  

## Available methods

`ankr-sdk` supports the following methods:

Early Access

- [`get_token_price_history`](#gettokenpricehistory--gettokenpricehistoryraw)
- [`get_account_balance_historical`](#getaccountbalancehistorical--getaccountbalancehistoricalraw)
- [`get_internal_transactions_by_block_number`](#getinternaltransactionsbyblocknumber--getinternaltransactionsbyblocknumberraw)
- [`get_internal_transactions_by_parent_hash`](#getinternaltransactionsbyparenthash--getinternaltransactionsbyparenthashraw)

Token API

- [`explain_token_price`](#explaintokenprice--explaintokenpriceraw)
- [`get_account_balance`](#getaccountbalance--getaccountbalanceraw)
- [`get_currencies`](#getcurrencies--getcurrenciesraw)
- [`get_token_holders`](#gettokenholders--gettokenholdersraw)
- [`get_token_holders_count_history`](#gettokenholderscounthistory--gettokenholderscounthistoryraw)
- [`get_token_holders_count`](#gettokenholderscount--gettokenholderscountraw)
- [`get_token_price`](#gettokenprice--gettokenpriceraw)
- [`getTokenTransfers`](#gettokentransfers--gettokentransfersraw)

NFT API

- [`getNFTsByOwner`](#getnftsbyowner)
- [`getNFTMetadata`](#getnftmetadata)
- [`getNFTHolders`](#getnftholders)
- [`getNftTransfers`](#getnfttransfers)

Query API

- [`getLogs`](#getlogs)
- [`getBlocks`](#getblocks)
- [`getTransactionsByHash`](#gettransactionsbyhash)
- [`getTransactionsByAddress`](#gettransactionsbyaddress)
- [`getBlockchainStats`](#getblockchainstats)
- [`getInteractions`](#getinteractions)


Note: some methods are available in *_raw format, allowing to get full reply with syncStatus and control pagination by hands.

### Pagination

- methods with *_raw ending support customized pagination, where you are controlling it, using `pageSize` and `pageToken`
- other methods support automatic pagination, DON'T use `pageSize` and `pageToken` fields to these methods

---

## Examples

### Early Access API

#### `get_token_price_history` / `get_token_price_history_raw`
```python3
from ankr import AnkrAdvancedAPI, AnkrWeb3
from ankr.types import Blockchain, GetTokenPriceHistoryRequest

ankr_w3 = AnkrWeb3("YOUR-TOKEN")

result = AnkrAdvancedAPI.get_token_price_history(
    request=GetTokenPriceHistoryRequest(
        blockchain=Blockchain.Eth,
        contractAddress='0x50327c6c5a14dcade707abad2e27eb517df87ab5',
        toTimestamp=1696970653,
        interval=100,
        limit=10
    )
)
print(result)
```

#### `get_account_balance_historical` / `get_account_balance_historical_raw`
```python3
from ankr import AnkrAdvancedAPI, AnkrWeb3
from ankr.types import Blockchain, GetAccountBalanceHistoricalRequest

ankr_w3 = AnkrWeb3("YOUR-TOKEN")

result = AnkrAdvancedAPI.get_account_balance_historical(
    request=GetAccountBalanceHistoricalRequest(
        blockchain=Blockchain.Eth,
        walletAddress='vitalik.eth',
        onlyWhitelisted=False,
        blockHeight=17967813,
    )
)
print(result)
```

#### `get_internal_transactions_by_block_number` / `get_internal_transactions_by_block_number_raw`
```python3
from ankr import AnkrAdvancedAPI, AnkrWeb3
from ankr.types import Blockchain, GetInternalTransactionsByBlockNumberRequest

ankr_w3 = AnkrWeb3("YOUR-TOKEN")

result = AnkrAdvancedAPI.get_internal_transactions_by_block_number(
    request=GetInternalTransactionsByBlockNumberRequest(
        blockchain=Blockchain.Eth,
        blockNumber=10000000,
        onlyWithValue=True,
    )
)
for transaction in result:
    print(transaction)
```

#### `get_internal_transactions_by_parent_hash` / `get_internal_transactions_by_parent_hash_raw`
```python3
from ankr import AnkrAdvancedAPI, AnkrWeb3
from ankr.types import Blockchain, GetInternalTransactionsByParentHashRequest

ankr_w3 = AnkrWeb3("YOUR-TOKEN")

result = AnkrAdvancedAPI.get_internal_transactions_by_parent_hash(
    request=GetInternalTransactionsByParentHashRequest(
        blockchain=Blockchain.Eth,
        parentTransactionHash='0xa50f8744e65cb76f66f9d54499d5401866a75d93db2e784952f55205afc3acc5',
        onlyWithValue=True,
    )
)
for transaction in result:
    print(transaction)
```

### Token API

#### `explain_token_price` / `explain_token_price_raw`

```python3
from ankr import AnkrAdvancedAPI, AnkrWeb3
from ankr.types import Blockchain, ExplainTokenPriceRequest

ankr_w3 = AnkrWeb3("YOUR-TOKEN")

pairs, estimates = AnkrAdvancedAPI.explain_token_price(
    request=ExplainTokenPriceRequest(
        blockchain=Blockchain.Eth,
        tokenAddress='0x8290333cef9e6d528dd5618fb97a76f268f3edd4',
        blockHeight=17463534,
    )
)

print(pairs)
print(estimates)
```

#### `get_account_balance` / `get_account_balance_raw`

```python3
from ankr import AnkrAdvancedAPI, AnkrWeb3
from ankr.types import GetAccountBalanceRequest

ankr_w3 = AnkrWeb3("YOUR-TOKEN")

result = AnkrAdvancedAPI.get_account_balance(
    request=GetAccountBalanceRequest(
        walletAddress="0x77A859A53D4de24bBC0CC80dD93Fbe391Df45527"
    )
)

for balance in result:
    print(balance)
```

#### `get_currencies` / `get_currencies_raw`

```python3
from ankr import AnkrAdvancedAPI, AnkrWeb3
from ankr.types import Blockchain, GetCurrenciesRequest

ankr_w3 = AnkrWeb3("YOUR-TOKEN")

result = AnkrAdvancedAPI.get_currencies(
    request=GetCurrenciesRequest(
        blockchain=Blockchain.Fantom,
    )
)

for currency in result:
    print(currency)
```

#### `get_token_holders` / `get_token_holders_raw`

```python3
from ankr import AnkrAdvancedAPI, AnkrWeb3
from ankr.types import Blockchain, GetTokenHoldersRequest

ankr_w3 = AnkrWeb3("YOUR-TOKEN")

result = AnkrAdvancedAPI.get_token_holders(
    request=GetTokenHoldersRequest(
        blockchain=Blockchain.Eth,
        contractAddress='0xdac17f958d2ee523a2206206994597c13d831ec7',
    )
)

for balance in result:
    print(balance)
```

#### `get_token_holders_count_history` / `get_token_holders_count_history_raw`

```python3
from ankr import AnkrAdvancedAPI, AnkrWeb3
from ankr.types import Blockchain, GetTokenHoldersCountRequest

ankr_w3 = AnkrWeb3("YOUR-TOKEN")

result = AnkrAdvancedAPI.get_token_holders_count_history_raw(
    request=GetTokenHoldersCountRequest(
        blockchain=Blockchain.Eth,
        contractAddress='0xdAC17F958D2ee523a2206206994597C13D831ec7',
    )
)

for balance in result:
    print(balance)
```

#### `get_token_holders_count` / `get_token_holders_count_raw`

```python3
from ankr import AnkrAdvancedAPI, AnkrWeb3
from ankr.types import Blockchain, GetTokenHoldersCountRequest

ankr_w3 = AnkrWeb3("YOUR-TOKEN")

result = AnkrAdvancedAPI.get_token_holders_count_history_raw(
    request=GetTokenHoldersCountRequest(
        blockchain=Blockchain.Eth,
        contractAddress='0xdAC17F958D2ee523a2206206994597C13D831ec7',
    )
)

print(result)
```

#### `get_token_price` / `get_token_price_raw`

```python3
from ankr import AnkrAdvancedAPI, AnkrWeb3
from ankr.types import Blockchain, GetTokenPriceRequest

ankr_w3 = AnkrWeb3("YOUR-TOKEN")

result = AnkrAdvancedAPI.get_token_price(
    request=GetTokenPriceRequest(
        blockchain=Blockchain.Eth,
        contractAddress='',
    )
)

print(result)
```

#### `get_token_transfers` / `get_token_transfers_raw`

```python3
from ankr import AnkrAdvancedAPI, AnkrWeb3
from ankr.types import Blockchain, GetTransfersRequest

ankr_w3 = AnkrWeb3("YOUR-TOKEN")

result = AnkrAdvancedAPI.get_token_transfers(
    request=GetTransfersRequest(
        blockchain=Blockchain.Eth,
        address=['0xf16e9b0d03470827a95cdfd0cb8a8a3b46969b91'],
        fromTimestamp=1674441035,
        toTimestamp=1674441035,
        descOrder=True,
    )
)

for transfer in result:
    print(result)
```



### About API keys

Ankr is offering _free_ access to Advanced API, however you have to register on Ankr platform to access it.

Get your individual API Key here https://www.ankr.com/rpc/advanced-api.
