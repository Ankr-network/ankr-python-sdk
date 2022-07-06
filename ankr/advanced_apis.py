from __future__ import annotations

from typing import Any, Dict, Iterable, List, Optional

from ankr import types
from ankr.exceptions import APIError
from ankr.providers import MultichainHTTPProvider


class AnkrMultichainAPI:
    def __init__(
        self,
        api_key: Optional[str] = None,
        endpoint_uri: Optional[str] = None,
    ) -> None:
        self.provider = MultichainHTTPProvider(api_key or "", endpoint_uri)


class AnkrQueryAPI(AnkrMultichainAPI):
    def get_logs(
        self,
        blockchain: types.BlockchainNames,
        from_block: Optional[types.BlockNumber] = None,
        to_block: Optional[types.BlockNumber] = None,
        address: Optional[types.AddressOrAddresses] = None,
        topics: Optional[types.Topics] = None,
        decode_logs: Optional[bool] = None,
        limit: Optional[int] = None,
        **kwargs: Any,
    ) -> Iterable[types.Log]:
        for log in self.provider.call_method_paginated(
            "ankr_getLogs",
            types.GetLogsRequest(
                blockchain=blockchain,
                from_block=from_block,
                to_block=to_block,
                address=address,
                topics=topics,
                decode_logs=decode_logs,
                **kwargs,
            ),
            reply_type=types.GetLogsReply,
            iterable_name="logs",
            iterable_type=types.Log,
            limit=limit,
        ):
            yield log

    def get_blocks(
        self,
        blockchain: types.BlockchainName,
        from_block: Optional[types.BlockNumber] = None,
        to_block: Optional[types.BlockNumber] = None,
        desc_order: Optional[bool] = None,
        include_logs: Optional[bool] = None,
        include_txs: Optional[bool] = None,
        decode_logs: Optional[bool] = None,
        decode_tx_data: Optional[bool] = None,
        **kwargs: Any,
    ) -> List[types.Block]:
        reply = self.provider.call_method(
            "ankr_getBlocks",
            types.GetBlocksRequest(
                blockchain=blockchain,
                from_block=from_block,
                to_block=to_block,
                desc_order=desc_order,
                include_logs=include_logs,
                include_txs=include_txs,
                decode_logs=decode_logs,
                decode_tx_data=decode_tx_data,
                **kwargs,
            ),
            types.GetBlocksReply,
        )
        return reply.blocks

    def get_transaction(
        self,
        transaction_hash: str,
        blockchain: Optional[types.BlockchainNames] = None,
        include_logs: Optional[bool] = False,
        decode_logs: Optional[bool] = False,
        decode_tx_data: Optional[bool] = False,
        **kwargs: Any,
    ) -> Optional[types.Transaction]:
        reply = self.provider.call_method(
            "ankr_getTransactionsByHash",
            types.GetTransactionsByHashRequest(
                blockchain=blockchain,
                transaction_hash=transaction_hash,
                include_logs=include_logs,
                decode_logs=decode_logs,
                decode_tx_data=decode_tx_data,
                **kwargs,
            ),
            types.GetTransactionsByHashReply,
        )
        if reply.transactions:
            return reply.transactions[0]


class AnkrTokenAPI(AnkrMultichainAPI):
    def get_token_holders(
        self,
        blockchain: types.BlockchainName,
        contract_address: str,
        limit: Optional[int] = None,
        **kwargs: Any,
    ) -> Iterable[types.HolderBalance]:
        for holder in self.provider.call_method_paginated(
            "ankr_getTokenHolders",
            types.GetTokenHoldersRequest(
                blockchain=blockchain,
                contract_address=contract_address,
                reply_type=types.GetLogsReply,
                **kwargs,
            ),
            types.GetTokenHoldersReply,
            iterable_name="holders",
            iterable_type=types.HolderBalance,
            limit=limit,
        ):
            yield holder

    def get_token_holders_count_history(
        self,
        blockchain: types.BlockchainName,
        contract_address: str,
        limit: Optional[int] = None,
        **kwargs: Any,
    ) -> Iterable[types.DailyHolderCount]:
        for daily_holder_count in self.provider.call_method_paginated(
            "ankr_getTokenHoldersCount",
            types.GetTokenHoldersCountRequest(
                blockchain=blockchain,
                contract_address=contract_address,
                **kwargs,
            ),
            types.GetTokenHoldersCountReply,
            iterable_name="holder_count_history",
            iterable_type=types.DailyHolderCount,
            limit=limit,
        ):
            yield daily_holder_count

    def get_token_holders_count(
        self,
        blockchain: types.BlockchainName,
        contract_address: str,
        **kwargs: Any,
    ) -> types.DailyHolderCount:
        reply = self.provider.call_method(
            rpc="ankr_getTokenHoldersCount",
            request=types.GetTokenHoldersCountRequest(
                blockchain=blockchain,
                contract_address=contract_address,
                page_size=1,
                **kwargs,
            ),
            reply_type=types.GetTokenHoldersCountReply,
        )
        if len(reply.holder_count_history) < 1:
            raise APIError("no token holders count found")
        return reply.holder_count_history[0]

    def get_account_balance(
        self,
        wallet_address: str,
        blockchain: Optional[types.BlockchainNames] = None,
        limit: Optional[int] = None,
        **kwargs: Any,
    ) -> Iterable[types.Balance]:
        for asset in self.provider.call_method_paginated(
            rpc="ankr_getAccountBalance",
            request=types.GetAccountBalanceRequest(
                blockchain=blockchain,
                wallet_address=wallet_address,
                **kwargs,
            ),
            reply_type=types.GetAccountBalanceReply,
            iterable_name="assets",
            iterable_type=types.Balance,
            limit=limit,
        ):
            yield asset


class AnkrNFTAPI(AnkrMultichainAPI):
    def get_nfts(
        self,
        blockchain: types.BlockchainNames,
        wallet_address: str,
        filter: Optional[List[Dict[str, List[str]]]] = None,
        limit: Optional[int] = None,
        **kwargs: Any,
    ) -> Iterable[types.Nft]:
        for nft in self.provider.call_method_paginated(
            "ankr_getNFTsByOwner",
            types.GetNFTsByOwnerRequest(
                blockchain=blockchain,
                wallet_address=wallet_address,
                filter=filter,
                **kwargs,
            ),
            types.GetNFTsByOwnerReply,
            iterable_name="assets",
            iterable_type=types.Nft,
            limit=limit,
        ):
            yield nft

    def get_nft_metadata(
        self,
        blockchain: types.BlockchainName,
        contract_address: str,
        token_id: str,
        **kwargs: Any,
    ) -> types.GetNFTMetadataReply:
        return self.provider.call_method(
            "ankr_getNFTMetadata",
            types.GetNFTMetadataRequest(
                blockchain=blockchain,
                contract_address=contract_address,
                token_id=token_id,
                **kwargs,
            ),
            types.GetNFTMetadataReply,
        )


class AnkrAdvancedAPI(AnkrQueryAPI, AnkrTokenAPI, AnkrNFTAPI):
    ...
