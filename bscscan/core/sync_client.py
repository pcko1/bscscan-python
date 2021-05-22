import bscscan
from bscscan.core.base import BaseClient
from bscscan.enums.fields_enum import FieldsEnum as fields
from bscscan.utils.parsing import ResponseParser as parser
from requests import Session


class SyncClient(BaseClient):
    def _build(self):
        for func, v in self._config.items():
            if not func.startswith("_"):  # disabled if _
                attr = getattr(getattr(bscscan, v["module"]), func)
                setattr(self, func, self._exec(attr))
        return self

    def _exec(self, func):
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
        return self._build()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._session.close()

    @classmethod
    def from_session(cls, api_key: str, session: Session):
        client = SyncClient(api_key)
        client._session = session
        return client._build()