from __future__ import annotations

from typing import Any, Iterable, List, Optional

from ankr import types
from ankr.exceptions import APIError
from ankr.providers import MultichainHTTPProvider


class AnkrMultichainAPI:
    def __init__(
        self,
        api_key: str,
        endpoint_uri: Optional[str] = None,
    ) -> None:
        self.provider = MultichainHTTPProvider(api_key, endpoint_uri)


class AnkrEarlyAccessAPI(AnkrMultichainAPI):
    def get_token_price_history(
            self,
            request: types.GetTokenPriceHistoryRequest,
    ) -> [types.Quote]:
        reply = self.provider.call_method(
            rpc="ankr_getTokenPriceHistory",
            request=request,
            reply=types.GetTokenPriceHistoryReply,
        )

        if reply.quotes:
            return reply.quotes
        else:
            return []

    def get_token_price_history_raw(
            self,
            request: types.GetTokenPriceHistoryRequest,
    ) -> types.GetTokenPriceHistoryReply:
        reply = self.provider.call_method(
            rpc="ankr_getTokenPriceHistory",
            request=request,
            reply=types.GetTokenPriceHistoryReply,
        )

        return reply

    def get_account_balance_historical(
            self,
            request: types.GetAccountBalanceHistoricalRequest,
            limit: Optional[int] = None,
    ) -> Iterable[types.Balance]:
        for asset in self.provider.call_method_paginated(
                rpc="ankr_getAccountBalanceHistorical",
                request=request,
                reply=types.GetAccountBalanceHistoricalReply,
                iterable_name="assets",
                iterable_type=types.Balance,
                limit=limit
        ):
            yield asset

    def get_account_balance_historical_raw(
            self,
            request: types.GetAccountBalanceHistoricalRequest,
    ) -> types.GetAccountBalanceHistoricalReply:
        reply = self.provider.call_method(
            rpc="ankr_getAccountBalanceHistorical",
            request=request,
            reply=types.GetAccountBalanceReply,
        )

        return reply

    def get_internal_transactions_by_block_number(
            self,
            request: types.GetInternalTransactionsByBlockNumberRequest,
            limit: Optional[int] = None,
    ) -> Iterable[types.InternalTransaction]:
        for asset in self.provider.call_method_paginated(
                rpc="ankr_getInternalTransactionsByBlockNumber",
                request=request,
                reply=types.GetInternalTransactionsReply,
                iterable_name="internalTransactions",
                iterable_type=types.InternalTransaction,
                limit=limit
        ):
            yield asset

    def get_internal_transactions_by_block_number_raw(
            self,
            request: types.GetInternalTransactionsByBlockNumberRequest,
    ) -> types.GetInternalTransactionsReply:
        reply = self.provider.call_method(
            rpc="ankr_getInternalTransactionsByBlockNumber",
            request=request,
            reply=types.GetInternalTransactionsReply,
        )

        return reply

    def get_internal_transactions_by_parent_hash(
            self,
            request: types.GetInternalTransactionsByParentHashRequest,
            limit: Optional[int] = None,
    ) -> Iterable[types.InternalTransaction]:
        for asset in self.provider.call_method_paginated(
                rpc="ankr_getInternalTransactionsByParentHash",
                request=request,
                reply=types.GetInternalTransactionsReply,
                iterable_name="internalTransactions",
                iterable_type=types.InternalTransaction,
                limit=limit
        ):
            yield asset

    def get_internal_transactions_by_parent_hash_raw(
            self,
            request: types.GetInternalTransactionsByBlockNumberRequest,
    ) -> types.GetInternalTransactionsReply:
        reply = self.provider.call_method(
            rpc="ankr_getInternalTransactionsByParentHash",
            request=request,
            reply=types.GetInternalTransactionsReply,
        )

        return reply

