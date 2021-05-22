from bscscan.enums.actions_enum import ActionsEnum as actions
from bscscan.enums.fields_enum import FieldsEnum as fields
from bscscan.enums.modules_enum import ModulesEnum as modules


class Logs:
    @staticmethod
    def get_logs(
        from_block: int,
        to_block: int,
        address: str,
        topic_0: str,
        topic_1: str = "",
        topic_2: str = "",
        topic_3: str = "",
        topic_0_1_opr: str = "",
        topic_1_2_opr: str = "",
        topic_2_3_opr: str = "",
        topic_0_2_opr: str = "",
        topic_0_3_opr: str = "",
        topic_1_3_opr: str = "",
    ):
        # NOTE: Only the first 1000 results are returned
        return (
            f"{fields.MODULE}"
            f"{modules.LOGS}"
            f"{fields.ACTION}"
            f"{actions.GET_LOGS}"
            f"{fields.FROM_BLOCK}"
            f"{from_block}"
            f"{fields.TO_BLOCK}"
            f"{to_block}"
            f"{fields.ADDRESS}"
            f"{address}"
            # topic 0
            f"{fields.TOPIC_0}"
            f"{topic_0}"
            #
            # Everything below is optional. If not provided by user, then
            # they remain empty and do not affect the tail of the url.
            #
            # topic 0_x operators
            f"{fields.TOPIC_0_1_OPR*bool(topic_0_1_opr)}"
            f"{topic_0_1_opr}"
            f"{fields.TOPIC_0_2_OPR*bool(topic_0_2_opr)}"
            f"{topic_0_2_opr}"
            f"{fields.TOPIC_0_3_OPR*bool(topic_0_3_opr)}"
            f"{topic_0_3_opr}"
            # topic 1
            f"{fields.TOPIC_1*bool(topic_1)}"
            f"{topic_1}"
            # topic 1_x operators
            f"{fields.TOPIC_1_2_OPR*bool(topic_1_2_opr)}"
            f"{topic_1_2_opr}"
            f"{fields.TOPIC_1_3_OPR*bool(topic_1_3_opr)}"
            f"{topic_1_3_opr}"
            # topic 2
            f"{fields.TOPIC_2*bool(topic_2)}"
            f"{topic_2}"
            # topic 2_x operators
            f"{fields.TOPIC_2_3_OPR*bool(topic_2_3_opr)}"
            f"{topic_2_3_opr}"
            # topic 3
            f"{fields.TOPIC_3*bool(topic_3)}"
            f"{topic_3}"
        )