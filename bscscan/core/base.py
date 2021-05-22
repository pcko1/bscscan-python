import json
from importlib import resources

from bscscan import configs

CONFIG_FILE = "stable.json"


class BaseClient:
    def __init__(
        self,
        api_key: str,
        debug: bool = False,  # display generated URLs for debugging purposes
    ):
        self._config = self._load_config()
        self._api_key = api_key
        self._debug = debug

    @staticmethod
    def _load_config(config_file: str = CONFIG_FILE) -> dict:
        with resources.path(configs, config_file) as path:
            with open(path, "r") as f:
                return json.load(f)
