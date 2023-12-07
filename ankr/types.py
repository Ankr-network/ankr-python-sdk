from __future__ import annotations
from enum import Enum
from typing import Literal, List, Dict


class SyncStatus:
    def __init__(self, lag: str, status: str, timestamp: float):
        self.lag = lag
        self.status = status
        self.timestamp = timestamp

    @classmethod
    def from_dict(cls, **data):
        return cls(
            lag=data.get("lag"),
            status=data.get("status"),
            timestamp=data.get("timestamp"),
        )


class MethodInput:
    def __init__(self, name: str, size: float, type: str, valueDecoded: str):
        self.name = name
        self.size = size
        self.type = type
        self.valueDecoded = valueDecoded

    @classmethod
    def from_dict(cls, **data):
        return cls(
            name=data.get("name"),
            size=data.get("size"),
            type=data.get("type"),
            valueDecoded=data.get("valueDecoded"),
        )


class Method:
    def __init__(
        self,
        id: str,
        inputs: List[MethodInput],
        name: str,
        signature: str,
        string: str,
        verified: bool,
    ):
        self.id = id
        self.inputs = inputs
        self.name = name
        self.signature = signature
        self.string = string
        self.verified = verified

    @classmethod
    def from_dict(cls, **data):
        return cls(
            id=data.get("id"),
            inputs=[
                MethodInput.from_dict(**methodinput_data)
                for methodinput_data in data.get("inputs", [])
            ],
            name=data.get("name"),
            signature=data.get("signature"),
            string=data.get("string"),
            verified=data.get("verified"),
        )


class EventInput:
    def __init__(
        self, indexed: bool, name: str, size: float, type: str, valueDecoded: str
    ):
        self.indexed = indexed
        self.name = name
        self.size = size
        self.type = type
        self.valueDecoded = valueDecoded

    @classmethod
    def from_dict(cls, **data):
        return cls(
            indexed=data.get("indexed"),
            name=data.get("name"),
            size=data.get("size"),
            type=data.get("type"),
            valueDecoded=data.get("valueDecoded"),
        )


class Event:
    def __init__(
        self,
        anonymous: bool,
        id: str,
        inputs: List[EventInput],
        name: str,
        signature: str,
        string: str,
        verified: bool,
    ):
        self.anonymous = anonymous
        self.id = id
        self.inputs = inputs
        self.name = name
        self.signature = signature
        self.string = string
        self.verified = verified

    @classmethod
    def from_dict(cls, **data):
        return cls(
            anonymous=data.get("anonymous"),
            id=data.get("id"),
            inputs=[
                EventInput.from_dict(**eventinput_data)
                for eventinput_data in data.get("inputs", [])
            ],
            name=data.get("name"),
            signature=data.get("signature"),
            string=data.get("string"),
            verified=data.get("verified"),
        )


class Log:
    def __init__(
        self,
        address: str,
        blockHash: str,
        blockNumber: str,
        blockchain: Blockchain,
        data: str,
        logIndex: str,
        removed: bool,
        topics: List[str],
        transactionHash: str,
        transactionIndex: str,
        event: Event = None,
    ):
        self.address = address
        self.blockHash = blockHash
        self.blockNumber = blockNumber
        self.blockchain = blockchain
        self.data = data
        self.logIndex = logIndex
        self.removed = removed
        self.topics = topics
        self.transactionHash = transactionHash
        self.transactionIndex = transactionIndex
        self.event = event

    @classmethod
    def from_dict(cls, **data):
        return cls(
            address=data.get("address"),
            blockHash=data.get("blockHash"),
            blockNumber=data.get("blockNumber"),
            blockchain=Blockchain(data.get("blockchain")),
            data=data.get("data"),
            logIndex=data.get("logIndex"),
            removed=data.get("removed"),
            topics=data.get("topics"),
            transactionHash=data.get("transactionHash"),
            transactionIndex=data.get("transactionIndex"),
            event=Event.from_dict(**data.get("event"))
            if data.get("event") is not None
            else None,
        )


class Transaction:
    def __init__(
        self,
        blockHash: str,
        blockNumber: str,
        from_: str,
        transactionIndex: str,
        value: str,
        gasPrice: str = None,
        gas: str = None,
        contractAddress: str = None,
        cumulativeGasUsed: str = None,
        input: str = None,
        v: str = None,
        r: str = None,
        s: str = None,
        method: Method = None,
        to: str = None,
        nonce: str = None,
        gasUsed: str = None,
        logs: List[Log] = None,
        hash: str = None,
        status: str = None,
        blockchain: str = None,
        timestamp: str = None,
        type: str = None,
    ):
        self.blockHash = blockHash
        self.blockNumber = blockNumber
        self.from_ = from_
        self.transactionIndex = transactionIndex
        self.value = value
        self.gasPrice = gasPrice
        self.gas = gas
        self.contractAddress = contractAddress
        self.cumulativeGasUsed = cumulativeGasUsed
        self.input = input
        self.v = v
        self.r = r
        self.s = s
        self.method = method
        self.to = to
        self.nonce = nonce
        self.gasUsed = gasUsed
        self.logs = logs
        self.hash = hash
        self.status = status
        self.blockchain = blockchain
        self.timestamp = timestamp
        self.type = type

    @classmethod
    def from_dict(cls, **data):
        return cls(
            blockHash=data.get("blockHash"),
            blockNumber=data.get("blockNumber"),
            from_=data.get("from"),
            transactionIndex=data.get("transactionIndex"),
            value=data.get("value"),
            gasPrice=data.get("gasPrice"),
            gas=data.get("gas"),
            contractAddress=data.get("contractAddress"),
            cumulativeGasUsed=data.get("cumulativeGasUsed"),
            input=data.get("input"),
            v=data.get("v"),
            r=data.get("r"),
            s=data.get("s"),
            method=Method.from_dict(**data.get("method"))
            if data.get("method") is not None
            else None,
            to=data.get("to"),
            nonce=data.get("nonce"),
            gasUsed=data.get("gasUsed"),
            logs=[Log.from_dict(**log_data) for log_data in data.get("logs", [])],
            hash=data.get("hash"),
            status=data.get("status"),
            blockchain=data.get("blockchain"),
            timestamp=data.get("timestamp"),
            type=data.get("type"),
        )


class Block:
    def __init__(
        self,
        difficulty: str,
        extraData: str,
        gasLimit: str,
        gasUsed: str,
        hash: str,
        logsBloom: str,
        miner: str,
        mixHash: str,
        nonce: str,
        number: str,
        parentHash: str,
        receiptsRoot: str,
        sha3Uncles: str,
        size: str,
        stateRoot: str,
        timestamp: str,
        totalDifficulty: str,
        transactions: List[Transaction],
        transactionsRoot: str,
        uncles: List[str],
        blockchain: str = None,
    ):
        self.difficulty = difficulty
        self.extraData = extraData
        self.gasLimit = gasLimit
        self.gasUsed = gasUsed
        self.hash = hash
        self.logsBloom = logsBloom
        self.miner = miner
        self.mixHash = mixHash
        self.nonce = nonce
        self.number = number
        self.parentHash = parentHash
        self.receiptsRoot = receiptsRoot
        self.sha3Uncles = sha3Uncles
        self.size = size
        self.stateRoot = stateRoot
        self.timestamp = timestamp
        self.totalDifficulty = totalDifficulty
        self.transactions = transactions
        self.transactionsRoot = transactionsRoot
        self.uncles = uncles
        self.blockchain = blockchain

    @classmethod
    def from_dict(cls, **data):
        return cls(
            difficulty=data.get("difficulty"),
            extraData=data.get("extraData"),
            gasLimit=data.get("gasLimit"),
            gasUsed=data.get("gasUsed"),
            hash=data.get("hash"),
            logsBloom=data.get("logsBloom"),
            miner=data.get("miner"),
            mixHash=data.get("mixHash"),
            nonce=data.get("nonce"),
            number=data.get("number"),
            parentHash=data.get("parentHash"),
            receiptsRoot=data.get("receiptsRoot"),
            sha3Uncles=data.get("sha3Uncles"),
            size=data.get("size"),
            stateRoot=data.get("stateRoot"),
            timestamp=data.get("timestamp"),
            totalDifficulty=data.get("totalDifficulty"),
            transactions=[
                Transaction.from_dict(**transaction_data)
                for transaction_data in data.get("transactions", [])
            ],
            transactionsRoot=data.get("transactionsRoot"),
            uncles=data.get("uncles"),
            blockchain=data.get("blockchain"),
        )


