from __future__ import annotations

from typing import Any, Iterable, List, Optional, Type, TypeVar, Union

from eth_typing import URI
from typing_extensions import Protocol
from web3 import HTTPProvider
from web3.types import RPCEndpoint, RPCResponse

from ankr import types
from ankr.exceptions import APIError

TRequest = TypeVar("TRequest", bound=types.RPCModel)
TReply = TypeVar("TReply")
TRequestPaginated = TypeVar("TRequestPaginated", bound=types.RPCRequestPaginated)
TReplyPaginated = TypeVar("TReplyPaginated", bound=types.RPCReplyPaginated)


class MultichainHTTPProvider(HTTPProvider):
    def __init__(
        self,
        api_key: str,
        endpoint_uri: Optional[Union[URI, str]] = None,
        request_kwargs: Optional[Any] = None,
        session: Optional[Any] = None,
    ) -> None:
        endpoint_uri = endpoint_uri or "https://rpc.ankr.com/multichain/"
        super().__init__(endpoint_uri + api_key, request_kwargs, session)

    def make_request(self, method: RPCEndpoint, params: Any) -> RPCResponse:
        response = super().make_request(method, params)
        if response.get("error"):
            raise APIError(response["error"])
        if "result" not in response:
            raise APIError("returned no result")
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
        *,
        method: str,
        request_params: Any,
        reply_type: Any,
        iterable_name: str,
        iterable_type: Any,
        limit: Optional[int] = None,
        call_function = Any,
        body_type : Any,
    ) -> Iterable[TReply]:
        # request_dict = request.dict(by_alias=True, exclude_none=True)

        # request_dict = {key: value for key, value in request.__dict__.items() if value is not None}


        body = body_type(
            id=1,
            jsonrpc="2.0",
            method=method,
            params=request_params
        )

        response = call_function(body=body)
        reply = response.get("result", {})

        items: List[Any] = reply.get(iterable_name, []) if isinstance(reply, dict) else []

        if limit:
            if limit <= len(items):
                yield from items[:limit]
                return
            limit -= len(items)

        yield from items

        if reply['nextPageToken']:
            request_params.page_token = reply['nextPageToken']
            yield from self.call_method_paginated(
                method=method,
                request_params=request_params,
                reply_type=reply_type,
                iterable_name=iterable_name,
                iterable_type=iterable_type,
                limit=limit,
                call_function=call_function,
                body_type=body_type
            )


class TProviderConstructor(Protocol):
    def __call__(
        self, api_key: Optional[str] = None, request_kwargs: Optional[Any] = None
    ) -> HTTPProvider:
        ...


def http_provider_constructor(url: str) -> TProviderConstructor:
    def init(
        api_key: Optional[str] = None,
        request_kwargs: Optional[Any] = None,
    ) -> HTTPProvider:
        if api_key is None:
            api_key = ""
        return HTTPProvider(f"{url}/{api_key}", request_kwargs)

    return init


# EVM
ArbitrumHTTPProvider = http_provider_constructor("https://rpc.ankr.com/arbitrum")
AvalancheHTTPProvider = http_provider_constructor("https://rpc.ankr.com/avalanche")
BscHTTPProvider = http_provider_constructor("https://rpc.ankr.com/bsc")
CeloHTTPProvider = http_provider_constructor("https://rpc.ankr.com/celo")
EthHTTPProvider = http_provider_constructor("https://rpc.ankr.com/eth")
FantomHTTPProvider = http_provider_constructor("https://rpc.ankr.com/fantom")
GnosisHTTPProvider = http_provider_constructor("https://rpc.ankr.com/gnosis")
HarmonyHTTPProvider = http_provider_constructor("https://rpc.ankr.com/harmony")
IotexHTTPProvider = http_provider_constructor("https://rpc.ankr.com/iotex")
MoonbeamHTTPProvider = http_provider_constructor("https://rpc.ankr.com/moonbeam")
NervosHTTPProvider = http_provider_constructor("https://rpc.ankr.com/nervos")
OptimismHTTPProvider = http_provider_constructor("https://rpc.ankr.com/optimism")
PolygonHTTPProvider = http_provider_constructor("https://rpc.ankr.com/polygon")
SyscoinHTTPProvider = http_provider_constructor("https://rpc.ankr.com/syscoin")

# Non-EVM
NearHTTPProvider = http_provider_constructor("https://rpc.ankr.com/near")
SolanaHTTPProvider = http_provider_constructor("https://rpc.ankr.com/solana")
