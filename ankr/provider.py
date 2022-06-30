from typing import (
    Optional,
    Union,
    Any,
    List,
    Iterable,
    TypeVar,
    Type,
    Dict,
)

from eth_typing import (
    URI,
)
from web3 import HTTPProvider
from web3.types import (
    RPCEndpoint,
    RPCResponse,
)

from ankr import types
from ankr.exceptions import AdvancedAPIException


TRequestPaginated = TypeVar("TRequestPaginated", bound=types.RequestPaginated)
TReplyPaginated = TypeVar("TReplyPaginated", bound=types.ReplyPaginated)


class AnkrProvider(HTTPProvider):
    def __init__(
        self,
        api_key: str = "",
        endpoint_uri: Optional[Union[URI, str]] = None,
        request_kwargs: Optional[Any] = None,
        session: Optional[Any] = None,
    ) -> None:
        if endpoint_uri is None:
            endpoint_uri = "https://rpc.ankr.com/multichain/"
        super().__init__(endpoint_uri + api_key, request_kwargs)

    def make_request(self, method: RPCEndpoint, params: Any) -> RPCResponse:
        response = super().make_request(method, params)
        if response.get("error"):
            raise AdvancedAPIException(response["error"])
        if "result" not in response:
            raise AdvancedAPIException("returned no result")
        return response

    def make_request_paginated(
        self,
        rpc: str,
        request: TRequestPaginated,
        reply_type: Type[TReplyPaginated],
    ) -> Iterable[TReplyPaginated]:
        request_dict = request.dict(by_alias=True, exclude_none=True)
        response = self.make_request(RPCEndpoint(rpc), request_dict)
        reply = reply_type(**response["result"])

        yield reply

        if reply.next_page_token:
            request.page_token = reply.next_page_token
            yield from self.make_request_paginated(
                RPCEndpoint(rpc), request, reply_type
            )


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
        for reply in self.provider.make_request_paginated(
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

    def get_nfts(
        self,
        blockchain: types.BlockchainNames,
        wallet_address: str,
        filter: Optional[List[Dict[str, List[str]]]] = None,
        **kwargs: Any,
    ) -> Iterable[types.Nft]:
        for reply in self.provider.make_request_paginated(
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