class GetBlocksReply:
    def __init__(self, blocks: List[Block], syncStatus: SyncStatus = None):
        self.blocks = blocks
        self.syncStatus = syncStatus

    @classmethod
    def from_dict(cls, **data):
        return cls(
            blocks=[
                Block.from_dict(**block_data) for block_data in data.get("blocks", [])
            ],
            syncStatus=SyncStatus.from_dict(**data.get("syncStatus"))
            if data.get("syncStatus") is not None
            else None,
        )


class GetBlocksRequest:
    def __init__(
        self,
        blockchain: Blockchain,
        fromBlock: float
        | Literal[Literal["latest"]]
        | Literal[Literal["earliest"]] = None,
        toBlock: float
        | Literal[Literal["latest"]]
        | Literal[Literal["earliest"]] = None,
        descOrder: bool = None,
        includeLogs: bool = None,
        includeTxs: bool = None,
        decodeLogs: bool = None,
        decodeTxData: bool = None,
        syncCheck: bool = None,
    ):
        self.blockchain = blockchain
        self.fromBlock = fromBlock
        self.toBlock = toBlock
        self.descOrder = descOrder
        self.includeLogs = includeLogs
        self.includeTxs = includeTxs
        self.decodeLogs = decodeLogs
        self.decodeTxData = decodeTxData
        self.syncCheck = syncCheck

    def to_dict(self):
        if isinstance(self.blockchain, str):
            blockchain_value = self.blockchain
        elif isinstance(self.blockchain, list):
            blockchain_value = [
                block.value if isinstance(block, Blockchain) else block
                for block in self.blockchain
            ]
        elif self.blockchain is not None:
            blockchain_value = self.blockchain.value
        else:
            blockchain_value = None
        return {
            "blockchain": blockchain_value,
            "fromBlock": self.fromBlock,
            "toBlock": self.toBlock,
            "descOrder": self.descOrder,
            "includeLogs": self.includeLogs,
            "includeTxs": self.includeTxs,
            "decodeLogs": self.decodeLogs,
            "decodeTxData": self.decodeTxData,
            "syncCheck": self.syncCheck,
        }


class GetTransactionsByHashReply:
    def __init__(self, transactions: List[Transaction], syncStatus: SyncStatus = None):
        self.transactions = transactions
        self.syncStatus = syncStatus

    @classmethod
    def from_dict(cls, **data):
        return cls(
            transactions=[
                Transaction.from_dict(**transaction_data)
                for transaction_data in data.get("transactions", [])
            ],
            syncStatus=SyncStatus.from_dict(**data.get("syncStatus"))
            if data.get("syncStatus") is not None
            else None,
        )


class GetTransactionsByHashRequest:
    def __init__(
        self,
        transactionHash: str,
        blockchain: Blockchain | List[Blockchain] = None,
        includeLogs: bool = None,
        decodeLogs: bool = None,
        decodeTxData: bool = None,
        syncCheck: bool = None,
    ):
        self.transactionHash = transactionHash
        self.blockchain = blockchain
        self.includeLogs = includeLogs
        self.decodeLogs = decodeLogs
        self.decodeTxData = decodeTxData
        self.syncCheck = syncCheck

    def to_dict(self):
        if isinstance(self.blockchain, str):
            blockchain_value = self.blockchain
        elif isinstance(self.blockchain, list):
            blockchain_value = [
                block.value if isinstance(block, Blockchain) else block
                for block in self.blockchain
            ]
        elif self.blockchain is not None:
            blockchain_value = self.blockchain.value
        else:
            blockchain_value = None
        return {
            "transactionHash": self.transactionHash,
            "blockchain": blockchain_value,
            "includeLogs": self.includeLogs,
            "decodeLogs": self.decodeLogs,
            "decodeTxData": self.decodeTxData,
            "syncCheck": self.syncCheck,
        }


class GetTransactionsByAddressReply:
    def __init__(
        self,
        nextPageToken: str,
        transactions: List[Transaction],
        syncStatus: SyncStatus = None,
    ):
        self.nextPageToken = nextPageToken
        self.transactions = transactions
        self.syncStatus = syncStatus

    @classmethod
    def from_dict(cls, **data):
        return cls(
            nextPageToken=data.get("nextPageToken"),
            transactions=[
                Transaction.from_dict(**transaction_data)
                for transaction_data in data.get("transactions", [])
            ],
            syncStatus=SyncStatus.from_dict(**data.get("syncStatus"))
            if data.get("syncStatus") is not None
            else None,
        )


class GetTransactionsByAddressRequest:
    def __init__(
        self,
        address: List[str],
        blockchain: Blockchain | List[Blockchain],
        fromBlock: float
        | Literal[Literal["latest"]]
        | Literal[Literal["earliest"]] = None,
        toBlock: float
        | Literal[Literal["latest"]]
        | Literal[Literal["earliest"]] = None,
        fromTimestamp: float
        | Literal[Literal["latest"]]
        | Literal[Literal["earliest"]] = None,
        toTimestamp: float
        | Literal[Literal["latest"]]
        | Literal[Literal["earliest"]] = None,
        pageToken: str = None,
        pageSize: float = None,
        descOrder: bool = None,
        includeLogs: bool = None,
        syncCheck: bool = None,
    ):
        self.address = address
        self.blockchain = blockchain
        self.fromBlock = fromBlock
        self.toBlock = toBlock
        self.fromTimestamp = fromTimestamp
        self.toTimestamp = toTimestamp
        self.pageToken = pageToken
        self.pageSize = pageSize
        self.descOrder = descOrder
        self.includeLogs = includeLogs
        self.syncCheck = syncCheck

    def to_dict(self):
        if isinstance(self.blockchain, str):
            blockchain_value = self.blockchain
        elif isinstance(self.blockchain, list):
            blockchain_value = [
                block.value if isinstance(block, Blockchain) else block
                for block in self.blockchain
            ]
        elif self.blockchain is not None:
            blockchain_value = self.blockchain.value
        else:
            blockchain_value = None
        return {
            "address": self.address,
            "blockchain": blockchain_value,
            "fromBlock": self.fromBlock,
            "toBlock": self.toBlock,
            "fromTimestamp": self.fromTimestamp,
            "toTimestamp": self.toTimestamp,
            "pageToken": self.pageToken,
            "pageSize": self.pageSize,
            "descOrder": self.descOrder,
            "includeLogs": self.includeLogs,
            "syncCheck": self.syncCheck,
        }


class GetLogsReply:
    def __init__(
        self, logs: List[Log], nextPageToken: str = None, syncStatus: SyncStatus = None
    ):
        self.logs = logs
        self.nextPageToken = nextPageToken
        self.syncStatus = syncStatus

    @classmethod
    def from_dict(cls, **data):
        return cls(
            logs=[Log.from_dict(**log_data) for log_data in data.get("logs", [])],
            nextPageToken=data.get("nextPageToken"),
            syncStatus=SyncStatus.from_dict(**data.get("syncStatus"))
            if data.get("syncStatus") is not None
            else None,
        )


