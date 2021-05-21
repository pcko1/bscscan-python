import json
import warnings

from bscscan.enums.warnings_enum import WarningsEnum as Warnings


class BaseClient:
    def __init__(self, api_key: str, suppress_warnings=False):
        if not suppress_warnings:
            warnings.warn(Warnings.CONTEXT_MANAGER_WARNING)
        self._api_key = api_key

    @staticmethod
    def _load_config(config_path: str) -> dict:
        with open(config_path, "r") as f:
            return json.load(f)
