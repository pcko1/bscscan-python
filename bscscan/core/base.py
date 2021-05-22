import json
import warnings
from importlib import resources
from bscscan import configs
from bscscan.enums.warnings_enum import WarningsEnum as Warnings

CONFIG_FILE = "stable.json"


class BaseClient:
    def __init__(self, api_key: str, suppress_warnings=False):
        if not suppress_warnings:
            warnings.warn(Warnings.CONTEXT_MANAGER_WARNING)
        self._config = self._load_config()
        self._api_key = api_key

    @staticmethod
    def _load_config(config_file: str = CONFIG_FILE) -> dict:
        with resources.path(configs, config_file) as path:
            with open(path, "r") as f:
                return json.load(f)