class GetLogsRequest:
    def __init__(
        self,
        blockchain: Blockchain | List[Blockchain],
        fromBlock: float
        | Literal[Literal["latest"]]
        | Literal[Literal["earliest"]] = None,
        toBlock: float
        | Literal[Literal["latest"]]
        | Literal[Literal["earliest"]] = None,
        fromTimestamp: float
        | Literal[Literal["latest"]]
        | Literal[Literal["earliest"]] = None,
        toTimestamp: float
        | Literal[Literal["latest"]]
        | Literal[Literal["earliest"]] = None,
        address: List[str] = None,
        topics: List[str | List[str]] = None,
        pageToken: str = None,
        pageSize: float = None,
        descOrder: bool = None,
        decodeLogs: bool = None,
        syncCheck: bool = None,
    ):
        self.blockchain = blockchain
        self.fromBlock = fromBlock
        self.toBlock = toBlock
        self.fromTimestamp = fromTimestamp
        self.toTimestamp = toTimestamp
        self.address = address
        self.topics = topics
        self.pageToken = pageToken
        self.pageSize = pageSize
        self.descOrder = descOrder
        self.decodeLogs = decodeLogs
        self.syncCheck = syncCheck

    def to_dict(self):
        if isinstance(self.blockchain, str):
            blockchain_value = self.blockchain
        elif isinstance(self.blockchain, list):
            blockchain_value = [
                block.value if isinstance(block, Blockchain) else block
                for block in self.blockchain
            ]
        elif self.blockchain is not None:
            blockchain_value = self.blockchain.value
        else:
            blockchain_value = None
        return {
            "blockchain": blockchain_value,
            "fromBlock": self.fromBlock,
            "toBlock": self.toBlock,
            "fromTimestamp": self.fromTimestamp,
            "toTimestamp": self.toTimestamp,
            "address": self.address,
            "topics": self.topics,
            "pageToken": self.pageToken,
            "pageSize": self.pageSize,
            "descOrder": self.descOrder,
            "decodeLogs": self.decodeLogs,
            "syncCheck": self.syncCheck,
        }


class BlockchainStats:
    def __init__(
        self,
        blockTimeMs: float,
        blockchain: str,
        latestBlockNumber: float,
        nativeCoinUsdPrice: str,
        totalEventsCount: float,
        totalTransactionsCount: float,
    ):
        self.blockTimeMs = blockTimeMs
        self.blockchain = blockchain
        self.latestBlockNumber = latestBlockNumber
        self.nativeCoinUsdPrice = nativeCoinUsdPrice
        self.totalEventsCount = totalEventsCount
        self.totalTransactionsCount = totalTransactionsCount

    @classmethod
    def from_dict(cls, **data):
        return cls(
            blockTimeMs=data.get("blockTimeMs"),
            blockchain=data.get("blockchain"),
            latestBlockNumber=data.get("latestBlockNumber"),
            nativeCoinUsdPrice=data.get("nativeCoinUsdPrice"),
            totalEventsCount=data.get("totalEventsCount"),
            totalTransactionsCount=data.get("totalTransactionsCount"),
        )


class GetBlockchainStatsReply:
    def __init__(self, stats: List[BlockchainStats], syncStatus: SyncStatus = None):
        self.stats = stats
        self.syncStatus = syncStatus

    @classmethod
    def from_dict(cls, **data):
        return cls(
            stats=[
                BlockchainStats.from_dict(**blockchainstats_data)
                for blockchainstats_data in data.get("stats", [])
            ],
            syncStatus=SyncStatus.from_dict(**data.get("syncStatus"))
            if data.get("syncStatus") is not None
            else None,
        )


class GetBlockchainStatsRequest:
    def __init__(
        self, blockchain: Blockchain | List[Blockchain] = None, syncCheck: bool = None
    ):
        self.blockchain = blockchain
        self.syncCheck = syncCheck

    def to_dict(self):
        if isinstance(self.blockchain, str):
            blockchain_value = self.blockchain
        elif isinstance(self.blockchain, list):
            blockchain_value = [
                block.value if isinstance(block, Blockchain) else block
                for block in self.blockchain
            ]
        elif self.blockchain is not None:
            blockchain_value = self.blockchain.value
        else:
            blockchain_value = None
        return {
            "blockchain": blockchain_value,
            "syncCheck": self.syncCheck,
        }


class GetInteractionsReply:
    def __init__(self, blockchains: List[str], syncStatus: SyncStatus = None):
        self.blockchains = blockchains
        self.syncStatus = syncStatus

    @classmethod
    def from_dict(cls, **data):
        return cls(
            blockchains=data.get("blockchains"),
            syncStatus=SyncStatus.from_dict(**data.get("syncStatus"))
            if data.get("syncStatus") is not None
            else None,
        )


class GetInteractionsRequest:
    def __init__(self, address: str, syncCheck: bool = None):
        self.address = address
        self.syncCheck = syncCheck

    def to_dict(self):
        return {
            "address": self.address,
            "syncCheck": self.syncCheck,
        }


class Balance:
    def __init__(
        self,
        balance: str,
        balanceRawInteger: str,
        balanceUsd: str,
        blockchain: Blockchain,
        holderAddress: str,
        thumbnail: str,
        tokenDecimals: float,
        tokenName: str,
        tokenPrice: str,
        tokenSymbol: str,
        tokenType: str,
        contractAddress: str = None,
    ):
        self.balance = balance
        self.balanceRawInteger = balanceRawInteger
        self.balanceUsd = balanceUsd
        self.blockchain = blockchain
        self.holderAddress = holderAddress
        self.thumbnail = thumbnail
        self.tokenDecimals = tokenDecimals
        self.tokenName = tokenName
        self.tokenPrice = tokenPrice
        self.tokenSymbol = tokenSymbol
        self.tokenType = tokenType
        self.contractAddress = contractAddress

    @classmethod
    def from_dict(cls, **data):
        return cls(
            balance=data.get("balance"),
            balanceRawInteger=data.get("balanceRawInteger"),
            balanceUsd=data.get("balanceUsd"),
            blockchain=Blockchain(data.get("blockchain")),
            holderAddress=data.get("holderAddress"),
            thumbnail=data.get("thumbnail"),
            tokenDecimals=data.get("tokenDecimals"),
            tokenName=data.get("tokenName"),
            tokenPrice=data.get("tokenPrice"),
            tokenSymbol=data.get("tokenSymbol"),
            tokenType=data.get("tokenType"),
            contractAddress=data.get("contractAddress"),
        )


class GetAccountBalanceReply:
    def __init__(
        self,
        assets: List[Balance],
        totalBalanceUsd: str,
        totalCount: float,
        nextPageToken: str = None,
        syncStatus: SyncStatus = None,
    ):
        self.assets = assets
        self.totalBalanceUsd = totalBalanceUsd
        self.totalCount = totalCount
        self.nextPageToken = nextPageToken
        self.syncStatus = syncStatus

    @classmethod
    def from_dict(cls, **data):
        return cls(
            assets=[
                Balance.from_dict(**balance_data)
                for balance_data in data.get("assets", [])
            ],
            totalBalanceUsd=data.get("totalBalanceUsd"),
            totalCount=data.get("totalCount"),
            nextPageToken=data.get("nextPageToken"),
            syncStatus=SyncStatus.from_dict(**data.get("syncStatus"))
            if data.get("syncStatus") is not None
            else None,
        )


class GetAccountBalanceRequest:
    def __init__(
        self,
        walletAddress: str,
        blockchain: Blockchain | List[Blockchain] = None,
        onlyWhitelisted: bool = None,
        nativeFirst: bool = None,
        pageToken: str = None,
        pageSize: float = None,
        syncCheck: bool = None,
    ):
        self.walletAddress = walletAddress
        self.blockchain = blockchain
        self.onlyWhitelisted = onlyWhitelisted
        self.nativeFirst = nativeFirst
        self.pageToken = pageToken
        self.pageSize = pageSize
        self.syncCheck = syncCheck

    def to_dict(self):
        if isinstance(self.blockchain, str):
            blockchain_value = self.blockchain
        elif isinstance(self.blockchain, list):
            blockchain_value = [
                block.value if isinstance(block, Blockchain) else block
                for block in self.blockchain
            ]
        elif self.blockchain is not None:
            blockchain_value = self.blockchain.value
        else:
            blockchain_value = None
        return {
            "walletAddress": self.walletAddress,
            "blockchain": blockchain_value,
            "onlyWhitelisted": self.onlyWhitelisted,
            "nativeFirst": self.nativeFirst,
            "pageToken": self.pageToken,
            "pageSize": self.pageSize,
            "syncCheck": self.syncCheck,
        }


