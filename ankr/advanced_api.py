from __future__ import annotations

from typing import Any, Dict, Iterable, List, Optional

from ankr import types
from ankr.provider import AnkrProvider


class AnkrAdvancedAPI:
    def __init__(
        self,
        api_key: Optional[str] = None,
        endpoint_uri: Optional[str] = None,
    ) -> None:
        self.provider = AnkrProvider(api_key or "", endpoint_uri)

    def get_logs(
        self,
        blockchain: types.BlockchainNames,
        from_block: Optional[types.BlockNumber] = None,
        to_block: Optional[types.BlockNumber] = None,
        address: Optional[types.AddressOrAddresses] = None,
        topics: Optional[types.Topics] = None,
        decode_logs: Optional[bool] = None,
        **kwargs: Any,
    ) -> Iterable[types.Log]:
        for reply in self.provider.call_method_paginated(
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
            types.GetLogsReply,
        ):
            yield from reply.logs

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

    def get_nfts(
        self,
        blockchain: types.BlockchainNames,
        wallet_address: str,
        filter: Optional[List[Dict[str, List[str]]]] = None,
        **kwargs: Any,
    ) -> Iterable[types.Nft]:
        for reply in self.provider.call_method_paginated(
            "ankr_getNFTsByOwner",
            types.GetNFTsByOwnerRequest(
                blockchain=blockchain,
                wallet_address=wallet_address,
                filter=filter,
                **kwargs,
            ),
            types.GetNFTsByOwnerReply,
        ):
            yield from reply.assets
