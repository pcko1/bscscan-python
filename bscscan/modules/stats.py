from bscscan.enums.actions_enum import ActionsEnum as actions
from bscscan.enums.fields_enum import FieldsEnum as fields
from bscscan.enums.modules_enum import ModulesEnum as modules


class Stats:
    @staticmethod
    def get_total_bnb_supply():
        """Get total supply of BNB on Binance Smart Chain.

        Returns:
            str: The total supply of BNB.

        Example:
            Args:
                def get_total_bnb_supply(

                )

            Returns:
                "17673568869449800000000000"

        """
        return (
            f"{fields.MODULE}"
            f"{modules.STATS}"
            f"{fields.ACTION}"
            f"{actions.BNB_SUPPLY}"
        )

    @staticmethod
    def get_validators_list():
        """Get list of validators on Binance Smart Chain.

        Returns:
            List[dict]: All validators as a list of dictionaries.

        Example:
            Args:
                get_validators_list(

                )

            Returns:
                [
                    {
                        "validatorAddress": "0x9f8ccdafcc39f3c7d6ebf637c9151673cbc36b88",
                        "validatorName": "",
                        "validatorStatus": "0",
                        "validatorVotingPower": "43379676392570",
                        "validatorVotingPowerProportion": "0.0617"
                    },
                    {
                        "validatorAddress": "0x2465176c461afb316ebc773c61faee85a6515daa",
                        "validatorName": "",
                        "validatorStatus": "0",
                        "validatorVotingPower": "38039845465042",
                        "validatorVotingPowerProportion": "0.0541"
                    },

                    ...
                ]
        """
        return (
            f"{fields.MODULE}"
            f"{modules.STATS}"
            f"{fields.ACTION}"
            f"{actions.VALIDATORS}"
        )