class GetTokenPriceReply:
    def __init__(
        self,
        blockchain: Blockchain,
        usdPrice: str,
        contractAddress: str = None,
        syncStatus: SyncStatus = None,
    ):
        self.blockchain = blockchain
        self.usdPrice = usdPrice
        self.contractAddress = contractAddress
        self.syncStatus = syncStatus

    @classmethod
    def from_dict(cls, **data):
        return cls(
            blockchain=Blockchain(data.get("blockchain")),
            usdPrice=data.get("usdPrice"),
            contractAddress=data.get("contractAddress"),
            syncStatus=SyncStatus.from_dict(**data.get("syncStatus"))
            if data.get("syncStatus") is not None
            else None,
        )


class GetTokenPriceRequest:
    def __init__(
        self,
        blockchain: Blockchain,
        contractAddress: str = None,
        syncCheck: bool = None,
    ):
        self.blockchain = blockchain
        self.contractAddress = contractAddress
        self.syncCheck = syncCheck

    def to_dict(self):
        if isinstance(self.blockchain, str):
            blockchain_value = self.blockchain
        elif isinstance(self.blockchain, list):
            blockchain_value = [
                block.value if isinstance(block, Blockchain) else block
                for block in self.blockchain
            ]
        elif self.blockchain is not None:
            blockchain_value = self.blockchain.value
        else:
            blockchain_value = None
        return {
            "blockchain": blockchain_value,
            "contractAddress": self.contractAddress,
            "syncCheck": self.syncCheck,
        }


class HolderBalance:
    def __init__(self, balance: str, balanceRawInteger: str, holderAddress: str):
        self.balance = balance
        self.balanceRawInteger = balanceRawInteger
        self.holderAddress = holderAddress

    @classmethod
    def from_dict(cls, **data):
        return cls(
            balance=data.get("balance"),
            balanceRawInteger=data.get("balanceRawInteger"),
            holderAddress=data.get("holderAddress"),
        )


class GetTokenHoldersReply:
    def __init__(
        self,
        blockchain: Blockchain,
        contractAddress: str,
        holders: List[HolderBalance],
        holdersCount: float,
        nextPageToken: str,
        tokenDecimals: float,
        syncStatus: SyncStatus = None,
    ):
        self.blockchain = blockchain
        self.contractAddress = contractAddress
        self.holders = holders
        self.holdersCount = holdersCount
        self.nextPageToken = nextPageToken
        self.tokenDecimals = tokenDecimals
        self.syncStatus = syncStatus

    @classmethod
    def from_dict(cls, **data):
        return cls(
            blockchain=Blockchain(data.get("blockchain")),
            contractAddress=data.get("contractAddress"),
            holders=[
                HolderBalance.from_dict(**holderbalance_data)
                for holderbalance_data in data.get("holders", [])
            ],
            holdersCount=data.get("holdersCount"),
            nextPageToken=data.get("nextPageToken"),
            tokenDecimals=data.get("tokenDecimals"),
            syncStatus=SyncStatus.from_dict(**data.get("syncStatus"))
            if data.get("syncStatus") is not None
            else None,
        )


class GetTokenHoldersRequest:
    def __init__(
        self,
        blockchain: Blockchain,
        contractAddress: str,
        pageToken: str = None,
        pageSize: float = None,
        syncCheck: bool = None,
    ):
        self.blockchain = blockchain
        self.contractAddress = contractAddress
        self.pageToken = pageToken
        self.pageSize = pageSize
        self.syncCheck = syncCheck

    def to_dict(self):
        if isinstance(self.blockchain, str):
            blockchain_value = self.blockchain
        elif isinstance(self.blockchain, list):
            blockchain_value = [
                block.value if isinstance(block, Blockchain) else block
                for block in self.blockchain
            ]
        elif self.blockchain is not None:
            blockchain_value = self.blockchain.value
        else:
            blockchain_value = None
        return {
            "blockchain": blockchain_value,
            "contractAddress": self.contractAddress,
            "pageToken": self.pageToken,
            "pageSize": self.pageSize,
            "syncCheck": self.syncCheck,
        }


class DailyHolderCount:
    def __init__(
        self,
        holderCount: float,
        lastUpdatedAt: str,
        totalAmount: str,
        totalAmountRawInteger: str,
    ):
        self.holderCount = holderCount
        self.lastUpdatedAt = lastUpdatedAt
        self.totalAmount = totalAmount
        self.totalAmountRawInteger = totalAmountRawInteger

    @classmethod
    def from_dict(cls, **data):
        return cls(
            holderCount=data.get("holderCount"),
            lastUpdatedAt=data.get("lastUpdatedAt"),
            totalAmount=data.get("totalAmount"),
            totalAmountRawInteger=data.get("totalAmountRawInteger"),
        )


class GetTokenHoldersCountReply:
    def __init__(
        self,
        blockchain: Blockchain,
        contractAddress: str,
        holderCountHistory: List[DailyHolderCount],
        latestHoldersCount: float,
        nextPageToken: str,
        tokenDecimals: float,
        syncStatus: SyncStatus = None,
    ):
        self.blockchain = blockchain
        self.contractAddress = contractAddress
        self.holderCountHistory = holderCountHistory
        self.latestHoldersCount = latestHoldersCount
        self.nextPageToken = nextPageToken
        self.tokenDecimals = tokenDecimals
        self.syncStatus = syncStatus

    @classmethod
    def from_dict(cls, **data):
        return cls(
            blockchain=Blockchain(data.get("blockchain")),
            contractAddress=data.get("contractAddress"),
            holderCountHistory=[
                DailyHolderCount.from_dict(**dailyholdercount_data)
                for dailyholdercount_data in data.get("holderCountHistory", [])
            ],
            latestHoldersCount=data.get("latestHoldersCount"),
            nextPageToken=data.get("nextPageToken"),
            tokenDecimals=data.get("tokenDecimals"),
            syncStatus=SyncStatus.from_dict(**data.get("syncStatus"))
            if data.get("syncStatus") is not None
            else None,
        )


class GetTokenHoldersCountRequest:
    def __init__(
        self,
        blockchain: Blockchain,
        contractAddress: str,
        pageToken: str = None,
        pageSize: float = None,
        syncCheck: bool = None,
    ):
        self.blockchain = blockchain
        self.contractAddress = contractAddress
        self.pageToken = pageToken
        self.pageSize = pageSize
        self.syncCheck = syncCheck

    def to_dict(self):
        if isinstance(self.blockchain, str):
            blockchain_value = self.blockchain
        elif isinstance(self.blockchain, list):
            blockchain_value = [
                block.value if isinstance(block, Blockchain) else block
                for block in self.blockchain
            ]
        elif self.blockchain is not None:
            blockchain_value = self.blockchain.value
        else:
            blockchain_value = None
        return {
            "blockchain": blockchain_value,
            "contractAddress": self.contractAddress,
            "pageToken": self.pageToken,
            "pageSize": self.pageSize,
            "syncCheck": self.syncCheck,
        }


class CurrencyDetailsExtended:
    def __init__(
        self,
        blockchain: Blockchain,
        decimals: float,
        name: str,
        symbol: str,
        thumbnail: str,
        address: str = None,
    ):
        self.blockchain = blockchain
        self.decimals = decimals
        self.name = name
        self.symbol = symbol
        self.thumbnail = thumbnail
        self.address = address

    @classmethod
    def from_dict(cls, **data):
        return cls(
            blockchain=Blockchain(data.get("blockchain")),
            decimals=data.get("decimals"),
            name=data.get("name"),
            symbol=data.get("symbol"),
            thumbnail=data.get("thumbnail"),
            address=data.get("address"),
        )


class GetCurrenciesReply:
    def __init__(
        self, currencies: List[CurrencyDetailsExtended], syncStatus: SyncStatus = None
    ):
        self.currencies = currencies
        self.syncStatus = syncStatus

    @classmethod
    def from_dict(cls, **data):
        return cls(
            currencies=[
                CurrencyDetailsExtended.from_dict(**currencydetailsextended_data)
                for currencydetailsextended_data in data.get("currencies", [])
            ],
            syncStatus=SyncStatus.from_dict(**data.get("syncStatus"))
            if data.get("syncStatus") is not None
            else None,
        )


