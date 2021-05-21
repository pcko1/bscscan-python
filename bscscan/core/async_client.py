from importlib import resources

import bscscan
from aiohttp import ClientSession as Session
from bscscan import configs
from bscscan.core.base import BaseClient
from bscscan.enums.fields_enum import FieldsEnum as fields
from bscscan.utils.parsing import ResponseParser as parser

CONFIG_FILE = "stable.json"


class AsyncClient(BaseClient):
    async def _build(self, config: dict):
        for func, v in config.items():
            if not func.startswith("_"):  # disabled if _
                attr = getattr(getattr(bscscan, v["module"]), func)
                setattr(self, func, await self._run(attr))

    async def _run(self, func):
        async def wrapper(*args, **kwargs):
            url = (
                f"{fields.PREFIX}"
                f"{func(*args, **kwargs)}"
                f"{fields.API_KEY}"
                f"{self._api_key}"
            )
            async with self._session.get(url) as response:
                return parser.parse(await response.json())

        return wrapper

    async def __aenter__(self):
        self._session = Session()
        with resources.path(configs, CONFIG_FILE) as path:
            await self._build(self._load_config(str(path)))
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self._session.close()
