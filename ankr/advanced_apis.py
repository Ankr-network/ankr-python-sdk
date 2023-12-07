from __future__ import annotations

from typing import Iterable, List, Optional

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
            limit=limit,
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
            limit=limit,
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
            limit=limit,
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
    ) -> Iterable[types.Log]:
        for log in self.provider.call_method_paginated(
            rpc="ankr_getLogs",
            request=request,
            reply=types.GetLogsReply,
            iterable_name="logs",
            iterable_type=types.Log,
            limit=limit,
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
        request: types.GetBlocksRequest,
    ) -> List[types.Block]:
        reply = self.provider.call_method(
            rpc="ankr_getBlocks",
            request=request,
            reply=types.GetBlocksReply,
        )

        return reply.blocks

    def get_blocks_raw(
        self,
        request: types.GetBlocksRequest,
    ) -> types.GetBlocksReply:
        reply = self.provider.call_method(
            rpc="ankr_getBlocks",
            request=request,
            reply=types.GetBlocksReply,
        )

        return reply

    def get_transaction(
        self,
        request: types.GetTransactionsByHashRequest,
    ) -> types.Transaction | None:
        reply = self.provider.call_method(
            rpc="ankr_getTransactionsByHash",
            request=request,
            reply=types.GetTransactionsByHashReply,
        )

        if len(reply.transactions) > 0:
            return reply.transactions[0]
        else:
            return None

    def get_transaction_raw(
        self,
        request: types.GetTransactionsByHashRequest,
    ) -> types.GetTransactionsByHashReply:
        reply = self.provider.call_method(
            rpc="ankr_getTransactionsByHash",
            request=request,
            reply=types.GetTransactionsByHashReply,
        )

        return reply

    def get_transactions_by_address(
        self,
        request: types.GetTransactionsByAddressRequest,
        limit: Optional[int] = None,
    ) -> Iterable[types.Transaction]:
        for transaction in self.provider.call_method_paginated(
            rpc="ankr_getTransactionsByAddress",
            request=request,
            reply=types.GetTransactionsByAddressReply,
            iterable_name="transactions",
            iterable_type=types.Transaction,
            limit=limit,
        ):
            yield transaction

    def get_transactions_by_address_raw(
        self,
        request: types.GetTransactionsByAddressRequest,
    ) -> types.GetTransactionsByAddressReply:
        reply = self.provider.call_method(
            rpc="ankr_getTransactionsByAddress",
            request=request,
            reply=types.GetTransactionsByAddressReply,
        )

        return reply

    def get_blockchain_stats(
        self,
        request: types.GetBlockchainStatsRequest,
    ) -> List[types.BlockchainStats]:
        reply = self.provider.call_method(
            rpc="ankr_getBlockchainStats",
            request=request,
            reply=types.GetBlockchainStatsReply,
        )

        return reply.stats

    def get_blockchain_stats_raw(
        self,
        request: types.GetBlockchainStatsRequest,
    ) -> types.GetBlockchainStatsReply:
        reply = self.provider.call_method(
            rpc="ankr_getBlockchainStats",
            request=request,
            reply=types.GetBlockchainStatsReply,
        )

        return reply

    def get_interactions(
        self,
        request: types.GetInteractionsRequest,
    ) -> List[types.Blockchain]:
        reply = self.provider.call_method(
            rpc="ankr_getInteractions",
            request=request,
            reply=types.GetInteractionsReply,
        )

        return reply.blockchains

    def get_interactions_raw(
        self,
        request: types.GetInteractionsRequest,
    ) -> types.GetInteractionsReply:
        reply = self.provider.call_method(
            rpc="ankr_getInteractions",
            request=request,
            reply=types.GetInteractionsReply,
        )

        return reply


