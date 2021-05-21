from bscscan.enums.actions_enum import ActionsEnum as actions
from bscscan.enums.fields_enum import FieldsEnum as fields
from bscscan.enums.modules_enum import ModulesEnum as modules
from bscscan.enums.tags_enum import TagsEnum as tags


class Tokens:
    @staticmethod
    def get_total_supply_by_contract_address(contract_address: str):
        """Get total supply of token by its contract address.

        Args:
            contract_address (str): Target contract address.

        Returns:
            str: Total supply of token behind target contract.

        Example:
            Args:
                get_total_supply_by_contract_address(
                    contract_address="0xe9e7cea3dedca5984780bafc599bd69add087d56"
                )

            Returns:
                "4200999999996203280118545633"
        """
        return (
            f"{fields.MODULE}"
            f"{modules.STATS}"
            f"{fields.ACTION}"
            f"{actions.TOKEN_SUPPLY}"
            f"{fields.CONTRACT_ADDRESS}"
            f"{contract_address}"
        )

    @staticmethod
    def get_circulating_supply_by_contract_address(contract_address: str):
        """Get circulating supply of token by its contract address.

        Args:
            contract_address (str): Target contract address.

        Returns:
            str: Circulating supply of token behind target contract.

        Example:
            Args:
                get_circulating_supply_by_contract_address(
                    contract_address="0xe9e7cea3dedca5984780bafc599bd69add087d56"
                )

            Returns:
                "4086900168016026430118545633"
        """
        return (
            f"{fields.MODULE}"
            f"{modules.STATS}"
            f"{fields.ACTION}"
            f"{actions.TOKEN_CSUPPLY}"
            f"{fields.CONTRACT_ADDRESS}"
            f"{contract_address}"
        )

    @staticmethod
    def get_acc_balance_by_token_contract_address(contract_address: str, address: str):
        """Get account balance given a contract address.

        Args:
            contract_address (str): Target contract address.
            address (str): Target wallet address.

        Returns:
            str: The target token balance of target account.

        Example:
            Args:
                get_acc_balance_by_token_contract_address(
                    contract_address="0xe9e7cea3dedca5984780bafc599bd69add087d56",
                    address="0x89e73303049ee32919903c09e8de5629b84f59eb"
                )

            Returns:
                "0"
        """
        return (
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
