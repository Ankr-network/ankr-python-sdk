from __future__ import annotations

from typing import Any, Iterable, List, Optional, Type, Union

from eth_typing import URI
from typing_extensions import Protocol
from web3 import HTTPProvider
from web3.types import RPCEndpoint, RPCResponse
from ankr.exceptions import APIError


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

    def clean_nones(self, value):
        """
        Recursively remove all None values from dictionaries and lists, and returns
        the result as a new dictionary or list.
        """
        if isinstance(value, list):
            return [self.clean_nones(x) for x in value if x is not None]
        elif isinstance(value, dict):
            return {
                key: self.clean_nones(val)
                for key, val in value.items()
                if val is not None
            }
        else:
            return value

    def make_request(self, method: RPCEndpoint, params: Any) -> RPCResponse:
        response = super().make_request(
            method, self.clean_nones(params.to_dict().copy())
        )
        if response.get("error"):
            raise APIError(response["error"])
        if "result" not in response:
            raise APIError("returned no result")
        return response

    def call_method(
        self,
        rpc: str,
        request: Any,
        reply: Any,
    ) -> Any:
        response = self.make_request(RPCEndpoint(rpc), request)
        reply = reply.from_dict(**response["result"])
        return reply

    def call_method_paginated(
        self,
        *,
        rpc: str,
        request: Any,
        reply: Any,
        iterable_name: str,
        iterable_type: Type[Any],
        limit: Optional[int] = None,
    ) -> Iterable[Any]:
        response = self.make_request(RPCEndpoint(rpc), request)
        reply = reply.from_dict(**response["result"])

        items: List[Any] = getattr(reply, iterable_name) or []

        if limit:
            if limit <= len(items):
                yield from items[:limit]
                return
            limit -= len(items)

        yield from items

        if reply.nextPageToken:
            request.pageToken = reply.nextPageToken
            yield from self.call_method_paginated(
                rpc=RPCEndpoint(rpc),
                request=request,
                reply=reply,
                iterable_name=iterable_name,
                iterable_type=iterable_type,
                limit=limit,
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
