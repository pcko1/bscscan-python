from bscscan.enums.actions_enum import ActionsEnum as actions
from bscscan.enums.fields_enum import FieldsEnum as fields
from bscscan.enums.modules_enum import ModulesEnum as modules


class Transactions:
    @staticmethod
    def get_tx_receipt_status(txhash: str):
        """Check the status of a transaction receipt.

        Args:
            txhash (str): Target tx hash.

        Returns:
            str: The status code.

        Example::

            from bscscan import AsyncBscScan

            with AsyncBscScan(YOUR_API_KEY) as client:
                print(
                    await get_tx_receipt_status(
                        txhash="0xe9975702518c79caf81d5da65dea689dcac701fcdd063f848d4f03c85392fd00"
                        )
                    )

            "1"
        """
        return (
            f"{fields.MODULE}"
            f"{modules.TRANSACTION}"
            f"{fields.ACTION}"
            f"{actions.GET_TX_RECEIPT_STATUS}"
            f"{fields.TXHASH}"
            f"{txhash}"
        )