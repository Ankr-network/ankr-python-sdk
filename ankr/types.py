from __future__ import annotations

import enum
from abc import ABC
from typing import Dict, List, Optional, Type, Union

import humps
from pydantic import BaseModel


class Blockchain(str, enum.Enum):
    ETH = "eth"
    BSC = "bsc"
    POLYGON = "polygon"
    FANTOM = "fantom"
    ARBITRUM = "arbitrum"
    AVALANCHE = "avalanche"
    SYSCOIN = "syscoin"


class NftContractType(str, enum.Enum):
    ERC721 = "ERC721"
    ERC1155 = "ERC1155"
    UNDEFINED = "UNDEFINED"


class BlockNumberName(str, enum.Enum):
    latest = "latest"
    earliest = "earliest"


BlockchainName = Union[Blockchain, str]
BlockchainNames = Union[BlockchainName, List[BlockchainName]]
BlockNumber = Union[int, str, BlockNumberName]
AddressOrAddresses = Union[str, List[str]]
Topics = Union[str, List[Union[str, List[str]]]]


class RPCModel(BaseModel):
    class Config:
        alias_generator = humps.camelize
        allow_population_by_field_name = True


class RPCRequestPaginated(ABC, RPCModel):
    page_token: Optional[str] = None


class RPCReplyPaginated(ABC, RPCModel):
    next_page_token: Optional[str] = None
    _iter_type: Type


class GetNFTsByOwnerRequest(RPCRequestPaginated):
    blockchain: BlockchainNames
    wallet_address: str
    filter: Optional[List[Dict[str, List[str]]]] = None
    page_token: Optional[str] = None
    page_size: Optional[int] = None


class Attribute(RPCModel):
    trait_type: Optional[str] = None
    value: Optional[str] = None
    display_type: Optional[str] = None
    bunny_id: Optional[str] = None
    count: Optional[int] = None
    frequency: Optional[str] = None
    mp_score: Optional[str] = None
    rarity: Optional[str] = None


class Nft(RPCModel):
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


class GetNFTsByOwnerReply(RPCReplyPaginated):
    owner: str
    assets: List[Nft]
    next_page_token: str


class GetNFTMetadataRequest(RPCModel):
    blockchain: BlockchainName
    contract_address: str
    token_id: str


class NftAttributes(RPCModel):
    token_url: str
    image_url: str
    name: str
    description: str
    contract_type: NftContractType
    traits: Optional[List[Attribute]] = None


class NftMetadata(RPCModel):
    blockchain: BlockchainName
    contract_address: str
    token_id: str
    contract_type: NftContractType


class GetNFTMetadataReply(RPCModel):
    metadata: Optional[NftMetadata] = None
    attributes: Optional[NftAttributes] = None


class Balance(RPCModel):
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


class GetAccountBalanceReply(RPCReplyPaginated):
    total_balance_usd: str
    assets: List[Balance]
    next_page_token: Optional[str] = None


class GetAccountBalanceRequest(RPCRequestPaginated):
    blockchain: Optional[BlockchainNames]
    wallet_address: str
    page_token: Optional[str] = None
    page_size: Optional[int] = None


class GetTokenHoldersRequest(RPCRequestPaginated):
    blockchain: BlockchainName
    contract_address: str
    page_token: Optional[str] = None
    page_size: Optional[int] = None


class HolderBalance(RPCModel):
    holder_address: str
    balance: str
    balance_raw_integer: str


class GetTokenHoldersReply(RPCReplyPaginated):
    blockchain: BlockchainName
    contract_address: str
    token_decimals: int
    holders: List[HolderBalance]
    holders_count: int
    next_page_token: str


class GetTokenHoldersCountRequest(RPCRequestPaginated):
    blockchain: BlockchainName
    contract_address: str
    page_token: Optional[str] = None
    page_size: Optional[int] = None


class DailyHolderCount(RPCModel):
    holder_count: int
    total_amount: str
    total_amount_raw_integer: str
    last_updated_at: str


class GetTokenHoldersCountReply(RPCReplyPaginated):
    blockchain: BlockchainName
    contract_address: str
    token_decimals: int
    holder_count_history: List[DailyHolderCount]
    next_page_token: str


class GetCurrenciesRequest(RPCModel):
    blockchain: BlockchainName


class CurrencyDetailsExtended(RPCModel):
    blockchain: BlockchainName
    address: Optional[str]
    name: str
    decimals: int
    symbol: str
    thumbnail: str


class GetCurrenciesReply(RPCModel):
    currencies: List[CurrencyDetailsExtended]


class GetUsdPriceRequest(RPCModel):
    blockchain: BlockchainName
    contract_address: str


class GetUsdPriceReply(RPCModel):
    usd_price: str
    blockchain: BlockchainName
    contract_address: Optional[str] = None


class EventInput(RPCModel):
    name: str
    type: str
    indexed: bool
    size: int
    value_decoded: str


class Event(RPCModel):
    name: str
    inputs: List[EventInput]
    anonymous: bool
    string: str
    signature: str
    id: str
    verified: bool


class Log(RPCModel):
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


class GetLogsReply(RPCReplyPaginated):
    logs: List[Log]
    next_page_token: Optional[str] = None


class GetLogsRequest(RPCRequestPaginated):
    blockchain: BlockchainNames
    from_block: Optional[BlockNumber] = None
    to_block: Optional[BlockNumber] = None
    address: Optional[Union[str, List[str]]] = None
    topics: Optional[Topics] = None
    page_token: Optional[str] = None
    page_size: Optional[int] = None
    decode_logs: Optional[bool] = None


class GetBlocksRequest(RPCModel):
    blockchain: BlockchainName
    from_block: Optional[BlockNumber] = None
    to_block: Optional[BlockNumber] = None
    desc_order: Optional[bool] = None
    include_logs: Optional[bool] = None
    include_txs: Optional[bool] = None
    decode_logs: Optional[bool] = None
    decode_tx_data: Optional[bool] = None


class MethodInput(RPCModel):
    name: str
    type: str
    size: int
    value_decoded: str


class Method(RPCModel):
    name: str
    inputs: List[MethodInput]
    string: str
    signature: str
    id: str
    verified: bool


class Transaction(RPCModel):
    class Config:
        fields = {
            "from_address": "from",
            "to_address": "to",
        }

    v: str
    r: str
    s: str
    nonce: str
    gas: str
    gas_price: str
    input: str
    block_number: str
    to_address: Optional[str]
    from_address: str
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


class Block(RPCModel):
    blockchain: str
    number: str
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


class GetBlocksReply(RPCModel):
    blocks: List[Block]


class GetTransactionsByHashRequest(RPCModel):
    blockchain: Optional[BlockchainNames]
    transaction_hash: str
    include_logs: Optional[bool] = None
    decode_logs: Optional[bool] = None
    decode_tx_data: Optional[bool] = None


class GetTransactionsByHashReply(RPCModel):
    transactions: List[Transaction]
