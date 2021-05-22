from bscscan.enums.actions_enum import ActionsEnum as actions
from bscscan.enums.fields_enum import FieldsEnum as fields
from bscscan.enums.modules_enum import ModulesEnum as modules


class Blocks:
    @staticmethod
    def get_block_reward_by_block_number(block_no: int):
        """Get block reward by block number.

        Args:
            block_no (int): Target block number.

        Returns:
            dict: Block reward as a dictionary of various data.

        Example::

            from bscscan import BscScan

            async with BscScan(YOUR_API_KEY) as client:
                print(
                    await client.get_block_reward_by_block_number(
                        block_no="2150000"
                    )
                )

        Results::

                {
                    "blockNumber": "2150000",
                    "timeStamp": "1605122780",
                    "blockMiner": "0xee01c3b1283aa067c58eab4709f85e99d46de5fe",
                    "blockReward": "12141249999983048",
                    "uncles": [],
                    "uncleInclusionReward": "0"
                }
        """
        return (
            f"{fields.MODULE}"
            f"{modules.BLOCK}"
            f"{fields.ACTION}"
            f"{actions.GET_BLOCK_REWARD}"
            f"{fields.BLOCKNO}"
            f"{block_no}"
        )

    @staticmethod
    def get_est_block_countdown_time_by_block_number(block_no: int):
        """Get estimated countdown time for a given block.

        Args:
            block_no (int): Target block number.

        Returns:
            dict: Countdown time in a dictionary of various data.

        Example::

            from bscscan import BscScan

            async with BscScan(YOUR_API_KEY) as client:
                print(
                    await client.get_est_block_countdown_time_by_block_number(
                        block_no="8000000"
                    )
                )

        Results::

                {
                    "CurrentBlock": "7584646",
                    "CountdownBlock": "8000000",
                    "RemainingBlock": "415354",
                    "EstimateTimeInSec": "1246077.0"
                }
        """
        return (
            f"{fields.MODULE}"
            f"{modules.BLOCK}"
            f"{fields.ACTION}"
            f"{actions.GET_BLOCK_COUNTDOWN}"
            f"{fields.BLOCKNO}"
            f"{block_no}"
        )

    @staticmethod
    def get_block_number_by_timestamp(timestamp: int, closest: str):
        """Get block number given a specific timestamp.

        NOTE: Supports UNIX timestamps in seconds.

        Args:
            timestamp (int): Target timestamp.
            closest (str): Closest block "before" or "after" target timestamp.

        Returns:
            str: Block number for requested timestamp.

        Example::

            from bscscan import BscScan

            async with BscScan(YOUR_API_KEY) as client:
                print(
                    await client.get_block_number_by_timestamp(
                        timestamp="1601510400",
                        closest="before"
                    )
                )

        Results::

            "946206"
        """
        assert closest in ["before", "after"], "Specify 'before' or 'after'."
        return (
            f"{fields.MODULE}"
            f"{modules.BLOCK}"
            f"{fields.ACTION}"
            f"{actions.GET_BLOCK_NUMBER_BY_TIME}"
            f"{fields.TIMESTAMP}"
            f"{timestamp}"
            f"{fields.CLOSEST}"
            f"{closest}"
        )
