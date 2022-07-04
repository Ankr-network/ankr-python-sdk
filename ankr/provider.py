from __future__ import annotations

from typing import Any, Iterable, Type, TypeVar

from eth_typing import URI
from web3 import HTTPProvider
from web3.types import RPCEndpoint, RPCResponse

from ankr import types
from ankr.exceptions import AdvancedAPIException

TRequest = TypeVar("TRequest", bound=types.RPCModel)
TReply = TypeVar("TReply", bound=types.RPCModel)
TRequestPaginated = TypeVar("TRequestPaginated", bound=types.RPCRequestPaginated)
TReplyPaginated = TypeVar("TReplyPaginated", bound=types.RPCReplyPaginated)


class AnkrProvider(HTTPProvider):
    def __init__(
        self,
        api_key: str = "",
        endpoint_uri: URI | str | None = None,
        request_kwargs: Any | None = None,
        session: Any = None,
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

    def call_method(
        self,
        rpc: str,
        request: TRequest,
        reply_type: Type[TReply],
    ) -> TReply:
        request_dict = request.dict(by_alias=True, exclude_none=True)
        response = self.make_request(RPCEndpoint(rpc), request_dict)
        reply = reply_type(**response["result"])
        return reply

    def call_method_paginated(
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
            yield from self.call_method_paginated(RPCEndpoint(rpc), request, reply_type)