class GetCurrenciesRequest:
    def __init__(self, blockchain: Blockchain, syncCheck: bool = None):
        self.blockchain = blockchain
        self.syncCheck = syncCheck

    def to_dict(self):
        if isinstance(self.blockchain, str):
            blockchain_value = self.blockchain
        elif isinstance(self.blockchain, list):
            blockchain_value = [
                block.value if isinstance(block, Blockchain) else block
                for block in self.blockchain
            ]
        elif self.blockchain is not None:
            blockchain_value = self.blockchain.value
        else:
            blockchain_value = None
        return {
            "blockchain": blockchain_value,
            "syncCheck": self.syncCheck,
        }


class TokenTransfer:
    def __init__(
        self,
        blockHeight: float,
        blockchain: str,
        thumbnail: str,
        timestamp: float,
        tokenDecimals: float,
        tokenName: str,
        tokenSymbol: str,
        transactionHash: str,
        value: str,
        valueRawInteger: str,
        fromAddress: str = None,
        contractAddress: str = None,
        toAddress: str = None,
        direction: str = None,
    ):
        self.blockHeight = blockHeight
        self.blockchain = blockchain
        self.thumbnail = thumbnail
        self.timestamp = timestamp
        self.tokenDecimals = tokenDecimals
        self.tokenName = tokenName
        self.tokenSymbol = tokenSymbol
        self.transactionHash = transactionHash
        self.value = value
        self.valueRawInteger = valueRawInteger
        self.fromAddress = fromAddress
        self.contractAddress = contractAddress
        self.toAddress = toAddress
        self.direction = direction

    @classmethod
    def from_dict(cls, **data):
        return cls(
            blockHeight=data.get("blockHeight"),
            blockchain=data.get("blockchain"),
            thumbnail=data.get("thumbnail"),
            timestamp=data.get("timestamp"),
            tokenDecimals=data.get("tokenDecimals"),
            tokenName=data.get("tokenName"),
            tokenSymbol=data.get("tokenSymbol"),
            transactionHash=data.get("transactionHash"),
            value=data.get("value"),
            valueRawInteger=data.get("valueRawInteger"),
            fromAddress=data.get("fromAddress"),
            contractAddress=data.get("contractAddress"),
            toAddress=data.get("toAddress"),
            direction=data.get("direction"),
        )


class GetTokenTransfersReply:
    def __init__(
        self,
        transfers: List[TokenTransfer],
        nextPageToken: str = None,
        syncStatus: SyncStatus = None,
    ):
        self.transfers = transfers
        self.nextPageToken = nextPageToken
        self.syncStatus = syncStatus

    @classmethod
    def from_dict(cls, **data):
        return cls(
            transfers=[
                TokenTransfer.from_dict(**tokentransfer_data)
                for tokentransfer_data in data.get("transfers", [])
            ],
            nextPageToken=data.get("nextPageToken"),
            syncStatus=SyncStatus.from_dict(**data.get("syncStatus"))
            if data.get("syncStatus") is not None
            else None,
        )


class GetTransfersRequest:
    def __init__(
        self,
        blockchain: Blockchain | List[Blockchain],
        fromBlock: float
        | Literal[Literal["latest"]]
        | Literal[Literal["earliest"]] = None,
        toBlock: float
        | Literal[Literal["latest"]]
        | Literal[Literal["earliest"]] = None,
        fromTimestamp: float
        | Literal[Literal["latest"]]
        | Literal[Literal["earliest"]] = None,
        toTimestamp: float
        | Literal[Literal["latest"]]
        | Literal[Literal["earliest"]] = None,
        address: List[str] = None,
        pageToken: str = None,
        pageSize: float = None,
        descOrder: bool = None,
        syncCheck: bool = None,
    ):
        self.blockchain = blockchain
        self.fromBlock = fromBlock
        self.toBlock = toBlock
        self.fromTimestamp = fromTimestamp
        self.toTimestamp = toTimestamp
        self.address = address
        self.pageToken = pageToken
        self.pageSize = pageSize
        self.descOrder = descOrder
        self.syncCheck = syncCheck

    def to_dict(self):
        if isinstance(self.blockchain, str):
            blockchain_value = self.blockchain
        elif isinstance(self.blockchain, list):
            blockchain_value = [
                block.value if isinstance(block, Blockchain) else block
                for block in self.blockchain
            ]
        elif self.blockchain is not None:
            blockchain_value = self.blockchain.value
        else:
            blockchain_value = None
        return {
            "blockchain": blockchain_value,
            "fromBlock": self.fromBlock,
            "toBlock": self.toBlock,
            "fromTimestamp": self.fromTimestamp,
            "toTimestamp": self.toTimestamp,
            "address": self.address,
            "pageToken": self.pageToken,
            "pageSize": self.pageSize,
            "descOrder": self.descOrder,
            "syncCheck": self.syncCheck,
        }


class Trait:
    def __init__(self, trait_type: str, value: str):
        self.trait_type = trait_type
        self.value = value

    @classmethod
    def from_dict(cls, **data):
        return cls(
            trait_type=data.get("trait_type"),
            value=data.get("value"),
        )


class Nft:
    def __init__(
        self,
        blockchain: Blockchain,
        collectionName: str,
        contractAddress: str,
        contractType: Literal[
            Literal["ERC721"], Literal["ERC1155"], Literal["UNDEFINED"]
        ],
        imageUrl: str,
        name: str,
        symbol: str,
        tokenId: str,
        tokenUrl: str,
        quantity: str = None,
        traits: List[Trait] = None,
    ):
        self.blockchain = blockchain
        self.collectionName = collectionName
        self.contractAddress = contractAddress
        self.contractType = contractType
        self.imageUrl = imageUrl
        self.name = name
        self.symbol = symbol
        self.tokenId = tokenId
        self.tokenUrl = tokenUrl
        self.quantity = quantity
        self.traits = traits

    @classmethod
    def from_dict(cls, **data):
        return cls(
            blockchain=Blockchain(data.get("blockchain")),
            collectionName=data.get("collectionName"),
            contractAddress=data.get("contractAddress"),
            contractType=data.get("contractType"),
            imageUrl=data.get("imageUrl"),
            name=data.get("name"),
            symbol=data.get("symbol"),
            tokenId=data.get("tokenId"),
            tokenUrl=data.get("tokenUrl"),
            quantity=data.get("quantity"),
            traits=[
                Trait.from_dict(**trait_data) for trait_data in data.get("traits", [])
            ],
        )


class GetNFTsByOwnerReply:
    def __init__(
        self,
        assets: List[Nft],
        nextPageToken: str,
        owner: str,
        syncStatus: SyncStatus = None,
    ):
        self.assets = assets
        self.nextPageToken = nextPageToken
        self.owner = owner
        self.syncStatus = syncStatus

    @classmethod
    def from_dict(cls, **data):
        return cls(
            assets=[Nft.from_dict(**nft_data) for nft_data in data.get("assets", [])],
            nextPageToken=data.get("nextPageToken"),
            owner=data.get("owner"),
            syncStatus=SyncStatus.from_dict(**data.get("syncStatus"))
            if data.get("syncStatus") is not None
            else None,
        )


class GetNFTsByOwnerRequest:
    def __init__(
        self,
        walletAddress: str,
        blockchain: Blockchain | List[Blockchain] = None,
        filter: List[Dict[str, List[str]]] = None,
        pageToken: str = None,
        pageSize: float = None,
        syncCheck: bool = None,
    ):
        self.walletAddress = walletAddress
        self.blockchain = blockchain
        self.filter = filter
        self.pageToken = pageToken
        self.pageSize = pageSize
        self.syncCheck = syncCheck

    def to_dict(self):
        if isinstance(self.blockchain, str):
            blockchain_value = self.blockchain
        elif isinstance(self.blockchain, list):
            blockchain_value = [
                block.value if isinstance(block, Blockchain) else block
                for block in self.blockchain
            ]
        elif self.blockchain is not None:
            blockchain_value = self.blockchain.value
        else:
            blockchain_value = None
        return {
            "walletAddress": self.walletAddress,
            "blockchain": blockchain_value,
            "filter": self.filter,
            "pageToken": self.pageToken,
            "pageSize": self.pageSize,
            "syncCheck": self.syncCheck,
        }


