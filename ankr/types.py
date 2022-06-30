import enum
from abc import ABC
from typing import List, Optional, Union, Dict, Iterable, Type

import humps
from pydantic import BaseModel


class BlockchainName(str, enum.Enum):
    ETH = "eth"
    BSC = "bsc"
    POLYGON = "polygon"
    FANTOM = "fantom"
    ARBITRUM = "arbitrum"
    AVALANCHE = "avalanche"
    SYSCOIN = "syscoin"


BlockchainNames = Union[BlockchainName, List[BlockchainName], str]


class BlockNumberName(str, enum.Enum):
    latest = "latest"
    earliest = "earliest"


BlockNumber = Union[int, str, BlockNumberName]
AddressOrAddresses = Union[str, List[str]]
Topics = Union[str, List[Union[str, List[str]]]]


class JsonRPCModel(BaseModel):
    class Config:
        alias_generator = humps.camelize
        allow_population_by_field_name = True


class RequestPaginated(ABC, JsonRPCModel):
    page_token: Optional[str] = None


class ReplyPaginated(ABC, JsonRPCModel):
    next_page_token: Optional[str] = None
    _iter_type: Type

    def __next__(self) -> Iterable:
        ...


class GetNFTsByOwnerRequest(RequestPaginated):
    blockchain: BlockchainNames
    wallet_address: str
    filter: Optional[List[Dict[str, List[str]]]] = None
    page_token: Optional[str] = None
    page_size: Optional[int] = None


class Attribute(JsonRPCModel):
    trait_type: Optional[str] = None
    value: Optional[str] = None
    display_type: Optional[str] = None
    bunny_id: Optional[str] = None
    count: Optional[int] = None
    frequency: Optional[str] = None
    mp_score: Optional[str] = None
    rarity: Optional[str] = None


class Nft(JsonRPCModel):
    blockchain: BlockchainName
    name: str
    token_id: str
    token_url: str
    image_url: str
    collection_name: str
    symbol: str
    contract_type: str
    contract_address: str
    quantity: Optional[str] = None
    traits: Optional[List[Attribute]] = None


class GetNFTsByOwnerReply(ReplyPaginated):
    owner: str
    assets: List[Nft]
    next_page_token: str


class GetNFTMetadataRequest(JsonRPCModel):
    blockchain: BlockchainName
    contract_address: str
    token_id: str


class NftAttributes(JsonRPCModel):
    token_url: str
    image_url: str
    name: str
    description: str
    contract_type: int
    traits: Optional[List[Attribute]] = None


class NftMetadata(JsonRPCModel):
    blockchain: BlockchainName
    contract_address: str
    token_id: str
    contract_type: int


class GetNFTMetadataReply(JsonRPCModel):
    metadata: Optional[NftMetadata] = None
    attributes: Optional[NftAttributes] = None


class Balance(JsonRPCModel):
    blockchain: str
    token_name: str
    token_symbol: str
    token_decimals: int
    token_type: str
    holder_address: str
    balance: str
    balance_raw_integer: str
    balance_usd: str
    token_price: str
    thumbnail: str
    contract_address: Optional[str] = None


class GetAccountBalanceReply(ReplyPaginated):
    total_balance_usd: str
    assets: List[Balance]
    next_page_token: Optional[str] = None


class GetAccountBalanceRequest(RequestPaginated):
    blockchain: Union[BlockchainName, List[BlockchainName], None]
    wallet_address: str
    page_token: Optional[str] = None
    page_size: Optional[int] = None


class GetTokenHoldersRequest(RequestPaginated):
    blockchain: BlockchainName
    contract_address: str
    page_token: Optional[str] = None
    page_size: Optional[int] = None


class HolderBalance(JsonRPCModel):
    holder_address: str
    balance: str
    balance_raw_integer: str


class GetTokenHoldersReply(ReplyPaginated):
    blockchain: BlockchainName
    contract_address: str
    token_decimals: int
    holders: List[HolderBalance]
    holders_count: int
    next_page_token: str


class GetTokenHoldersCountRequest(RequestPaginated):
    blockchain: BlockchainName
    contract_address: str
    page_token: Optional[str] = None
    page_size: Optional[int] = None


