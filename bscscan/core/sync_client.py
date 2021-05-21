from importlib import resources

import bscscan
from bscscan import configs
from bscscan.core.base import BaseClient
from bscscan.enums.fields_enum import FieldsEnum as fields
from bscscan.utils.parsing import ResponseParser as parser
from requests import Session

CONFIG_FILE = "stable.json"


class SyncClient(BaseClient):
    def _build(self, config: dict):
        for func, v in config.items():
            if not func.startswith("_"):  # disabled if _
                attr = getattr(getattr(bscscan, v["module"]), func)
                setattr(self, func, self._run(attr))

    def _run(self, func):
        def wrapper(*args, **kwargs):
            url = (
                f"{fields.PREFIX}"
                f"{func(*args, **kwargs)}"
                f"{fields.API_KEY}"
                f"{self._api_key}"
            )
            with self._session.get(url) as response:
                return parser.parse(response.json())

        return wrapper

    def __enter__(self):
        self._session = Session()
        with resources.path(configs, CONFIG_FILE) as path:
            self._build(self._load_config(str(path)))
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._session.close()