class NftAttributes:
    def __init__(
        self,
        contractType: Literal[
            Literal["ERC721"], Literal["ERC1155"], Literal["UNDEFINED"]
        ],
        description: str,
        imageUrl: str,
        name: str,
        tokenUrl: str,
        traits: List[Trait] = None,
    ):
        self.contractType = contractType
        self.description = description
        self.imageUrl = imageUrl
        self.name = name
        self.tokenUrl = tokenUrl
        self.traits = traits

    @classmethod
    def from_dict(cls, **data):
        return cls(
            contractType=data.get("contractType"),
            description=data.get("description"),
            imageUrl=data.get("imageUrl"),
            name=data.get("name"),
            tokenUrl=data.get("tokenUrl"),
            traits=[
                Trait.from_dict(**trait_data) for trait_data in data.get("traits", [])
            ],
        )


class NftMetadata:
    def __init__(
        self,
        blockchain: Blockchain,
        collectionName: str,
        collectionSymbol: str,
        contractAddress: str,
        contractType: Literal[
            Literal["ERC721"], Literal["ERC1155"], Literal["UNDEFINED"]
        ],
        tokenId: str,
    ):
        self.blockchain = blockchain
        self.collectionName = collectionName
        self.collectionSymbol = collectionSymbol
        self.contractAddress = contractAddress
        self.contractType = contractType
        self.tokenId = tokenId

    @classmethod
    def from_dict(cls, **data):
        return cls(
            blockchain=Blockchain(data.get("blockchain")),
            collectionName=data.get("collectionName"),
            collectionSymbol=data.get("collectionSymbol"),
            contractAddress=data.get("contractAddress"),
            contractType=data.get("contractType"),
            tokenId=data.get("tokenId"),
        )


class GetNFTMetadataReply:
    def __init__(
        self,
        metadata: NftMetadata = None,
        attributes: NftAttributes = None,
        syncStatus: SyncStatus = None,
    ):
        self.metadata = metadata
        self.attributes = attributes
        self.syncStatus = syncStatus

    @classmethod
    def from_dict(cls, **data):
        return cls(
            metadata=NftMetadata.from_dict(**data.get("metadata"))
            if data.get("metadata") is not None
            else None,
            attributes=NftAttributes.from_dict(**data.get("attributes"))
            if data.get("attributes") is not None
            else None,
            syncStatus=SyncStatus.from_dict(**data.get("syncStatus"))
            if data.get("syncStatus") is not None
            else None,
        )


class GetNFTMetadataRequest:
    def __init__(
        self,
        blockchain: Blockchain,
        contractAddress: str,
        forceFetch: bool,
        tokenId: str,
        syncCheck: bool = None,
    ):
        self.blockchain = blockchain
        self.contractAddress = contractAddress
        self.forceFetch = forceFetch
        self.tokenId = tokenId
        self.syncCheck = syncCheck

    def to_dict(self):
        if isinstance(self.blockchain, str):
            blockchain_value = self.blockchain
        elif isinstance(self.blockchain, list):
            blockchain_value = [
                block.value if isinstance(block, Blockchain) else block
                for block in self.blockchain
            ]
        elif self.blockchain is not None:
            blockchain_value = self.blockchain.value
        else:
            blockchain_value = None
        return {
            "blockchain": blockchain_value,
            "contractAddress": self.contractAddress,
            "forceFetch": self.forceFetch,
            "tokenId": self.tokenId,
            "syncCheck": self.syncCheck,
        }


class GetNFTHoldersReply:
    def __init__(
        self, holders: List[str], nextPageToken: str, syncStatus: SyncStatus = None
    ):
        self.holders = holders
        self.nextPageToken = nextPageToken
        self.syncStatus = syncStatus

    @classmethod
    def from_dict(cls, **data):
        return cls(
            holders=data.get("holders"),
            nextPageToken=data.get("nextPageToken"),
            syncStatus=SyncStatus.from_dict(**data.get("syncStatus"))
            if data.get("syncStatus") is not None
            else None,
        )


class GetNFTHoldersRequest:
    def __init__(
        self,
        blockchain: Blockchain,
        contractAddress: str,
        pageToken: str = None,
        pageSize: float = None,
        syncCheck: bool = None,
    ):
        self.blockchain = blockchain
        self.contractAddress = contractAddress
        self.pageToken = pageToken
        self.pageSize = pageSize
        self.syncCheck = syncCheck

    def to_dict(self):
        if isinstance(self.blockchain, str):
            blockchain_value = self.blockchain
        elif isinstance(self.blockchain, list):
            blockchain_value = [
                block.value if isinstance(block, Blockchain) else block
                for block in self.blockchain
            ]
        elif self.blockchain is not None:
            blockchain_value = self.blockchain.value
        else:
            blockchain_value = None
        return {
            "blockchain": blockchain_value,
            "contractAddress": self.contractAddress,
            "pageToken": self.pageToken,
            "pageSize": self.pageSize,
            "syncCheck": self.syncCheck,
        }


class NftTransfer:
    def __init__(
        self,
        blockHeight: float,
        blockchain: Blockchain,
        collectionName: str,
        collectionSymbol: str,
        fromAddress: str,
        imageUrl: str,
        name: str,
        timestamp: float,
        toAddress: str,
        transactionHash: str,
        type: Literal[Literal["ERC721"], Literal["ERC1155"], Literal["UNDEFINED"]],
        value: str,
        tokenId: str = None,
        contractAddress: str = None,
    ):
        self.blockHeight = blockHeight
        self.blockchain = blockchain
        self.collectionName = collectionName
        self.collectionSymbol = collectionSymbol
        self.fromAddress = fromAddress
        self.imageUrl = imageUrl
        self.name = name
        self.timestamp = timestamp
        self.toAddress = toAddress
        self.transactionHash = transactionHash
        self.type = type
        self.value = value
        self.tokenId = tokenId
        self.contractAddress = contractAddress

    @classmethod
    def from_dict(cls, **data):
        return cls(
            blockHeight=data.get("blockHeight"),
            blockchain=Blockchain(data.get("blockchain")),
            collectionName=data.get("collectionName"),
            collectionSymbol=data.get("collectionSymbol"),
            fromAddress=data.get("fromAddress"),
            imageUrl=data.get("imageUrl"),
            name=data.get("name"),
            timestamp=data.get("timestamp"),
            toAddress=data.get("toAddress"),
            transactionHash=data.get("transactionHash"),
            type=data.get("type"),
            value=data.get("value"),
            tokenId=data.get("tokenId"),
            contractAddress=data.get("contractAddress"),
        )


class GetNftTransfersReply:
    def __init__(
        self,
        transfers: List[NftTransfer],
        nextPageToken: str = None,
        syncStatus: SyncStatus = None,
    ):
        self.transfers = transfers
        self.nextPageToken = nextPageToken
        self.syncStatus = syncStatus

    @classmethod
    def from_dict(cls, **data):
        return cls(
            transfers=[
                NftTransfer.from_dict(**nfttransfer_data)
                for nfttransfer_data in data.get("transfers", [])
            ],
            nextPageToken=data.get("nextPageToken"),
            syncStatus=SyncStatus.from_dict(**data.get("syncStatus"))
            if data.get("syncStatus") is not None
            else None,
        )


class GetTokenAllowancesRequest:
    def __init__(
        self,
        blockchain: Blockchain | List[Blockchain],
        walletAddress: str,
        spenderAddress: str = None,
        contractAddress: str = None,
    ):
        self.blockchain = blockchain
        self.walletAddress = walletAddress
        self.spenderAddress = spenderAddress
        self.contractAddress = contractAddress

    def to_dict(self):
        if isinstance(self.blockchain, str):
            blockchain_value = self.blockchain
        elif isinstance(self.blockchain, list):
            blockchain_value = [
                block.value if isinstance(block, Blockchain) else block
                for block in self.blockchain
            ]
        elif self.blockchain is not None:
            blockchain_value = self.blockchain.value
        else:
            blockchain_value = None
        return {
            "blockchain": blockchain_value,
            "walletAddress": self.walletAddress,
            "spenderAddress": self.spenderAddress,
            "contractAddress": self.contractAddress,
        }


