from bscscan.core.async_client import AsyncClient
from bscscan.core.base import BaseClient
from bscscan.core.sync_client import SyncClient


class BscScan:
    """Client factory."""

    def __new__(cls, api_key: str, asynchronous=True, debug=False, timeout=None) -> BaseClient:
        """Create a new client.

        Args:
            api_key (str): Your BscScan.com API key.
            asynchronous (bool, optional): Whether client is async or not. Defaults to True.
            debug (bool, optional): Display generated URLs for debugging. Defaults to False.

        Returns:
            BaseClient: BscScan client.
        """
        if asynchronous:
            return AsyncClient(api_key=api_key, debug=debug, timeout=timeout)
        return SyncClient(api_key=api_key, debug=debug, timeout=timeout)
