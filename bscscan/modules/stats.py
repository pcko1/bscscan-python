from bscscan.enums.actions_enum import ActionsEnum as actions
from bscscan.enums.fields_enum import FieldsEnum as fields
from bscscan.enums.modules_enum import ModulesEnum as modules


class Stats:
    @staticmethod
    def get_total_bnb_supply() -> str:
        url = (
            f"{fields.MODULE}"
            f"{modules.STATS}"
            f"{fields.ACTION}"
            f"{actions.BNB_SUPPLY}"
        )
        return url

    @staticmethod
    def get_validators_list() -> str:
        url = (
            f"{fields.MODULE}"
            f"{modules.STATS}"
            f"{fields.ACTION}"
            f"{actions.VALIDATORS}"
        )
        return url