class ERC20TokenAllowance:
    def __init__(
        self,
        blockHeight: float,
        thumbnail: str,
        timestamp: float,
        value: str = None,
        tokenDecimals: float = None,
        walletAddress: str = None,
        contractAddress: str = None,
        transactionHash: str = None,
        blockchain: str = None,
        tokenName: str = None,
        tokenSymbol: str = None,
        spenderAddress: str = None,
        rawLog: Log = None,
    ):
        self.blockHeight = blockHeight
        self.thumbnail = thumbnail
        self.timestamp = timestamp
        self.value = value
        self.tokenDecimals = tokenDecimals
        self.walletAddress = walletAddress
        self.contractAddress = contractAddress
        self.transactionHash = transactionHash
        self.blockchain = blockchain
        self.tokenName = tokenName
        self.tokenSymbol = tokenSymbol
        self.spenderAddress = spenderAddress
        self.rawLog = rawLog

    @classmethod
    def from_dict(cls, **data):
        return cls(
            blockHeight=data.get("blockHeight"),
            thumbnail=data.get("thumbnail"),
            timestamp=data.get("timestamp"),
            value=data.get("value"),
            tokenDecimals=data.get("tokenDecimals"),
            walletAddress=data.get("walletAddress"),
            contractAddress=data.get("contractAddress"),
            transactionHash=data.get("transactionHash"),
            blockchain=data.get("blockchain"),
            tokenName=data.get("tokenName"),
            tokenSymbol=data.get("tokenSymbol"),
            spenderAddress=data.get("spenderAddress"),
            rawLog=Log.from_dict(**data.get("rawLog"))
            if data.get("rawLog") is not None
            else None,
        )


class GetTokenAllowancesReply:
    def __init__(self, allowances: List[ERC20TokenAllowance]):
        self.allowances = allowances

    @classmethod
    def from_dict(cls, **data):
        return cls(
            allowances=[
                ERC20TokenAllowance.from_dict(**erc20tokenallowance_data)
                for erc20tokenallowance_data in data.get("allowances", [])
            ],
        )


class GetTokenPriceHistoryRequest:
    def __init__(
        self,
        blockchain: Blockchain,
        contractAddress: str,
        fromTimestamp: float
        | Literal[Literal["latest"]]
        | Literal[Literal["earliest"]] = None,
        toTimestamp: float
        | Literal[Literal["latest"]]
        | Literal[Literal["earliest"]] = None,
        interval: float = None,
        limit: float = None,
        syncCheck: bool = None,
    ):
        self.blockchain = blockchain
        self.contractAddress = contractAddress
        self.fromTimestamp = fromTimestamp
        self.toTimestamp = toTimestamp
        self.interval = interval
        self.limit = limit
        self.syncCheck = syncCheck

    def to_dict(self):
        if isinstance(self.blockchain, str):
            blockchain_value = self.blockchain
        elif isinstance(self.blockchain, list):
            blockchain_value = [
                block.value if isinstance(block, Blockchain) else block
                for block in self.blockchain
            ]
        elif self.blockchain is not None:
            blockchain_value = self.blockchain.value
        else:
            blockchain_value = None
        return {
            "blockchain": blockchain_value,
            "contractAddress": self.contractAddress,
            "fromTimestamp": self.fromTimestamp,
            "toTimestamp": self.toTimestamp,
            "interval": self.interval,
            "limit": self.limit,
            "syncCheck": self.syncCheck,
        }


class Quote:
    def __init__(self, blockHeight: float, timestamp: float, usdPrice: str):
        self.blockHeight = blockHeight
        self.timestamp = timestamp
        self.usdPrice = usdPrice

    @classmethod
    def from_dict(cls, **data):
        return cls(
            blockHeight=data.get("blockHeight"),
            timestamp=data.get("timestamp"),
            usdPrice=data.get("usdPrice"),
        )


class GetTokenPriceHistoryReply:
    def __init__(self, quotes: List[Quote], syncStatus: SyncStatus = None):
        self.quotes = quotes
        self.syncStatus = syncStatus

    @classmethod
    def from_dict(cls, **data):
        return cls(
            quotes=[
                Quote.from_dict(**quote_data) for quote_data in data.get("quotes", [])
            ],
            syncStatus=SyncStatus.from_dict(**data.get("syncStatus"))
            if data.get("syncStatus") is not None
            else None,
        )


class ExplainTokenPriceRequest:
    def __init__(
        self,
        blockHeight: float | Literal[Literal["latest"]] | Literal[Literal["earliest"]],
        blockchain: Blockchain,
        tokenAddress: str,
    ):
        self.blockHeight = blockHeight
        self.blockchain = blockchain
        self.tokenAddress = tokenAddress

    def to_dict(self):
        if isinstance(self.blockchain, str):
            blockchain_value = self.blockchain
        elif isinstance(self.blockchain, list):
            blockchain_value = [
                block.value if isinstance(block, Blockchain) else block
                for block in self.blockchain
            ]
        elif self.blockchain is not None:
            blockchain_value = self.blockchain.value
        else:
            blockchain_value = None
        return {
            "blockHeight": self.blockHeight,
            "blockchain": blockchain_value,
            "tokenAddress": self.tokenAddress,
        }


class PriceEstimate:
    def __init__(self, price: str, strategy: str):
        self.price = price
        self.strategy = strategy

    @classmethod
    def from_dict(cls, **data):
        return cls(
            price=data.get("price"),
            strategy=data.get("strategy"),
        )


class ExplainTokenPriceLPDetails:
    def __init__(
        self,
        address: str,
        lastUpdatedBlock: float,
        price: str,
        reserve0: str,
        reserve1: str,
        token0: str,
        token1: str,
    ):
        self.address = address
        self.lastUpdatedBlock = lastUpdatedBlock
        self.price = price
        self.reserve0 = reserve0
        self.reserve1 = reserve1
        self.token0 = token0
        self.token1 = token1

    @classmethod
    def from_dict(cls, **data):
        return cls(
            address=data.get("address"),
            lastUpdatedBlock=data.get("lastUpdatedBlock"),
            price=data.get("price"),
            reserve0=data.get("reserve0"),
            reserve1=data.get("reserve1"),
            token0=data.get("token0"),
            token1=data.get("token1"),
        )


class ExplainTokenPriceTokenDetails:
    def __init__(self, contractAddress: str, decimals: float, name: str, symbol: str):
        self.contractAddress = contractAddress
        self.decimals = decimals
        self.name = name
        self.symbol = symbol

    @classmethod
    def from_dict(cls, **data):
        return cls(
            contractAddress=data.get("contractAddress"),
            decimals=data.get("decimals"),
            name=data.get("name"),
            symbol=data.get("symbol"),
        )


class ExplainTokenPriceSinglePair:
    def __init__(
        self,
        liquidity_pools: List[ExplainTokenPriceLPDetails],
        priceEstimates: List[PriceEstimate],
        token0: ExplainTokenPriceTokenDetails,
        token1: ExplainTokenPriceTokenDetails,
    ):
        self.liquidity_pools = liquidity_pools
        self.priceEstimates = priceEstimates
        self.token0 = token0
        self.token1 = token1

    @classmethod
    def from_dict(cls, **data):
        return cls(
            liquidity_pools=[
                ExplainTokenPriceLPDetails.from_dict(**explaintokenpricelpdetails_data)
                for explaintokenpricelpdetails_data in data.get("liquidity_pools", [])
            ],
            priceEstimates=[
                PriceEstimate.from_dict(**priceestimate_data)
                for priceestimate_data in data.get("priceEstimates", [])
            ],
            token0=ExplainTokenPriceTokenDetails.from_dict(**data.get("token0"))
            if data.get("token0") is not None
            else None,
            token1=ExplainTokenPriceTokenDetails.from_dict(**data.get("token1"))
            if data.get("token1") is not None
            else None,
        )