class AnkrQueryAPI(AnkrMultichainAPI):
    def get_logs(
        self,
        request: types.GetLogsRequest,
        limit: Optional[int] = None,
    ) -> Iterable[types.GetLogsReply]:
        for log in self.provider.call_method_paginated(
                rpc="ankr_getLogs",
                request=request,
                reply=types.GetLogsReply,
                iterable_name="logs",
                iterable_type=types.Log,
                limit=limit
        ):
            yield log

    def get_logs_raw(
        self,
        request: types.GetLogsRequest,
    ) -> types.GetLogsReply:
        reply = self.provider.call_method(
                rpc="ankr_getLogs",
                request=request,
                reply=types.GetLogsReply,
        )

        return reply


    def get_blocks(
        self,
        request: types_gen.GetBlocksRequest,
    ) -> List[types_gen.Block]:
        reply = self.provider.call_method(
            rpc="ankr_getBlocks",
            request=request,
            reply=types_gen.GetBlocksReply,
        )

        return reply.blocks

    def get_blocks_raw(
        self,
        request: types_gen.GetBlocksRequest,
    ) -> types_gen.GetBlocksReply:
        reply = self.provider.call_method(
            rpc="ankr_getBlocks",
            request=request,
            reply=types_gen.GetBlocksReply,
        )

        return reply


    def get_transaction(
        self,
        transaction_hash: str,
        blockchain: Optional[types.BlockchainNames] = None,
        include_logs: Optional[bool] = False,
        decode_logs: Optional[bool] = False,
        decode_tx_data: Optional[bool] = False,
        **kwargs: Any,
    ) -> Optional[Any]:
        reply = super().call_method(
            "ankr_getTransactionsByHash",
            request_params = ankr_gen.AnkrGetTransactionsByHashParams(
                blockchain=blockchain,
                transaction_hash=transaction_hash,
                include_logs=include_logs,
                decode_logs=decode_logs,
                decode_tx_data=decode_tx_data,
                **kwargs,
            ),
            call_function=self.api.ankr_get_transactions_by_hash_post,
            body_type=ankr_gen.AnkrGetTransactionsByHashBody
        )

        if reply['transactions']:
            return reply['transactions'][0]


class AnkrTokenAPI(AnkrMultichainAPI):
    def explain_token_price(
            self,
            request: types.ExplainTokenPriceRequest,
    ) -> ([types.ExplainTokenPriceSinglePair],[types.PriceEstimate]):
        reply = self.provider.call_method(
            rpc="ankr_explainTokenPrice",
            request=request,
            reply=types.ExplainTokenPriceReply,
        )

        if reply.pairs and reply.priceEstimates:
            return reply.pairs, reply.priceEstimates
        elif reply.pairs:
            return reply.pairs, []
        elif reply.priceEstimates:
            return [], reply.priceEstimates
        else:
            return [], []

    def explain_token_price_raw(
            self,
            request: types.ExplainTokenPriceRequest,
    ) -> types.ExplainTokenPriceReply:
        reply = self.provider.call_method(
            rpc="ankr_explainTokenPrice",
            request=request,
            reply=types.ExplainTokenPriceReply,
        )

        return reply

    def get_account_balance(
            self,
            request: types.GetAccountBalanceRequest,
            limit: Optional[int] = None,
    ) -> Iterable[types.Balance]:
        for asset in self.provider.call_method_paginated(
                rpc="ankr_getAccountBalance",
                request=request,
                reply=types.GetAccountBalanceReply,
                iterable_name="assets",
                iterable_type=types.Balance,
                limit=limit
        ):
            yield asset

    def get_account_balance_raw(
            self,
            request: types.GetAccountBalanceRequest,
    ) -> types.GetAccountBalanceReply:
        reply = self.provider.call_method(
            rpc="ankr_getAccountBalance",
            request=request,
            reply=types.GetAccountBalanceReply,
        )

        return reply

    def get_currencies(
            self,
            request: types.GetCurrenciesRequest,
    ) -> List[types.CurrencyDetailsExtended]:
        reply = self.provider.call_method(
            rpc="ankr_getCurrencies",
            request=request,
            reply=types.GetCurrenciesReply,
        )

        return reply.currencies

    def get_currencies_raw(
            self,
            request: types.GetCurrenciesRequest,
    ) -> types.GetCurrenciesReply:
        reply = self.provider.call_method(
            rpc="ankr_getCurrencies",
            request=request,
            reply=types.GetCurrenciesReply,
        )

        return reply

    def get_token_holders(
            self,
            request: types.GetTokenHoldersRequest,
            limit: Optional[int] = None,
    ) -> Iterable[types.HolderBalance]:
        for asset in self.provider.call_method_paginated(
                rpc="ankr_getTokenHolders",
                request=request,
                reply=types.GetTokenHoldersReply,
                iterable_name="holders",
                iterable_type=types.HolderBalance,
                limit=limit
        ):
            yield asset

    def get_token_holders_raw(
            self,
            request: types.GetTokenHoldersRequest,
    ) -> types.GetTokenHoldersReply:
        reply = self.provider.call_method(
            rpc="ankr_getTokenHolders",
            request=request,
            reply=types.GetTokenHoldersReply,
        )
        return reply

    def get_token_holders_count_history(
            self,
            request: types.GetTokenHoldersCountRequest,
            limit: Optional[int] = None,
    ) -> Iterable[types.DailyHolderCount]:
        for holder in self.provider.call_method_paginated(
                rpc="ankr_getTokenHoldersCount",
                request=request,
                reply=types.GetTokenHoldersCountReply,
                iterable_name="holderCountHistory",
                iterable_type=types.DailyHolderCount,
                limit=limit
        ):
            yield holder

    def get_token_holders_count_history_raw(
            self,
            request: types.GetTokenHoldersCountRequest,
    ) -> types.GetTokenHoldersCountReply:
        reply = self.provider.call_method(
            rpc="ankr_getTokenHoldersCount",
            request=request,
            reply=types.GetTokenHoldersCountReply,
        )
        return reply

    def get_token_holders_count(
            self,
            request: types.GetTokenHoldersCountRequest,
    ) -> Iterable[types.DailyHolderCount]:
        request.pageSize = 1
        reply = self.provider.call_method(
            rpc="ankr_getTokenHoldersCount",
            request=request,
            reply=types.GetTokenHoldersCountReply,
        )
        if len(reply.holderCountHistory) < 1:
            raise APIError("no token holders count found")
        return reply.holderCountHistory[0]

    def get_token_holders_count_raw(
            self,
            request: types.GetTokenHoldersCountRequest,
    ) -> types.GetTokenHoldersCountReply:
        reply = self.provider.call_method(
            rpc="ankr_getTokenHoldersCount",
            request=request,
            reply=types.GetTokenHoldersCountReply,
        )
        return reply

    def get_token_price(
        self,
        request: types.GetTokenPriceRequest
    ) -> str:
        reply = self.provider.call_method(
            rpc="ankr_getTokenPrice",
            request=request,
            reply=types.GetTokenPriceReply,
        )
        return reply.usdPrice

    def get_token_price_raw(
        self,
        request: types.GetTokenPriceRequest
    ) -> types.GetTokenPriceReply:
        reply = self.provider.call_method(
            rpc="ankr_getTokenPrice",
            request=request,
            reply=types.GetTokenPriceReply,
        )
        return reply

    def get_token_transfers(
        self,
        request: types.GetTransfersRequest,
        limit: Optional[int] = None
    ) -> Iterable[types.TokenTransfer]:
        for transfer in self.provider.call_method_paginated(
                rpc="ankr_getTokenTransfers",
                request=request,
                reply=types.GetTokenTransfersReply,
                iterable_name="transfers",
                iterable_type=types.TokenTransfer,
                limit=limit
        ):
            yield transfer

    def get_token_transfers_raw(
        self,
        request: types.GetTransfersRequest
    ) -> types.GetTokenTransfersReply:
        reply = self.provider.call_method(
            rpc="ankr_getTokenTransfers",
            request=request,
            reply=types.GetTokenTransfersReply,
        )
        return reply



