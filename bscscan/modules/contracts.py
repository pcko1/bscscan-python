from bscscan.enums.actions_enum import ActionsEnum as actions
from bscscan.enums.fields_enum import FieldsEnum as fields
from bscscan.enums.modules_enum import ModulesEnum as modules


class Contracts:
    @staticmethod
    def get_contract_abi(contract_address: str):
        """Get ABI for a specific contract, if uploaded.

        Args:
            contract_address (str): Target contract address.

        Returns:
            str: ABI as a string.

        Example::

            from bscscan import BscScan

            async with BscScan(YOUR_API_KEY) as client:
                print(
                    await client.get_contract_abi(
                        contract_address="0x0000000000000000000000000000000000001004"
                    )
                )

        Results::

            "[{\'inputs\':[],\'stateMutability\':\'nonpayable\',\'type\':\'constructor\'}, ...]"
        """
        return (
            f"{fields.MODULE}"
            f"{modules.CONTRACT}"
            f"{fields.ACTION}"
            f"{actions.GET_ABI}"
            f"{fields.ADDRESS}"
            f"{contract_address}"
        )

    @staticmethod
    def get_contract_source_code(contract_address: str):
        """Get source code for a specific contract, if uploaded.

        Args:
            contract_address (str): Target contract address.

        Returns:
            List[dict]: Source code in a list of dictionaries of various data.

        Example::

            from bscscan import BscScan

            async with BscScan(YOUR_API_KEY) as client:
                print(
                    await client.get_contract_source_code(
                        contract_address="0x0000000000000000000000000000000000001004"
                    )
                )

        Results::

            [
                {
                    "SourceCode": "// File: contracts/interface/IBEP20.sol\\r\\n\\r\\npragma...",
                    "ABI": "[{\'inputs\':[],\'stateMutability\':\'nonpayable\',...}]",
                    "ContractName": "TokenHub",
                    "CompilerVersion": "v0.6.4+commit.1dca32f3",
                    "OptimizationUsed": "1",
                    "Runs": "200",
                    "ConstructorArguments": "",
                    "EVMVersion": "Default",
                    "Library": "",
                    "LicenseType": "None",
                    "Proxy": "0",
                    "Implementation": "",
                    "SwarmSource": "ipfs://cf38311fc70c7842415f6e43694ca6a2795a904f0541302504db82e7675343ff"
                }
            ]
        """
        return (
            f"{fields.MODULE}"
            f"{modules.CONTRACT}"
            f"{fields.ACTION}"
            f"{actions.GET_SOURCE_CODE}"
            f"{fields.ADDRESS}"
            f"{contract_address}"
        )
