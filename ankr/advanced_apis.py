from __future__ import annotations

from typing import Any, Dict, Iterable, List, Optional

import ankr.types
import ankr_gen
from ankr import types
from ankr.exceptions import APIError

class AnkrMultichainAPI:
    def __init__(
        self,
        api_key: str,
        # endpoint_uri: Optional[str] = None,
    ) -> None:
        configuration = ankr_gen.Configuration()
        configuration.host = f"https://rpc.ankr.com/multichain/{api_key}"
        # if endpoint_uri is not None:
        #     configuration.host = endpoint_uri
        # self.provider = MultichainHTTPProvider(api_key, "https://rpc.ankr.com/multichain/")
        self.provider = ankr_gen.ApiClient(configuration=configuration)

    def __del__(self):
        self.provider.__del__()

    def call_method(
            self,
            method: str,
            request_params: Any,
            call_function : Any,
            body_type : Any,
    ) -> Any:
        body = body_type(
            id=1,
            jsonrpc="2.0",
            method=method,
            params=request_params
        )
        response = call_function(body=body)
        reply = response.result

        if reply is None:
            error = response.error
            return error

        return reply

    def call_method_paginated(
            self,
            *,
            method: str,
            request_params: Any,
            iterable_name: str,
            limit: Optional[int] = None,
            call_function : Any,
            body_type : Any,
    ) -> Iterable[Any]:
        body = body_type(
            id=1,
            jsonrpc="2.0",
            method=method,
            params=request_params
        )

        response = call_function(body=body)
        reply = response.result

        error = None

        if reply is None:
            error = response.error
            yield error
            return

        items: List[Any] = reply.get(iterable_name, []) if isinstance(reply, dict) else []

        if limit:
            if limit <= len(items):
                yield from items[:limit]
                return
            limit -= len(items)

        yield from items

        if reply.get('nextPageToken'):
            request_params.page_token = reply.get('nextPageToken')
            yield from self.call_method_paginated(
                method=method,
                request_params=request_params,
                iterable_name=iterable_name,
                limit=limit,
                call_function=call_function,
                body_type=body_type
            )



