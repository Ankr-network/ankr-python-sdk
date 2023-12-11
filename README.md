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
- [`get_token_transfers`](#gettokentransfers--gettokentransfersraw)

NFT API

- [`get_nfts`](#getnfts--getnftsraw)
- [`get_nft_metadata`](#getnftmetadata--getnftmetadataraw)
- [`get_nft_holders`](#getnftholders--getnftholdersraw)
- [`get_nft_transfers`](#getnfttransfers--getnfttransfersraw)

Query API

- [`get_logs`](#getlogs--getlogsraw)
- [`get_blocks`](#getblocks--getblocksraw)
- [`get_transaction`](#gettransaction--gettransactionraw)
- [`get_transactions_by_address`](#gettransactionsbyaddress--gettransactionsbyaddressraw)
- [`get_blockchain_stats`](#getblockchainstats--getblockchainstatsraw)
- [`get_interactions`](#getinteractions--getinteractionsraw)


Note: some methods are available in *_raw format, allowing to get full reply with syncStatus and control pagination by hands.

### Pagination

- methods with *_raw ending support customized pagination, where you are controlling it, using `pageSize` and `pageToken`
- other methods support automatic pagination, DON'T use `pageSize` and `pageToken` fields to these methods

---

## Examples

### Early Access API

#### `get_token_price_history` / `get_token_price_history_raw`

Get a list of history of the price for given contract to given timestamp.

```python3
from ankr import AnkrAdvancedAPI
from ankr.types import Blockchain, GetTokenPriceHistoryRequest

advancedAPI = AnkrAdvancedAPI("YOUR-TOKEN")

result = advancedAPI.get_token_price_history(
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

Get the coin and token balances of the wallet at specified block.

```python3
from ankr import AnkrAdvancedAPI
from ankr.types import Blockchain, GetAccountBalanceHistoricalRequest

advancedAPI = AnkrAdvancedAPI("YOUR-TOKEN")

result = advancedAPI.get_account_balance_historical(
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

Get a list of internal transactions in the block.

```python3
from ankr import AnkrAdvancedAPI
from ankr.types import Blockchain, GetInternalTransactionsByBlockNumberRequest

advancedAPI = AnkrAdvancedAPI("YOUR-TOKEN")

result = advancedAPI.get_internal_transactions_by_block_number(
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

Get a list of internal transactions in the transaction.

```python3
from ankr import AnkrAdvancedAPI
from ankr.types import Blockchain, GetInternalTransactionsByParentHashRequest

advancedAPI = AnkrAdvancedAPI("YOUR-TOKEN")

result = advancedAPI.get_internal_transactions_by_parent_hash(
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

Get a list of tokens and pool how price for calculated.

```python3
from ankr import AnkrAdvancedAPI
from ankr.types import Blockchain, ExplainTokenPriceRequest

advancedAPI = AnkrAdvancedAPI("YOUR-TOKEN")

pairs, estimates = advancedAPI.explain_token_price(
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

Get the coin and token balances of a wallet.

```python3
from ankr import AnkrAdvancedAPI
from ankr.types import GetAccountBalanceRequest

advancedAPI = AnkrAdvancedAPI("YOUR-TOKEN")

result = advancedAPI.get_account_balance(
    request=GetAccountBalanceRequest(
        walletAddress="0x77A859A53D4de24bBC0CC80dD93Fbe391Df45527"
    )
)

for balance in result:
    print(balance)
```

#### `get_currencies` / `get_currencies_raw`

Get a list of supported currencies for a given blockchain.

```python3
from ankr import AnkrAdvancedAPI
from ankr.types import Blockchain, GetCurrenciesRequest

advancedAPI = AnkrAdvancedAPI("YOUR-TOKEN")

result = advancedAPI.get_currencies(
    request=GetCurrenciesRequest(
        blockchain=Blockchain.Fantom,
    )
)

for currency in result:
    print(currency)
```

#### `get_token_holders` / `get_token_holders_raw`

Get the list of token holders for a given contract address.

```python3
from ankr import AnkrAdvancedAPI
from ankr.types import Blockchain, GetTokenHoldersRequest

advancedAPI = AnkrAdvancedAPI("YOUR-TOKEN")

result = advancedAPI.get_token_holders(
    request=GetTokenHoldersRequest(
        blockchain=Blockchain.Eth,
        contractAddress='0xdac17f958d2ee523a2206206994597c13d831ec7',
    )
)

for balance in result:
    print(balance)
```

#### `get_token_holders_count_history` / `get_token_holders_count_history_raw`

Get historical data about the number of token holders for a given contract address.

```python3
from ankr import AnkrAdvancedAPI
from ankr.types import Blockchain, GetTokenHoldersCountRequest

advancedAPI = AnkrAdvancedAPI("YOUR-TOKEN")

result = advancedAPI.get_token_holders_count_history(
    request=GetTokenHoldersCountRequest(
        blockchain=Blockchain.Eth,
        contractAddress='0xdAC17F958D2ee523a2206206994597C13D831ec7',
    )
)

for balance in result:
    print(balance)
```

#### `get_token_holders_count` / `get_token_holders_count_raw`

Get current data about the number of token holders for a given contract address.

```python3
from ankr import AnkrAdvancedAPI
from ankr.types import Blockchain, GetTokenHoldersCountRequest

advancedAPI = AnkrAdvancedAPI("YOUR-TOKEN")

result = advancedAPI.get_token_holders_count_history_raw(
    request=GetTokenHoldersCountRequest(
        blockchain=Blockchain.Eth,
        contractAddress='0xdAC17F958D2ee523a2206206994597C13D831ec7',
    )
)

print(result)
```

#### `get_token_price` / `get_token_price_raw`

Get token price by contract.

```python3
from ankr import AnkrAdvancedAPI
from ankr.types import Blockchain, GetTokenPriceRequest

advancedAPI = AnkrAdvancedAPI("YOUR-TOKEN")

result = advancedAPI.get_token_price(
    request=GetTokenPriceRequest(
        blockchain=Blockchain.Eth,
        contractAddress='',
    )
)

print(result)
```

#### `get_token_transfers` / `get_token_transfers_raw`

Get token transfers of specified address.

```python3
from ankr import AnkrAdvancedAPI
from ankr.types import Blockchain, GetTransfersRequest

advancedAPI = AnkrAdvancedAPI("YOUR-TOKEN")

result = advancedAPI.get_token_transfers(
    request=GetTransfersRequest(
        blockchain=Blockchain.Eth,
        address=['0xf16e9b0d03470827a95cdfd0cb8a8a3b46969b91'],
        fromTimestamp=1674441035,
        toTimestamp=1674441035,
        descOrder=True,
    )
)

for transfer in result:
    print(transfer)
```

### NFT API

#### `get_nfts` / `get_nfts_raw`

Get data about all the NFTs (collectibles) owned by a wallet.

```python3
from ankr import AnkrAdvancedAPI
from ankr.types import Blockchain, GetNFTsByOwnerRequest

advancedAPI = AnkrAdvancedAPI("YOUR-TOKEN")

result = advancedAPI.get_nfts(
    request=GetNFTsByOwnerRequest(
        blockchain=Blockchain.Eth,
        walletAddress='0x0E11A192d574b342C51be9e306694C41547185DD',
    )
)

for nft in result:
    print(nft)
```

#### `get_nft_metadata` / `get_nft_metadata_raw`

Get NFT's contract metadata.

```python3
from ankr import AnkrAdvancedAPI
from ankr.types import Blockchain, GetNFTMetadataRequest

advancedAPI = AnkrAdvancedAPI("YOUR-TOKEN")

reply = advancedAPI.get_nft_metadata(
    request=GetNFTMetadataRequest(
        blockchain=Blockchain.Eth,
        contractAddress='0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d',
        tokenId='1500',
        forceFetch=False,
    )
)

print(reply.metadata)
print(reply.attributes)
```

#### `get_nft_holders` / `get_nft_holders_raw`

Get NFT's holders.

```python3
from ankr import AnkrAdvancedAPI
from ankr.types import Blockchain, GetNFTHoldersRequest

advancedAPI = AnkrAdvancedAPI("YOUR-TOKEN")

result = advancedAPI.get_nft_holders(
    request=GetNFTHoldersRequest(
        blockchain=Blockchain.Arbitrum,
        contractAddress='0xc36442b4a4522e871399cd717abdd847ab11fe88',
    ),
    limit=1000
)

for holder in result:
    print(holder)
```

#### `get_nft_transfers` / `get_nft_transfers_raw`

Get NFT Transfers of specified address.

```python3
from ankr import AnkrAdvancedAPI
from ankr.types import Blockchain, GetTransfersRequest

advancedAPI = AnkrAdvancedAPI("YOUR-TOKEN")

result = advancedAPI.get_nft_transfers(
    request=GetTransfersRequest(
        blockchain=[Blockchain.Eth, Blockchain.Bsc],
        address=['0xd8da6bf26964af9d7eed9e03e53415d37aa96045'],
        fromTimestamp=1672553107,
        toTimestamp=1672683207,
    )
)

for transfer in result:
    print(transfer)
```

### Query API

#### `get_logs` / `get_logs_raw`

Get logs matching the filter.

```python3
from ankr import AnkrAdvancedAPI
from ankr.types import Blockchain, GetLogsRequest

advancedAPI = AnkrAdvancedAPI("YOUR-TOKEN")

result = advancedAPI.get_logs(
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

for log in result:
    print(log)
```

#### `get_blocks` / `get_blocks_raw`

Query data about blocks within a specified range.

```python3
from ankr import AnkrAdvancedAPI
from ankr.types import Blockchain, GetBlocksRequest

advancedAPI = AnkrAdvancedAPI("YOUR-TOKEN")

result = advancedAPI.get_blocks(
    request=GetBlocksRequest(
        blockchain=Blockchain.Eth,
        fromBlock=14500001,
        toBlock=14500004,
        descOrder=True,
        includeLogs=True,
        includeTxs=True,
        decodeLogs=True,
    )
)

for block in result:
    print(block)
```

#### `get_transaction` / `get_transaction_raw`

Query data about transaction by the transaction hash.

```python3
from ankr import AnkrAdvancedAPI
from ankr.types import GetTransactionsByHashRequest

advancedAPI = AnkrAdvancedAPI("YOUR-TOKEN")

result = advancedAPI.get_transaction(
    request=GetTransactionsByHashRequest(
        transactionHash='0x82c13aaac6f0b6471afb94a3a64ae89d45baa3608ad397621dbb0d847f51196f',
        decodeTxData=True
    )
)

print(result)
```

#### `get_transactions_by_address` / `get_transactions_by_address_raw`

Query data about transactions of specified address.

```python3
from ankr import AnkrAdvancedAPI
from ankr.types import Blockchain, GetTransactionsByAddressRequest

advancedAPI = AnkrAdvancedAPI("YOUR-TOKEN")

result = advancedAPI.get_transactions_by_address(
    request=GetTransactionsByAddressRequest(
        blockchain=Blockchain.Bsc,
        fromBlock=23593283,
        toBlock=23593283,
        address=[
            "0x97242e3315c7ece760dc7f83a7dd8af6659f8c4c"
        ],
        descOrder=True,
    )
)

for transaction in result:
    print(transaction)
```

#### `get_blockchain_stats` / `get_blockchain_stats_raw`

Returns blockchain stats (num of txs, etc.).

```python3
from ankr import AnkrAdvancedAPI
from ankr.types import Blockchain, GetBlockchainStatsRequest

advancedAPI = AnkrAdvancedAPI("YOUR-TOKEN")

result = advancedAPI.get_blockchain_stats(
    request=GetBlockchainStatsRequest(
        blockchain=Blockchain.Bsc,
    )
)

for stat in result:
    print(stat)
```

#### `get_interactions` / `get_interactions_raw`

Returns on which chain address was interacting.

```python3
from ankr import AnkrAdvancedAPI
from ankr.types import GetInteractionsRequest

advancedAPI = AnkrAdvancedAPI("YOUR-TOKEN")

result = advancedAPI.get_interactions(
    request=GetInteractionsRequest(
        address='0xF977814e90dA44bFA03b6295A0616a897441aceC',
    )
)

for blockchain in result:
    print(blockchain)
```



### About API keys

Ankr is offering _free_ access to Advanced API, however you have to register on Ankr platform to access it.

Get your individual API Key here https://www.ankr.com/rpc/advanced-api.
