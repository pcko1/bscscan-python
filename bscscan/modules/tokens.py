from bscscan.enums.actions_enum import ActionsEnum as actions
from bscscan.enums.fields_enum import FieldsEnum as fields
from bscscan.enums.modules_enum import ModulesEnum as modules
from bscscan.enums.tags_enum import TagsEnum as tags


class Tokens:
    @staticmethod
    def get_total_supply_by_contract_address(contract_address: str) -> str:
        url = (
            f"{fields.MODULE}"
            f"{modules.STATS}"
            f"{fields.ACTION}"
            f"{actions.TOKEN_SUPPLY}"
            f"{fields.CONTRACT_ADDRESS}"
            f"{contract_address}"
        )
        return url

    @staticmethod
    def get_circulating_supply_by_contract_address(contract_address: str) -> str:
        url = (
            f"{fields.MODULE}"
            f"{modules.STATS}"
            f"{fields.ACTION}"
            f"{actions.TOKEN_CSUPPLY}"
            f"{fields.CONTRACT_ADDRESS}"
            f"{contract_address}"
        )
        return url

    @staticmethod
    def get_acc_balance_by_token_contract_address(
        contract_address: str, address: str
    ) -> str:
        url = (
            f"{fields.MODULE}"
            f"{modules.ACCOUNT}"
            f"{fields.ACTION}"
            f"{actions.TOKEN_BALANCE}"
            f"{fields.CONTRACT_ADDRESS}"
            f"{contract_address}"
            f"{fields.ADDRESS}"
            f"{address}"
            f"{fields.TAG}"
            f"{tags.LATEST}"
        )
        return url