class ExplainTokenPriceReply:
    def __init__(
        self,
        blockchain: str,
        pairs: List[ExplainTokenPriceSinglePair],
        priceEstimates: List[PriceEstimate],
        tokenAddress: str,
    ):
        self.blockchain = blockchain
        self.pairs = pairs
        self.priceEstimates = priceEstimates
        self.tokenAddress = tokenAddress

    @classmethod
    def from_dict(cls, **data):
        return cls(
            blockchain=data.get("blockchain"),
            pairs=[
                ExplainTokenPriceSinglePair.from_dict(
                    **explaintokenpricesinglepair_data
                )
                for explaintokenpricesinglepair_data in data.get("pairs", [])
            ],
            priceEstimates=[
                PriceEstimate.from_dict(**priceestimate_data)
                for priceestimate_data in data.get("priceEstimates", [])
            ],
            tokenAddress=data.get("tokenAddress"),
        )


class GetInternalTransactionsByParentHashRequest:
    def __init__(
        self,
        blockchain: Blockchain,
        onlyWithValue: bool,
        parentTransactionHash: str,
        syncCheck: bool = None,
    ):
        self.blockchain = blockchain
        self.onlyWithValue = onlyWithValue
        self.parentTransactionHash = parentTransactionHash
        self.syncCheck = syncCheck

    def to_dict(self):
        if isinstance(self.blockchain, str):
            blockchain_value = self.blockchain
        elif isinstance(self.blockchain, list):
            blockchain_value = [
                block.value if isinstance(block, Blockchain) else block
                for block in self.blockchain
            ]
        elif self.blockchain is not None:
            blockchain_value = self.blockchain.value
        else:
            blockchain_value = None
        return {
            "blockchain": blockchain_value,
            "onlyWithValue": self.onlyWithValue,
            "parentTransactionHash": self.parentTransactionHash,
            "syncCheck": self.syncCheck,
        }


class GetInternalTransactionsByBlockNumberRequest:
    def __init__(
        self,
        blockNumber: float,
        blockchain: Blockchain,
        onlyWithValue: bool,
        syncCheck: bool = None,
    ):
        self.blockNumber = blockNumber
        self.blockchain = blockchain
        self.onlyWithValue = onlyWithValue
        self.syncCheck = syncCheck

    def to_dict(self):
        if isinstance(self.blockchain, str):
            blockchain_value = self.blockchain
        elif isinstance(self.blockchain, list):
            blockchain_value = [
                block.value if isinstance(block, Blockchain) else block
                for block in self.blockchain
            ]
        elif self.blockchain is not None:
            blockchain_value = self.blockchain.value
        else:
            blockchain_value = None
        return {
            "blockNumber": self.blockNumber,
            "blockchain": blockchain_value,
            "onlyWithValue": self.onlyWithValue,
            "syncCheck": self.syncCheck,
        }


class InternalTransaction:
    def __init__(
        self,
        blockHash: str,
        blockHeight: float,
        blockchain: Blockchain,
        callType: str,
        fromAddress: str,
        gas: float,
        gasUsed: float,
        input: str,
        output: str,
        timestamp: str,
        toAddress: str,
        transactionHash: str,
        transactionIndex: float,
        value: str,
        callPath: str = None,
        callStack: List[float] = None,
        error: str = None,
        contractAddress: str = None,
    ):
        self.blockHash = blockHash
        self.blockHeight = blockHeight
        self.blockchain = blockchain
        self.callType = callType
        self.fromAddress = fromAddress
        self.gas = gas
        self.gasUsed = gasUsed
        self.input = input
        self.output = output
        self.timestamp = timestamp
        self.toAddress = toAddress
        self.transactionHash = transactionHash
        self.transactionIndex = transactionIndex
        self.value = value
        self.callPath = callPath
        self.callStack = callStack
        self.error = error
        self.contractAddress = contractAddress

    @classmethod
    def from_dict(cls, **data):
        return cls(
            blockHash=data.get("blockHash"),
            blockHeight=data.get("blockHeight"),
            blockchain=Blockchain(data.get("blockchain")),
            callType=data.get("callType"),
            fromAddress=data.get("fromAddress"),
            gas=data.get("gas"),
            gasUsed=data.get("gasUsed"),
            input=data.get("input"),
            output=data.get("output"),
            timestamp=data.get("timestamp"),
            toAddress=data.get("toAddress"),
            transactionHash=data.get("transactionHash"),
            transactionIndex=data.get("transactionIndex"),
            value=data.get("value"),
            callPath=data.get("callPath"),
            callStack=data.get("callStack"),
            error=data.get("error"),
            contractAddress=data.get("contractAddress"),
        )


class GetInternalTransactionsReply:
    def __init__(
        self, internalTransactions: List[InternalTransaction], nextPageToken: str = None
    ):
        self.internalTransactions = internalTransactions
        self.nextPageToken = nextPageToken

    @classmethod
    def from_dict(cls, **data):
        return cls(
            internalTransactions=[
                InternalTransaction.from_dict(**internaltransaction_data)
                for internaltransaction_data in data.get("internalTransactions", [])
            ],
            nextPageToken=data.get("nextPageToken"),
        )


class GetAccountBalanceHistoricalRequest:
    def __init__(
        self,
        walletAddress: str,
        blockchain: Blockchain | List[Blockchain] = None,
        onlyWhitelisted: bool = None,
        nativeFirst: bool = None,
        pageToken: str = None,
        pageSize: float = None,
        blockHeight: float
        | Literal[Literal["latest"]]
        | Literal[Literal["earliest"]] = None,
        syncCheck: bool = None,
    ):
        self.walletAddress = walletAddress
        self.blockchain = blockchain
        self.onlyWhitelisted = onlyWhitelisted
        self.nativeFirst = nativeFirst
        self.pageToken = pageToken
        self.pageSize = pageSize
        self.blockHeight = blockHeight
        self.syncCheck = syncCheck

    def to_dict(self):
        if isinstance(self.blockchain, str):
            blockchain_value = self.blockchain
        elif isinstance(self.blockchain, list):
            blockchain_value = [
                block.value if isinstance(block, Blockchain) else block
                for block in self.blockchain
            ]
        elif self.blockchain is not None:
            blockchain_value = self.blockchain.value
        else:
            blockchain_value = None
        return {
            "walletAddress": self.walletAddress,
            "blockchain": blockchain_value,
            "onlyWhitelisted": self.onlyWhitelisted,
            "nativeFirst": self.nativeFirst,
            "pageToken": self.pageToken,
            "pageSize": self.pageSize,
            "blockHeight": self.blockHeight,
            "syncCheck": self.syncCheck,
        }


class GetAccountBalanceHistoricalReply:
    def __init__(
        self,
        assets: List[Balance],
        totalBalanceUsd: str,
        totalCount: float,
        nextPageToken: str = None,
        syncStatus: SyncStatus = None,
        blockHeight: float
        | Literal[Literal["latest"]]
        | Literal[Literal["earliest"]] = None,
    ):
        self.assets = assets
        self.totalBalanceUsd = totalBalanceUsd
        self.totalCount = totalCount
        self.nextPageToken = nextPageToken
        self.syncStatus = syncStatus
        self.blockHeight = blockHeight

    @classmethod
    def from_dict(cls, **data):
        return cls(
            assets=[
                Balance.from_dict(**balance_data)
                for balance_data in data.get("assets", [])
            ],
            totalBalanceUsd=data.get("totalBalanceUsd"),
            totalCount=data.get("totalCount"),
            nextPageToken=data.get("nextPageToken"),
            syncStatus=SyncStatus.from_dict(**data.get("syncStatus"))
            if data.get("syncStatus") is not None
            else None,
            blockHeight=data.get("blockHeight"),
        )


class Blockchain(Enum):
    Arbitrum = "arbitrum"
    Avalanche = "avalanche"
    Avalanche_fuji = "avalanche_fuji"
    Base = "base"
    Bsc = "bsc"
    Eth = "eth"
    Eth_goerli = "eth_goerli"
    Fantom = "fantom"
    Flare = "flare"
    Gnosis = "gnosis"
    Linea = "linea"
    Optimism = "optimism"
    Optimism_testnet = "optimism_testnet"
    Polygon = "polygon"
    Polygon_mumbai = "polygon_mumbai"
    Polygon_zkevm = "polygon_zkevm"
    Rollux = "rollux"
    Scroll = "scroll"
    Syscoin = "syscoin"
