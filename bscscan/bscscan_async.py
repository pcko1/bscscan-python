import json
import warnings
from importlib import resources

from aiohttp import ClientSession as Session

import bscscan
from bscscan import configs
from bscscan.enums.fields_enum import FieldsEnum as fields
from bscscan.enums.warnings_enum import WarningsEnum as Warnings
from bscscan.utils.parsing import ResponseParser as parser

CONFIG_FILE = "stable.json"


class AsyncBscScan:
    def __init__(self, api_key: str, suppress_warnings=False):
        if not suppress_warnings:
            warnings.warn(Warnings.CONTEXT_MANAGER_WARNING)
        self.__api_key = api_key

    @staticmethod
    def __load_config(config_path: str) -> dict:
        with open(config_path, "r") as f:
            return json.load(f)

    async def __build(self, config: dict):
        for func, v in config.items():
            if not func.startswith("_"):  # disabled if _
                attr = getattr(getattr(bscscan, v["module"]), func)
                setattr(self, func, await self.__run(attr))

    async def __run(self, func):
        async def wrapper(*args, **kwargs):
            url = (
                f"{fields.PREFIX}"
                f"{func(*args, **kwargs)}"
                f"{fields.API_KEY}"
                f"{self.__api_key}"
            )
            async with self.__session.get(url) as response:
                return parser.parse(await response.json())

        return wrapper

    async def __aenter__(self):
        self.__session = Session()
        with resources.path(configs, CONFIG_FILE) as path:
            await self.__build(self.__load_config(str(path)))
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.__session.close()
