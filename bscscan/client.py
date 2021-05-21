from bscscan.core.async_client import AsyncClient
from bscscan.core.base import BaseClient
from bscscan.core.sync_client import SyncClient


class BscScan:
    """Client factory."""

    def __new__(cls, api_key: str, asynchronous=True) -> BaseClient:
        if asynchronous:
            return AsyncClient(api_key=api_key)
        else:
            return SyncClient(api_key=api_key)
