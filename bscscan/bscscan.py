import json
import warnings
from importlib import resources

from requests import Session

import bscscan
from bscscan import configs
from bscscan.enums.fields_enum import FieldsEnum as fields
from bscscan.enums.warnings_enum import WarningsEnum as Warnings
from bscscan.utils.parsing import ResponseParser as parser

CONFIG_FILE = "stable.json"


class BscScan:
    def __init__(self, api_key: str, suppress_warnings=False):
        if not suppress_warnings:
            warnings.warn(Warnings.CONTEXT_MANAGER_WARNING)
        self.__api_key = api_key

    @staticmethod
    def __load_config(config_path: str) -> dict:
        with open(config_path, "r") as f:
            return json.load(f)

    def __build(self, config: dict):
        for func, v in config.items():
            if not func.startswith("_"):  # disabled if _
                attr = getattr(getattr(bscscan, v["module"]), func)
                setattr(self, func, self.__run(attr))

    def __run(self, func):
        def wrapper(*args, **kwargs):
            url = (
                f"{fields.PREFIX}"
                f"{func(*args, **kwargs)}"
                f"{fields.API_KEY}"
                f"{self.__api_key}"
            )
            with self.__session.get(url) as response:
                return parser.parse(response.json())

        return wrapper

    def __enter__(self):
        self.__session = Session()
        with resources.path(configs, CONFIG_FILE) as path:
            self.__build(self.__load_config(str(path)))
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__session.close()
