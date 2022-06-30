from typing import Union

from web3.types import RPCError


class AdvancedAPIException(Exception):
    def __init__(self, error: Union[RPCError, str]):
        super().__init__(f"Failed to handle request: {error}")