class AnkrNFTAPI(AnkrMultichainAPI):
    def get_nfts(
        self,
        request: types_gen.GetNFTsByOwnerRequest,
        limit: Optional[int] = None,
    ) -> Iterable[types_gen.GetNFTsByOwnerReply]:
        for nft in self.provider.call_method_paginated(
                rpc="ankr_getNFTsByOwner",
                request=request,
                reply=types_gen.GetNFTsByOwnerReply,
                iterable_name="assets",
                iterable_type=types_gen.Nft,
                limit=limit
        ):
            yield nft

    def get_nfts_raw(
        self,
        request: GetNFTsByOwnerRequest,
        limit: Optional[int] = None,
    ) -> GetNFTsByOwnerReply:
        reply = self.provider.call_method(
            rpc="ankr_getNFTsByOwner",
            request=request,
            reply=GetNFTsByOwnerReply,
        )

        return reply

    def get_nft_metadata(
        self,
        blockchain: types.BlockchainName,
        contract_address: str,
        token_id: str,
        **kwargs: Any,
    ) -> Any:
        return super().call_method(
            "ankr_getNFTMetadata",
            request_params = ankr_gen.AnkrGetNFTMetadataParams(
                blockchain=blockchain,
                contract_address=contract_address,
                token_id=token_id,
                **kwargs,
            ),
            call_function=self.api.ankr_get_nft_metadata_post,
            body_type=ankr_gen.AnkrGetNFTMetadataBody
        )

    def get_nft_holders(
        self,
        blockchain: types.BlockchainName,
        contract_address: str,
        limit: Optional[int] = None,
        **kwargs: Any,
    ) -> Iterable[types.Address]:
        return super().call_method_paginated(
                method="ankr_getNFTHolders",
                request_params=ankr_gen.AnkrGetNFTHoldersParams(
                    blockchain=blockchain,
                    contract_address=contract_address,
                    **kwargs,
                ),
                iterable_name="holders",
                limit=limit,
                call_function=self.api.ankr_get_nft_holders_post,
                body_type=ankr_gen.AnkrGetNFTHoldersBody
        )


class AnkrAdvancedAPI(AnkrEarlyAccessAPI, AnkrQueryAPI, AnkrTokenAPI, AnkrNFTAPI):
    ...