class DailyHolderCount(JsonRPCModel):
    holder_count: int
    total_amount: str
    total_amount_raw_integer: str
    last_updated_at: str


class GetTokenHoldersCountReply(ReplyPaginated):
    blockchain: BlockchainName
    contract_address: str
    token_decimals: int
    holder_count_history: List[DailyHolderCount]
    next_page_token: str


class GetCurrenciesRequest(JsonRPCModel):
    blockchain: BlockchainName


class CurrencyDetailsExtended(JsonRPCModel):
    blockchain: BlockchainName
    address: Optional[str]
    name: str
    decimals: int
    symbol: str
    thumbnail: str


class GetCurrenciesReply(JsonRPCModel):
    currencies: List[CurrencyDetailsExtended]


class GetUsdPriceRequest(JsonRPCModel):
    blockchain: BlockchainName
    contract_address: str


class GetUsdPriceReply(JsonRPCModel):
    usd_price: str
    blockchain: BlockchainName
    contract_address: Optional[str] = None


class EventInput(JsonRPCModel):
    name: str
    type: str
    indexed: bool
    size: int
    value_decoded: str


class Event(JsonRPCModel):
    name: str
    inputs: List[EventInput]
    anonymous: bool
    string: str
    signature: str
    id: str
    verified: bool


class Log(JsonRPCModel):
    address: str
    topics: List[str]
    data: str
    block_number: str
    transaction_hash: str
    transaction_index: str
    block_hash: str
    log_index: str
    removed: bool
    event: Optional[Event] = None


class GetLogsReply(ReplyPaginated):
    logs: List[Log]
    next_page_token: Optional[str] = None


class GetLogsRequest(RequestPaginated):
    blockchain: Union[BlockchainName, List[BlockchainName]]
    from_block: Union[int, str, BlockNumberName, None] = None
    to_block: Union[int, str, BlockNumberName, None] = None
    address: Optional[Union[str, List[str]]] = None
    topics: Optional[Union[str, List[Union[str, List[str]]]]] = None
    page_token: Optional[str] = None
    page_size: Optional[int] = None
    decode_logs: Optional[bool] = None


class GetBlocksRequest(JsonRPCModel):
    blockchain: BlockchainName
    from_block: Union[int, BlockNumberName, None]
    to_block: Union[int, BlockNumberName, None]
    desc_order: Optional[bool] = None
    include_logs: Optional[bool] = None
    include_txs: Optional[bool] = None
    decode_logs: Optional[bool] = None
    decode_tx_data: Optional[bool] = None


class MethodInput(JsonRPCModel):
    name: str
    type: str
    size: int
    value_decoded: str


class Method(JsonRPCModel):
    name: str
    inputs: List[MethodInput]
    string: str
    signature: str
    id: str
    verified: bool


class Transaction(JsonRPCModel):
    class Config:
        fields = {"from": "from"}

    v: str
    r: str
    s: str
    nonce: str
    gas: str
    gas_price: str
    input: str
    block_number: str
    to: Optional[str]
    transaction_index: str
    block_hash: str
    value: str
    type: str
    contract_address: Optional[str]
    cumulative_gas_used: str
    gas_used: str
    logs: List[Log]
    logs_bloom: str
    transaction_hash: str
    hash: str
    status: str
    blockchain: str
    timestamp: str
    method: Optional[Method]


class Block(JsonRPCModel):
    blockchain: str
    int: str
    hash: str
    parent_hash: str
    nonce: str
    mix_hash: str
    sha3_uncles: str
    logs_bloom: str
    state_root: str
    miner: str
    difficulty: str
    extra_data: str
    size: str
    gas_limit: str
    gas_used: str
    timestamp: str
    transactions_root: str
    receipts_root: str
    total_difficulty: str
    transactions: List[Transaction]
    uncles: List[str]


class GetBlocksReply(JsonRPCModel):
    blocks: List[Block]


class GetTransactionsByHashRequest(JsonRPCModel):
    blockchain: Union[BlockchainName, List[BlockchainName], None]
    transaction_hash: str
    include_logs: Optional[bool] = None
    decode_logs: Optional[bool] = None
    decode_tx_data: Optional[bool] = None


class GetTransactionsByHashReply(JsonRPCModel):
    transactions: List[Transaction]
