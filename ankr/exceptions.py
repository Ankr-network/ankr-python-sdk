from __future__ import annotations

from web3.types import RPCError


class APIError(Exception):
    def __init__(self, error: RPCError | str) -> None:
        super().__init__(f"failed to handle request, {error}")
