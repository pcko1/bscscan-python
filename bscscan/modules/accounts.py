from functools import reduce
from typing import List

from bscscan.enums.actions_enum import ActionsEnum as actions
from bscscan.enums.fields_enum import FieldsEnum as fields
from bscscan.enums.modules_enum import ModulesEnum as modules
from bscscan.enums.tags_enum import TagsEnum as tags


class Accounts:
    @staticmethod
    def get_bnb_balance(address: str):

        url = (
            f"{fields.MODULE}"
            f"{modules.ACCOUNT}"
            f"{fields.ACTION}"
            f"{actions.BALANCE}"
            f"{fields.ADDRESS}"
            f"{address}"
            f"{fields.TAG}"
            f"{tags.LATEST}"
        )
        return url

    @staticmethod
    def get_bnb_balance_multiple(addresses: List[str]):
        # NOTE: Max 20 wallets at a time
        address_list = reduce(lambda w1, w2: str(w1) + "," + str(w2), addresses)
        url = (
            f"{fields.MODULE}"
            f"{modules.ACCOUNT}"
            f"{fields.ACTION}"
            f"{actions.BALANCE_MULTI}"
            f"{fields.ADDRESS}"
            f"{address_list}"
            f"{fields.TAG}"
            f"{tags.LATEST}"
        )
        return url

    @staticmethod
    def get_normal_txs_by_address(
        address: str,
        startblock: int,
        endblock: int,
        sort: str,
    ):
        # NOTE: Returns the last 10k events
        url = (
            f"{fields.MODULE}"
            f"{modules.ACCOUNT}"
            f"{fields.ACTION}"
            f"{actions.TXLIST}"
            f"{fields.ADDRESS}"
            f"{address}"
            f"{fields.START_BLOCK}"
            f"{str(startblock)}"
            f"{fields.END_BLOCK}"
            f"{str(endblock)}"
            f"{fields.SORT}"
            f"{sort}"
        )
        return url

    @staticmethod
    def get_normal_txs_by_address_paginated(
        address: str,
        page: int,
        offset: int,
        startblock: int,
        endblock: int,
        sort: str,
    ):
        url = (
            f"{fields.MODULE}"
            f"{modules.ACCOUNT}"
            f"{fields.ACTION}"
            f"{actions.TXLIST}"
            f"{fields.ADDRESS}"
            f"{address}"
            f"{fields.START_BLOCK}"
            f"{str(startblock)}"
            f"{fields.END_BLOCK}"
            f"{str(endblock)}"
            f"{fields.SORT}"
            f"{sort}"
            f"{fields.PAGE}"
            f"{str(page)}"
            f"{fields.OFFSET}"
            f"{str(offset)}"
        )
        return url

    @staticmethod
    def get_internal_txs_by_address(
        address: str,
        startblock: int,
        endblock: int,
        sort: str,
    ):
        # NOTE: Returns the last 10k events
        url = (
            f"{fields.MODULE}"
            f"{modules.ACCOUNT}"
            f"{fields.ACTION}"
            f"{actions.TXLIST_INTERNAL}"
            f"{fields.ADDRESS}"
            f"{address}"
            f"{fields.START_BLOCK}"
            f"{str(startblock)}"
            f"{fields.END_BLOCK}"
            f"{str(endblock)}"
            f"{fields.SORT}"
            f"{sort}"
        )
        return url

    @staticmethod
    def get_internal_txs_by_address_paginated(
        address: str,
        page: int,
        offset: int,
        startblock: int,
        endblock: int,
        sort: str,
    ):
        url = (
            f"{fields.MODULE}"
            f"{modules.ACCOUNT}"
            f"{fields.ACTION}"
            f"{actions.TXLIST_INTERNAL}"
            f"{fields.ADDRESS}"
            f"{address}"
            f"{fields.START_BLOCK}"
            f"{str(startblock)}"
            f"{fields.END_BLOCK}"
            f"{str(endblock)}"
            f"{fields.SORT}"
            f"{sort}"
            f"{fields.PAGE}"
            f"{str(page)}"
            f"{fields.OFFSET}"
            f"{str(offset)}"
        )
        return url

    @staticmethod
    def get_internal_txs_by_txhash(txhash: str):
        # NOTE: Returns the last 10k events
        url = (
            f"{fields.MODULE}"
            f"{modules.ACCOUNT}"
            f"{fields.ACTION}"
            f"{actions.TXLIST_INTERNAL}"
            f"{fields.TXHASH}"
            f"{txhash}"
        )
        return url

    @staticmethod
    def get_internal_txs_by_block_range_paginated(
        startblock: int,
        endblock: int,
        page: int,
        offset: int,
        sort: str,
    ):
        # NOTE: Returns the last 10k events
        url = (
            f"{fields.MODULE}"
            f"{modules.ACCOUNT}"
            f"{fields.ACTION}"
            f"{actions.TXLIST_INTERNAL}"
            f"{fields.START_BLOCK}"
            f"{str(startblock)}"
            f"{fields.END_BLOCK}"
            f"{str(endblock)}"
            f"{fields.SORT}"
            f"{sort}"
            f"{fields.PAGE}"
            f"{str(page)}"
            f"{fields.OFFSET}"
            f"{str(offset)}"
        )
        return url

    @staticmethod
    def get_bep20_token_transfer_events_by_address(
        address: str,
        startblock: int,
        endblock: int,
        sort: str,
    ):
        # NOTE: Returns the last 10k events
        url = (
            f"{fields.MODULE}"
            f"{modules.ACCOUNT}"
            f"{fields.ACTION}"
            f"{actions.TOKENTX}"
            f"{fields.ADDRESS}"
            f"{address}"
            f"{fields.START_BLOCK}"
            f"{str(startblock)}"
            f"{fields.END_BLOCK}"
            f"{str(endblock)}"
            f"{fields.SORT}"
            f"{sort}"
        )
        return url

    @staticmethod
    def get_bep20_token_transfer_events_by_contract_address_paginated(
        contract_address: str, page: int, offset: int, sort: str
    ):

        url = (
            f"{fields.MODULE}"
            f"{modules.ACCOUNT}"
            f"{fields.ACTION}"
            f"{actions.TOKENTX}"
            f"{fields.CONTRACT_ADDRESS}"
            f"{contract_address}"
            f"{fields.SORT}"
            f"{sort}"
            f"{fields.PAGE}"
            f"{str(page)}"
            f"{fields.OFFSET}"
            f"{str(offset)}"
        )
        return url

    @staticmethod
    def get_bep20_token_transfer_events_by_address_and_contract_paginated(
        contract_address: str, address: str, page: int, offset: int, sort: str
    ):

        url = (
            f"{fields.MODULE}"
            f"{modules.ACCOUNT}"
            f"{fields.ACTION}"
            f"{actions.TOKENTX}"
            f"{fields.CONTRACT_ADDRESS}"
            f"{contract_address}"
            f"{fields.ADDRESS}"
            f"{address}"
            f"{fields.SORT}"
            f"{sort}"
            f"{fields.PAGE}"
            f"{str(page)}"
            f"{fields.OFFSET}"
            f"{str(offset)}"
        )
        return url

    @staticmethod
    def get_bep721_token_transfer_events_by_address(
        address: str,
        startblock: int,
        endblock: int,
        sort: str,
    ):
        url = (
            f"{fields.MODULE}"
            f"{modules.ACCOUNT}"
            f"{fields.ACTION}"
            f"{actions.TOKENNFTTX}"
            f"{fields.ADDRESS}"
            f"{address}"
            f"{fields.START_BLOCK}"
            f"{str(startblock)}"
            f"{fields.END_BLOCK}"
            f"{str(endblock)}"
            f"{fields.SORT}"
            f"{sort}"
        )
        return url

    @staticmethod
    def get_bep721_token_transfer_events_by_contract_address_paginated(
        contract_address: str, page: int, offset: int, sort: str
    ):
        url = (
            f"{fields.MODULE}"
            f"{modules.ACCOUNT}"
            f"{fields.ACTION}"
            f"{actions.TOKENNFTTX}"
            f"{fields.CONTRACT_ADDRESS}"
            f"{contract_address}"
            f"{fields.SORT}"
            f"{sort}"
            f"{fields.PAGE}"
            f"{str(page)}"
            f"{fields.OFFSET}"
            f"{str(offset)}"
        )
        return url

    @staticmethod
    def get_bep721_token_transfer_events_by_address_and_contract_paginated(
        contract_address: str, address: str, page: int, offset: int, sort: str
    ):
        url = (
            f"{fields.MODULE}"
            f"{modules.ACCOUNT}"
            f"{fields.ACTION}"
            f"{actions.TOKENNFTTX}"
            f"{fields.CONTRACT_ADDRESS}"
            f"{contract_address}"
            f"{fields.ADDRESS}"
            f"{address}"
            f"{fields.SORT}"
            f"{sort}"
            f"{fields.PAGE}"
            f"{str(page)}"
            f"{fields.OFFSET}"
            f"{str(offset)}"
        )
        return url

    @staticmethod
    def get_validated_blocks_by_address(address: str):
        url = (
            f"{fields.MODULE}"
            f"{modules.ACCOUNT}"
            f"{fields.ACTION}"
            f"{actions.GET_MINED_BLOCKS}"
            f"{fields.ADDRESS}"
            f"{address}"
            f"{fields.BLOCK_TYPE}"
            f"blocks"
        )
        return url

    @staticmethod
    def get_validated_blocks_by_address_paginated(address: str, page: int, offset: int):
        url = (
            f"{fields.MODULE}"
            f"{modules.ACCOUNT}"
            f"{fields.ACTION}"
            f"{actions.GET_MINED_BLOCKS}"
            f"{fields.ADDRESS}"
            f"{address}"
            f"{fields.BLOCK_TYPE}"
            f"blocks"
            f"{fields.PAGE}"
            f"{str(page)}"
            f"{fields.OFFSET}"
            f"{str(offset)}"
        )
        return url