class AnkrQueryAPI(AnkrMultichainAPI):
    def __init__(
            self,
            api_key: str,
            # endpoint_uri: Optional[str] = None,
    ) -> None:
        super().__init__(api_key)
        self.api = ankr_gen.QueryAPIApi(api_client=self.provider)

    def __del__(self):
        super().__del__()

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
    ) -> Iterable[Any]:
        for log in super().call_method_paginated(
                method="ankr_getLogs",
                request_params=ankr_gen.AnkrGetLogsParams(
                    blockchain=blockchain,
                    from_block=from_block,
                    to_block=to_block,
                    address=address,
                    topics=topics,
                    decode_logs=decode_logs,
                    **kwargs
                ),
                iterable_name="logs",
                limit=limit,
                call_function=self.api.ankr_get_logs_post,
                body_type=ankr_gen.AnkrGetLogsBody
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
    ) -> List[Any]:
        reply = super().call_method(
            "ankr_getBlocks",
            request_params = ankr_gen.AnkrGetBlocksParams(
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
            call_function=self.api.ankr_get_blocks_post,
            body_type=ankr_gen.AnkrGetBlocksBody
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
    def __init__(
            self,
            api_key: str,
            # endpoint_uri: Optional[str] = None,
    ) -> None:
        super().__init__(api_key)
        self.api = ankr_gen.TokenAPIApi(api_client=self.provider)

    def __del__(self):
        super().__del__()

    def get_token_holders(
        self,
        blockchain: types.BlockchainName,
        contract_address: str,
        limit: Optional[int] = None,
        **kwargs: Any,
    ) -> Iterable[Any]:
        for holder in super().call_method_paginated(
                method="ankr_getTokenHolders",
                request_params=ankr_gen.AnkrGetTokenHoldersParams(
                    blockchain=blockchain,
                    contract_address=contract_address,
                    **kwargs,
                ),
                iterable_name="holders",
                limit=limit,
                call_function=self.api.ankr_get_token_holders_post,
                body_type=ankr_gen.AnkrGetTokenHoldersBody
        ):
            yield holder

    def get_token_holders_count_history(
        self,
        blockchain: types.BlockchainName,
        contract_address: str,
        limit: Optional[int] = None,
        **kwargs: Any,
    ) -> Iterable[Any]:
        for daily_holder_count in super().call_method_paginated(
                method="ankr_getTokenHoldersCount",
                request_params=ankr_gen.AnkrGetTokenHoldersParams(
                    blockchain=blockchain,
                    contract_address=contract_address,
                    **kwargs,
                ),
                iterable_name="holderCountHistory",
                limit=limit,
                call_function=self.api.ankr_get_token_holders_count_post,
                body_type=ankr_gen.AnkrGetTokenHoldersCountBody
        ):
            yield daily_holder_count

    def get_token_holders_count(
        self,
        blockchain: types.BlockchainName,
        contract_address: str,
        **kwargs: Any,
    ) -> Any:
        reply = super().call_method(
            "ankr_getTokenHoldersCount",
            request_params = ankr_gen.AnkrGetTokenHoldersParams(
                blockchain=blockchain,
                contract_address=contract_address,
                page_size=1,
                **kwargs,
            ),
            call_function=self.api.ankr_get_token_holders_count_post,
            body_type=ankr_gen.AnkrGetTokenHoldersCountBody
        )

        if not reply['holderCountHistory'] or (
                reply['holderCountHistory'] and len(reply['holderCountHistory']) < 1):
            raise APIError("no token holders count found")

        return reply['holderCountHistory'][0]

    def get_token_price(
        self,
        blockchain: types.BlockchainName,
        contract_address: str,
        **kwargs: Any,
    ) -> str:
        reply = super().call_method(
            "ankr_getTokenPrice",
            request_params = ankr_gen.AnkrGetTokenPriceParams(
                blockchain=blockchain,
                contract_address=contract_address,
                **kwargs,
            ),
            call_function=self.api.ankr_get_token_price_post,
            body_type=ankr_gen.AnkrGetTokenPriceBody
        )


        return reply['usdPrice']

    def get_account_balance(
        self,
        wallet_address: str,
        blockchain: Optional[types.BlockchainNames] = None,
        limit: Optional[int] = None,
        **kwargs: Any,
    ) -> Iterable[Any]:
        for asset in super().call_method_paginated(
                method="ankr_getAccountBalance",
                request_params=ankr_gen.AnkrGetAccountBalanceParams(
                    blockchain=blockchain,
                    wallet_address=wallet_address,
                    **kwargs,
                ),
                iterable_name="assets",
                limit=limit,
                call_function=self.api.ankr_get_account_balance_post,
                body_type=ankr_gen.AnkrGetAccountBalanceBody
        ):
            yield asset


class AnkrNFTAPI(AnkrMultichainAPI):
    def __init__(
            self,
            api_key: str,
            # endpoint_uri: Optional[str] = None,
    ) -> None:
        super().__init__(api_key)
        self.api = ankr_gen.NFTAPIApi(api_client=self.provider)

    def __del__(self):
        super().__del__()

    def get_nfts(
        self,
        blockchain: types.BlockchainNames,
        wallet_address: str,
        filter: Optional[List[Dict[str, List[str]]]] = None,
        limit: Optional[int] = None,
        **kwargs: Any,
    ) -> Iterable[Any]:
        for nft in super().call_method_paginated(
                method="ankr_getNFTsByOwner",
                request_params=ankr_gen.AnkrGetNFTsByOwnerParams(
                    blockchain=blockchain,
                    wallet_address=wallet_address,
                    filter=filter,
                    **kwargs,
                ),
                iterable_name="assets",
                limit=limit,
                call_function=self.api.ankr_get_nfts_by_owner_post,
                body_type=ankr_gen.AnkrGetNFTsByOwnerBody
        ):
            yield nft

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


class AnkrAdvancedAPI(AnkrQueryAPI, AnkrTokenAPI, AnkrNFTAPI):
    ...