class AnkrTokenAPI(AnkrMultichainAPI):
    def explain_token_price(
        self,
        request: types.ExplainTokenPriceRequest,
    ) -> ([types.ExplainTokenPriceSinglePair], [types.PriceEstimate]):
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
            limit=limit,
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
            limit=limit,
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
            limit=limit,
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
    ) -> types.DailyHolderCount:
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

    def get_token_price(self, request: types.GetTokenPriceRequest) -> str:
        reply = self.provider.call_method(
            rpc="ankr_getTokenPrice",
            request=request,
            reply=types.GetTokenPriceReply,
        )
        return reply.usdPrice

    def get_token_price_raw(
        self, request: types.GetTokenPriceRequest
    ) -> types.GetTokenPriceReply:
        reply = self.provider.call_method(
            rpc="ankr_getTokenPrice",
            request=request,
            reply=types.GetTokenPriceReply,
        )
        return reply

    def get_token_transfers(
        self, request: types.GetTransfersRequest, limit: Optional[int] = None
    ) -> Iterable[types.TokenTransfer]:
        for transfer in self.provider.call_method_paginated(
            rpc="ankr_getTokenTransfers",
            request=request,
            reply=types.GetTokenTransfersReply,
            iterable_name="transfers",
            iterable_type=types.TokenTransfer,
            limit=limit,
        ):
            yield transfer

    def get_token_transfers_raw(
        self, request: types.GetTransfersRequest
    ) -> types.GetTokenTransfersReply:
        reply = self.provider.call_method(
            rpc="ankr_getTokenTransfers",
            request=request,
            reply=types.GetTokenTransfersReply,
        )
        return reply


class AnkrNFTAPI(AnkrMultichainAPI):
    def get_nfts(
        self, request: types.GetNFTsByOwnerRequest, limit: Optional[int] = None
    ) -> Iterable[types.Nft]:
        for nft in self.provider.call_method_paginated(
            rpc="ankr_getNFTsByOwner",
            request=request,
            reply=types.GetNFTsByOwnerReply,
            iterable_name="assets",
            iterable_type=types.Nft,
            limit=limit,
        ):
            yield nft

    def get_nfts_raw(
        self, request: types.GetNFTsByOwnerRequest
    ) -> types.GetNFTsByOwnerReply:
        reply = self.provider.call_method(
            rpc="ankr_getNFTsByOwner",
            request=request,
            reply=types.GetNFTsByOwnerReply,
        )
        return reply

    def get_nft_metadata(
        self, request: types.GetNFTMetadataRequest
    ) -> types.GetNFTMetadataReply:
        reply = self.provider.call_method(
            rpc="ankr_getNFTMetadata",
            request=request,
            reply=types.GetNFTMetadataReply,
        )
        return reply

    def get_nft_metadata_raw(
        self, request: types.GetNFTMetadataRequest
    ) -> types.GetNFTMetadataReply:
        reply = self.provider.call_method(
            rpc="ankr_getNFTMetadata",
            request=request,
            reply=types.GetNFTMetadataReply,
        )
        return reply

    def get_nft_holders(
        self,
        request: types.GetNFTHoldersRequest,
        limit: Optional[int] = None,
    ) -> Iterable[str]:
        for holder in self.provider.call_method_paginated(
            rpc="ankr_getNFTHolders",
            request=request,
            reply=types.GetNFTHoldersReply,
            iterable_name="holders",
            iterable_type=str,
            limit=limit,
        ):
            yield holder

    def get_nft_holders_raw(
        self,
        request: types.GetNFTHoldersRequest,
    ) -> types.GetNFTHoldersReply:
        reply = self.provider.call_method(
            rpc="ankr_getNFTHolders",
            request=request,
            reply=types.GetNFTHoldersReply,
        )
        return reply

    def get_nft_transfers(
        self, request: types.GetTransfersRequest, limit: Optional[int] = None
    ) -> Iterable[types.NftTransfer]:
        for transfer in self.provider.call_method_paginated(
            rpc="ankr_getNftTransfers",
            request=request,
            reply=types.GetNftTransfersReply,
            iterable_name="transfers",
            iterable_type=types.NftTransfer,
            limit=limit,
        ):
            yield transfer

    def get_nft_transfers_raw(
        self, request: types.GetTransfersRequest
    ) -> types.GetNftTransfersReply:
        reply = self.provider.call_method(
            rpc="ankr_getNftTransfers",
            request=request,
            reply=types.GetNftTransfersReply,
        )
        return reply


class AnkrAdvancedAPI(AnkrEarlyAccessAPI, AnkrQueryAPI, AnkrTokenAPI, AnkrNFTAPI):
    ...
