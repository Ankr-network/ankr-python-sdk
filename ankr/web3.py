from __future__ import annotations

from typing import Any, Dict, Optional, Sequence, Type, Union, cast

from ens import ENS
from web3 import Web3
from web3._utils.empty import empty
from web3.eth import Eth
from web3.middleware import geth_poa_middleware
from web3.module import Module

from ankr.advanced_apis import (
    AnkrNFTAPI,
    AnkrQueryAPI,
    AnkrTokenAPI,
    AnkrEarlyAccessAPI,
)
from ankr.providers import (
    ArbitrumHTTPProvider,
    AvalancheHTTPProvider,
    BscHTTPProvider,
    CeloHTTPProvider,
    EthHTTPProvider,
    FantomHTTPProvider,
    GnosisHTTPProvider,
    HarmonyHTTPProvider,
    IotexHTTPProvider,
    MoonbeamHTTPProvider,
    NervosHTTPProvider,
    OptimismHTTPProvider,
    PolygonHTTPProvider,
    SyscoinHTTPProvider,
    TProviderConstructor,
)


class _Web3NamedMeta(type):
    def __new__(metacls, name, bases, namespace, **kw):  # type: ignore
        return super().__new__(metacls, "Web3", bases, namespace, **kw)


class AnkrWeb3(Web3, metaclass=_Web3NamedMeta):
    query: AnkrQueryAPI
    token: AnkrTokenAPI
    nft: AnkrNFTAPI

    eth: Eth
    arbitrum: Eth
    avalanche: Eth
    bsc: Eth
    celo: Eth
    fantom: Eth
    gnosis: Eth
    harmony: Eth
    iotex: Eth
    moonbeam: Eth
    nervos: Eth
    optimism: Eth
    polygon: Eth
    syscoin: Eth

    def __init__(
        self,
        api_key: str,
        request_kwargs: Optional[Any] = None,
        middlewares: Optional[Sequence[Any]] = None,
        modules: Optional[Dict[str, Union[Type[Module], Sequence[Any]]]] = None,
        external_modules: Optional[
            Dict[str, Union[Type[Module], Sequence[Any]]]
        ] = None,
        ens: ENS = cast(ENS, empty),
    ) -> None:
        self.__api_key = api_key
        self.__request_kwargs = request_kwargs
        self.__middlewares = middlewares
        self.__modules = modules
        self.__external_modules = external_modules
        self.__ens = ens

        self.early = AnkrEarlyAccessAPI(api_key)
        self.query = AnkrQueryAPI(api_key)
        self.token = AnkrTokenAPI(api_key)
        self.nft = AnkrNFTAPI(api_key)

        eth_provider = EthHTTPProvider(api_key, request_kwargs)
        super().__init__(eth_provider, middlewares, modules, external_modules, ens)
        self.arbitrum = self.__new_evm_chain(ArbitrumHTTPProvider)
        self.avalanche = self.__new_evm_chain(AvalancheHTTPProvider)
        self.bsc = self.__new_evm_chain(BscHTTPProvider)
        self.celo = self.__new_evm_chain(CeloHTTPProvider)
        self.fantom = self.__new_evm_chain(FantomHTTPProvider)
        self.gnosis = self.__new_evm_chain(GnosisHTTPProvider)
        self.harmony = self.__new_evm_chain(HarmonyHTTPProvider)
        self.iotex = self.__new_evm_chain(IotexHTTPProvider)
        self.moonbeam = self.__new_evm_chain(MoonbeamHTTPProvider)
        self.nervos = self.__new_evm_chain(NervosHTTPProvider)
        self.optimism = self.__new_evm_chain(OptimismHTTPProvider)
        self.polygon = self.__new_evm_chain(PolygonHTTPProvider)
        self.syscoin = self.__new_evm_chain(SyscoinHTTPProvider)

    def __new_evm_chain(self, provider: TProviderConstructor) -> Eth:
        w3 = Web3(
            provider(self.__api_key, self.__request_kwargs),
            self.__middlewares,
            self.__modules,
            self.__external_modules,
            self.__ens,
        )
        w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        return w3.eth
