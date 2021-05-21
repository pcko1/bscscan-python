from functools import reduce
from typing import List

from bscscan.enums.actions_enum import ActionsEnum as actions
from bscscan.enums.fields_enum import FieldsEnum as fields
from bscscan.enums.modules_enum import ModulesEnum as modules
from bscscan.enums.tags_enum import TagsEnum as tags


class Accounts:
    @staticmethod
    def get_bnb_balance(address: str):
        """Get the BNB balance of an account.

        Args:
            address (str): Target account.

        Returns:
            str: Its balance as a string. Must be manually cast to float.

        Example::

            from bscscan import AsyncBscScan

            async with AsyncBscScan(YOUR_API_KEY) as client:
                print(
                    await client.get_bnb_balance(
                        address="0x0000000000000000000000000000000000001004"
                        )
                )

        Results::

            "158732998695887136972460565"
        """

        return (
            f"{fields.MODULE}"
            f"{modules.ACCOUNT}"
            f"{fields.ACTION}"
            f"{actions.BALANCE}"
            f"{fields.ADDRESS}"
            f"{address}"
            f"{fields.TAG}"
            f"{tags.LATEST}"
        )

    @staticmethod
    def get_bnb_balance_multiple(addresses: List[str]):
        """Get the BNB balance of multiple accounts.

        **NOTE: Max 20 accounts per call are supported.**

        Args:
            addresses (List[str]): List of target accounts.

        Returns:
            List[dict]: Their balances in a list of dictionaries.

        Example::

            from bscscan import AsyncBscScan

            async with AsyncBscScan(YOUR_API_KEY) as client:
                print(
                    await client.get_bnb_balance_multiple(
                        addresses=[
                            "0x0000000000000000000000000000000000001004",
                            "0x63a9975ba31b0b9626b34300f7f627147df1f526",
                            "0x198ef1ec325a96cc354c7266a038be8b5c558f67"
                        ]
                    )
                )

        Results::

            [
                {
                    "account": "0x0000000000000000000000000000000000001004",
                    "balance": "158732998695887136972460565"
                },
                {
                    "account": "0x63a9975ba31b0b9626b34300f7f627147df1f526",
                    "balance": "0"
                },
                {
                    "account": "0x198ef1ec325a96cc354c7266a038be8b5c558f67",
                    "balance": "0"
                }
            ]
        """
        address_list = reduce(lambda w1, w2: str(w1) + "," + str(w2), addresses)
        return (
            f"{fields.MODULE}"
            f"{modules.ACCOUNT}"
            f"{fields.ACTION}"
            f"{actions.BALANCE_MULTI}"
            f"{fields.ADDRESS}"
            f"{address_list}"
            f"{fields.TAG}"
            f"{tags.LATEST}"
        )

    @staticmethod
    def get_normal_txs_by_address(
        address: str,
        startblock: int,
        endblock: int,
        sort: str,
    ):
        """Get a list of all normal transactions for an address.

        **NOTE: Returns the 10,000 most recent transactions.**

        Args:
            address (str): Target address.
            startblock (int): Start block of the query.
            endblock (int): End block of the query.
            sort (str): "asc" to return results in ascending order.

        Returns:
            List[dict]: A list of dictionaries of normal transactions.

        Example::

            from bscscan import AsyncBscScan

            async with AsyncBscScan(YOUR_API_KEY) as client:
                print(
                    await client.get_normal_txs_by_address(
                        address="0x35e7a025f4da968de7e4d7e4004197917f4070f1",
                        startblock=0,
                        endblock=99999999,
                        sort="asc"
                    )
                )

        Results::

            [
                {
                    "blockNumber": "3385",
                    "timeStamp": "1598681758",
                    "hash": "0xd638d39681335a703c9ed03d389c468e3ddaf74efbbc59f0be8b0217f1281df8",
                    "nonce": "0",
                    "blockHash": "0x51bdc4233991acedb25a895c8659f6fb7607dc40626a1dcb795e57ed7ed1a673",
                    "transactionIndex": "1",
                    "from": "0x35e7a025f4da968de7e4d7e4004197917f4070f1",
                    "to": "0x0000000000000000000000000000000000001002",
                    "value": "207350625000000",
                    "gas": "9223372036854775807",
                    "gasPrice": "0",
                    "isError": "0",
                    "txreceipt_status": "1",
                    "input": "0x",
                    "contractAddress": "",
                    "cumulativeGasUsed": "112103",
                    "gasUsed": "1516",
                    "confirmations": "7581257"
                },

                ...
            ]
        """
        return (
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

    @staticmethod
    def get_normal_txs_by_address_paginated(
        address: str,
        page: int,
        offset: int,
        startblock: int,
        endblock: int,
        sort: str,
    ):
        """Get a list of all normal transactions for an address as numbered pages.

        Args:
            address (str): Target address.
            page (int): Page number to fetch.
            offset (int): Max records to return.
            startblock (int): Start block of the query.
            endblock (int): End block of the query.
            sort (str): "asc" to return results in ascending order.

        Returns:
            List[dict]: All transactions on requested page as a list of dictionaries.

        Example::

            from bscscan import AsyncBscScan

            async with AsyncBscScan(YOUR_API_KEY) as client:
                print(
                    await client.get_normal_txs_by_address_paginated(
                        address="0x35e7a025f4da968de7e4d7e4004197917f4070f1",
                        startblock=0,
                        endblock=99999999,
                        page=1,
                        offset=10,
                        sort="asc",
                    )
                )

        Results::

            [
                {
                    "blockNumber": "3385",
                    "timeStamp": "1598681758",
                    "hash": "0xd638d39681335a703c9ed03d389c468e3ddaf74efbbc59f0be8b0217f1281df8",
                    "nonce": "0",
                    "blockHash": "0x51bdc4233991acedb25a895c8659f6fb7607dc40626a1dcb795e57ed7ed1a673",
                    "transactionIndex": "1",
                    "from": "0x35e7a025f4da968de7e4d7e4004197917f4070f1",
                    "to": "0x0000000000000000000000000000000000001002",
                    "value": "207350625000000",
                    "gas": "9223372036854775807",
                    "gasPrice": "0",
                    "isError": "0",
                    "txreceipt_status": "1",
                    "input": "0x",
                    "contractAddress": "",
                    "cumulativeGasUsed": "112103",
                    "gasUsed": "1516",
                    "confirmations": "7581258"
                },

                ...
            ]
        """
        return (
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

    @staticmethod
    def get_internal_txs_by_address(
        address: str,
        startblock: int,
        endblock: int,
        sort: str,
    ):
        """Get a list of all internal transactions for an address.

        **NOTE: Returns the 10,000 most recent transactions.**

        Args:
            address (str): Target address.
            startblock (int): Start block of the query.
            endblock (int): End block of the query.
            sort (str): "asc" to return results in ascending order.

        Returns:
            List[dict]: A list of dictionaries of internal transactions.

        Example::

            from bscscan import AsyncBscScan

            async with AsyncBscScan(YOUR_API_KEY) as client:
                print(
                    await client.get_internal_txs_by_address(
                        address="0x0000000000000000000000000000000000001004",
                        startblock=0,
                        endblock=2702578,
                        sort="asc"
                    )
                )

        Results::

            [
                {
                    "blockNumber": "958",
                    "timeStamp": "1598674477",
                    "hash": "0x4d74a6fc84d57f18b8e1dfa07ee517c4feb296d16a8353ee41adc03669982028",
                    "from": "0x0000000000000000000000000000000000001004",
                    "to": "0x4e656459ed25bf986eea1196bc1b00665401645d",
                    "value": "100000000000000",
                    "contractAddress": "",
                    "input": "",
                    "type": "call",
                    "gas": "12300",
                    "gasUsed": "0",
                    "traceId": "0_1_1",
                    "isError": "0",
                    "errCode": ""
                },

                ...
            ]
        """
        return (
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

    @staticmethod
    def get_internal_txs_by_address_paginated(
        address: str,
        page: int,
        offset: int,
        startblock: int,
        endblock: int,
        sort: str,
    ):
        """Get a list of all internal transactions for an address as numbered pages.

        Args:
            address (str): Target address.
            page (int): Page number to fetch.
            offset (int): Max records to return.
            startblock (int): Start block of the query.
            endblock (int): End block of the query.
            sort (str): "asc" to return results in ascending order.

        Returns:
            List[dict]: All transactions on requested page as a list of dictionaries.

        Example::

            from bscscan import AsyncBscScan

            async with AsyncBscScan(YOUR_API_KEY) as client:
                print(
                    await client.get_internal_txs_by_address_paginated(
                        address="0x0000000000000000000000000000000000001004",
                        startblock=0,
                        endblock=2702578,
                        page=1,
                        offset=10,
                        sort="asc",
                    )
                )

        Results::

            [
                {
                    "blockNumber": "958",
                    "timeStamp": "1598674477",
                    "hash": "0x4d74a6fc84d57f18b8e1dfa07ee517c4feb296d16a8353ee41adc03669982028",
                    "from": "0x0000000000000000000000000000000000001004",
                    "to": "0x4e656459ed25bf986eea1196bc1b00665401645d",
                    "value": "100000000000000",
                    "contractAddress": "",
                    "input": "",
                    "type": "call",
                    "gas": "12300",
                    "gasUsed": "0",
                    "traceId": "0_1_1",
                    "isError": "0",
                    "errCode": ""
                },

                ...
            ]
        """
        return (
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

    @staticmethod
    def get_internal_txs_by_txhash(txhash: str):
        """Get all internal transactions given for a tx hash.

        **NOTE: Returns the 10,000 most recent transactions.**

        Args:
            txhash (str): Target tx hash.

        Returns:
            List[dict]: All internal transactions as a list of dictionaries.

        Example::

            from bscscan import AsyncBscScan

            async with AsyncBscScan(YOUR_API_KEY) as client:
                print(
                    await client.get_internal_txs_by_txhash(
                        txhash="0x6dbc8f3e1ba98c63463b19ebef957ccd842db274ed499a54f2cdde8499604d54"
                    )
                )

            [
                {
                    "blockNumber": "5012927",
                    "timeStamp": "1613725978",
                    "from": "0xcde540d7eafe93ac5fe6233bee57e1270d3e330f",
                    "to": "0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c",
                    "value": "21820550428160139857",
                    "contractAddress": "",
                    "input": "",
                    "type": "call",
                    "gas": "117864",
                    "gasUsed": "22674",
                    "isError": "0",
                    "errCode": ""
                },

        Results::

                ...
            ]
        """
        return (
            f"{fields.MODULE}"
            f"{modules.ACCOUNT}"
            f"{fields.ACTION}"
            f"{actions.TXLIST_INTERNAL}"
            f"{fields.TXHASH}"
            f"{txhash}"
        )

    @staticmethod
    def get_internal_txs_by_block_range_paginated(
        startblock: int,
        endblock: int,
        page: int,
        offset: int,
        sort: str,
    ):
        """Get all internal transactions given for a given block range as numbered pages.

        **NOTE: Returns the 10,000 most recent transactions.**

        Args:
            startblock (int): Start block of the query.
            endblock (int): End block of the query.
            page (int): Page number to fetch.
            offset (int): Max records to return.
            sort (str): "asc" to return results in ascending order.

        Returns:
            List[dict]: All internal transactions as a list of dictionaries.

        Example::

            from bscscan import AsyncBscScan

            async with AsyncBscScan(YOUR_API_KEY) as client:
                print(
                    await client.get_internal_txs_by_block_range_paginated(
                        startblock=0,
                        endblock=2702578,
                        page=1,
                        offset=10,
                        sort="asc"
                    )
                )

        Results::

            [
                {
                "blockNumber": "958",
                "timeStamp": "1598674477",
                "hash": "0x4d74a6fc84d57f18b8e1dfa07ee517c4feb296d16a8353ee41adc03669982028",
                "from": "0x0000000000000000000000000000000000001004",
                "to": "0x4e656459ed25bf986eea1196bc1b00665401645d",
                "value": "100000000000000",
                "contractAddress": "",
                "input": "",
                "type": "call",
                "gas": "12300",
                "gasUsed": "0",
                "traceId": "0_1_1",
                "isError": "0",
                "errCode": ""
                },

                ...
            ]

        """
        return (
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

    @staticmethod
    def get_bep20_token_transfer_events_by_address(
        address: str,
        startblock: int,
        endblock: int,
        sort: str,
    ):
        """Get all BEP20 token transfer events for a given address.

        **NOTE: Returns the 10,000 most recent events.**

        Args:
            address (str): Target address.
            startblock (int): Start block of the query.
            endblock (int): End block of the query.
            sort (str): "asc" to return results in ascending order.

        Returns:
            List[dict]: All token transfers for target address.

        Example::

            from bscscan import AsyncBscScan

            async with AsyncBscScan(YOUR_API_KEY) as client:
                print(
                    await client.get_bep20_token_transfer_events_by_address(
                        address="0x63aea877b5d5fa234a1532f1b26a4f6d9051866e",
                        startblock=0,
                        endblock=999999999,
                        sort="asc"
                    )
                )

        Results::

            [
                {
                    "blockNumber": "4387931",
                    "timeStamp": "1611843685",
                    "hash": "0x9603a00eaad4572fc03aae6ce4e64d129767752da95f53e3f726ad4ed86a843e",
                    "nonce": "0",
                    "blockHash": "0x33667c5034de6cb748e2d746b31b21f2c90dc20e8b670658bbb1c2201ced17f3",
                    "from": "0x7be44b47c12761eab1b80b5779638fb09165c743",
                    "contractAddress": "0xe9e7cea3dedca5984780bafc599bd69add087d56",
                    "to": "0x63aea877b5d5fa234a1532f1b26a4f6d9051866e",
                    "value": "42265483120736185167",
                    "tokenName": "Binance-Peg BUSD Token",
                    "tokenSymbol": "BUSD",
                    "tokenDecimal": "18",
                    "transactionIndex": "8",
                    "gas": "411698",
                    "gasPrice": "20000000000",
                    "gasUsed": "286489",
                    "cumulativeGasUsed": "1154025",
                    "input": "deprecated",
                    "confirmations": "3196712"
                },

                ...
            ]
        """

        return (
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

    @staticmethod
    def get_bep20_token_transfer_events_by_contract_address_paginated(
        contract_address: str, page: int, offset: int, sort: str
    ):
        """Get all token transfer events for a given BEP20 contract as numbered pages.

        **NOTE: Returns the 10,000 most recent events.**

        Args:
            contract_address (str): Target contract address.
            page (int): Page number to fetch.
            offset (int): Max records to return.
            sort (str): "asc" to return results in ascending order.

        Returns:
            List[dict]: All token transfers for target contract address.

        Example::

            from bscscan import AsyncBscScan

            async with AsyncBscScan(YOUR_API_KEY) as client:
                print(
                    await client.get_bep20_token_transfer_events_by_contract_address_paginated(
                        contract_address="0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c",
                        page=1,
                        offset=100,
                        sort="asc"
                    )
                )

        Results::

            [
                {
                    "blockNumber": "188549",
                    "timeStamp": "1599237427",
                    "hash": "0x817585be21abae212524b1f86fb0c6ceaff0048ae4a29739108476b2ca06290e",
                    "nonce": "16",
                    "blockHash": "0x499c458e0ba984af9a2d1a188e2ba36c117f7a7eeba7ee23471e85b01653e10c",
                    "from": "0x72af20bdae54756576b3725e73b75391e599a191",
                    "contractAddress": "0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c",
                    "to": "0x72af20bdae54756576b3725e73b75391e599a191",
                    "value": "10000000000000000",
                    "tokenName": "Wrapped BNB",
                    "tokenSymbol": "WBNB",
                    "tokenDecimal": "18",
                    "transactionIndex": "0",
                    "gas": "45614",
                    "gasPrice": "22000000000",
                    "gasUsed": "28382",
                    "cumulativeGasUsed": "28382",
                    "input": "deprecated",
                    "confirmations": "7396096"
                },

                ...
            ]
        """
        return (
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

    @staticmethod
    def get_bep20_token_transfer_events_by_address_and_contract_paginated(
        contract_address: str, address: str, page: int, offset: int, sort: str
    ):
        """Get all token transfers for a given BEP20 contract and wallet as numbered pages.

        Args:
            contract_address (str): Target contract address.
            address (str): Target wallet address.
            page (int): Page number to fetch.
            offset (int): Max records to return.
            sort (str): "asc" to return results in ascending order.

        Returns:
            List[dict]: All token transfers as a list of dictionaries.

        Example::

            from bscscan import AsyncBscScan

            async with AsyncBscScan(YOUR_API_KEY) as client:
                print(
                    await client.get_bep20_token_transfer_events_by_address_and_contract_paginated(
                        "contract_address": "0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c",
                        "address": "0x63aea877b5d5fa234a1532f1b26a4f6d9051866e",
                        "page": 1,
                        "offset": 100,
                        "sort": "asc"
                    )
                )

        Results::

            [
                {
                    "blockNumber": "4505611",
                    "timeStamp": "1612197293",
                    "hash": "0x3ac8603f421ccc08e198e4d06f05b8b31dc76b747369d78f3e7fa489f4692c44",
                    "nonce": "43",
                    "blockHash": "0x3ea200d5770ce8fcfa17754fad9143c77ab9ef5c3a5bd9ceb18c13a40ec6e926",
                    "from": "0x7be44b47c12761eab1b80b5779638fb09165c743",
                    "contractAddress": "0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c",
                    "to": "0x63aea877b5d5fa234a1532f1b26a4f6d9051866e",
                    "value": "98000000000000000000",
                    "tokenName": "Wrapped BNB",
                    "tokenSymbol": "WBNB",
                    "tokenDecimal": "18",
                    "transactionIndex": "127",
                    "gas": "209173",
                    "gasPrice": "20000000000",
                    "gasUsed": "130773",
                    "cumulativeGasUsed": "6294816",
                    "input": "deprecated",
                    "confirmations": "3079034"
                },

                ...
            ]
        """

        return (
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

    @staticmethod
    def get_bep721_token_transfer_events_by_address(
        address: str,
        startblock: int,
        endblock: int,
        sort: str,
    ):
        """Get all BEP721 token transfer events for a given address.

        **NOTE: Returns the 10,000 most recent events.**

        Args:
            address (str): Target address.
            startblock (int): Start block of the query.
            endblock (int): End block of the query.
            sort (str): "asc" to return results in ascending order.

        Returns:
            List[dict]: All token transfers for target address.

        Example::

            from bscscan import AsyncBscScan

            async with AsyncBscScan(YOUR_API_KEY) as client:
                print(
                    await client.get_bep721_token_transfer_events_by_address(
                        address=0xcd4ee0a77e09afa8d5a6518f7cf8539bef684e6c",
                        startblock=0,
                        endblock=999999999,
                        sort=asc"
                    )
                )

        Results::

            [
                {
                    "blockNumber": "2657100",
                    "timeStamp": "1606646313",
                    "hash": "0x43485c443c235156777148dddcc1483a1c8f46cccf5ab185cfc4bd678f247b6b",
                    "nonce": "6",
                    "blockHash": "0x20b6e2e67e74badc19b225a0aa4febe2382569c99842e32bc9d5dc94631a349d",
                    "from": "0x0000000000000000000000000000000000000000",
                    "contractAddress": "0x5e74094cd416f55179dbd0e45b1a8ed030e396a1",
                    "to": "0xcd4ee0a77e09afa8d5a6518f7cf8539bef684e6c",
                    "tokenID": "384552",
                    "tokenName": "Pancake Lottery Ticket",
                    "tokenSymbol": "PLT",
                    "tokenDecimal": "0",
                    "transactionIndex": "2",
                    "gas": "27000000",
                    "gasPrice": "20000000000",
                    "gasUsed": "22547256",
                    "cumulativeGasUsed": "22947060",
                    "input": "deprecated",
                    "confirmations": "4927545"
                },

                ...
            ]
        """
        return (
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

    @staticmethod
    def get_bep721_token_transfer_events_by_contract_address_paginated(
        contract_address: str, page: int, offset: int, sort: str
    ):
        """Get all token transfer events for a given BEP721 contract as numbered pages.

        **NOTE: Returns the 10,000 most recent events.**

        Args:
            contract_address (str): Target contract address.
            page (int): Page number to fetch.
            offset (int): Max records to return.
            sort (str): "asc" to return results in ascending order.

        Returns:
            List[dict]: All token transfers for target contract address.

        Example::

            from bscscan import AsyncBscScan

            async with AsyncBscScan(YOUR_API_KEY) as client:
                print(
                    await client.get_bep721_token_transfer_events_by_contract_address_paginated(
                        contract_address="0x5e74094cd416f55179dbd0e45b1a8ed030e396a1",
                        page=1,
                        offset=100,
                        sort="asc"
                    )
                )

        Results::

            [
                {
                    "blockNumber": "1592608",
                    "timeStamp": "1603449812",
                    "hash": "0x4d9d86b931bdaef28c2437d1dcf6bdbc9c80c5681cbf819726cad94c04edcd7a",
                    "nonce": "391",
                    "blockHash": "0x69e55bc5300dff5c5c009e818a0e8f71e0c895d1ce36da6b79182c860381524d",
                    "from": "0x0000000000000000000000000000000000000000",
                    "contractAddress": "0x5e74094cd416f55179dbd0e45b1a8ed030e396a1",
                    "to": "0xb9fa21a62fc96cb2ac635a051061e2e50d964051",
                    "tokenID": "1",
                    "tokenName": "Pancake Lottery Ticket",
                    "tokenSymbol": "PLT",
                    "tokenDecimal": "0",
                    "transactionIndex": "4",
                    "gas": "1919509",
                    "gasPrice": "20000000000",
                    "gasUsed": "1260114",
                    "cumulativeGasUsed": "1700085",
                    "input": "deprecated",
                    "confirmations": "5992037"
                },

                ...
            ]
        """
        return (
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

    @staticmethod
    def get_bep721_token_transfer_events_by_address_and_contract_paginated(
        contract_address: str, address: str, page: int, offset: int, sort: str
    ):
        """Get all token transfers for a given BEP721 contract and wallet as numbered pages.

        Args:
            contract_address (str): Target contract address.
            address (str): Target wallet address.
            page (int): Page number to fetch.
            offset (int): Max records to return.
            sort (str): "asc" to return results in ascending order.

        Returns:
            List[dict]: All token transfers as a list of dictionaries.

        Example::

            from bscscan import AsyncBscScan

            async with AsyncBscScan(YOUR_API_KEY) as client:
                print(
                    await client.get_bep721_token_transfer_events_by_address_and_contract_paginated(
                        "contract_address": "0x5e74094cd416f55179dbd0e45b1a8ed030e396a1",
                        "address": "0xcd4ee0a77e09afa8d5a6518f7cf8539bef684e6c",
                        "page": 1,
                        "offset": 100,
                        "sort": "asc"
                    )
                )

        Results::

            [
                {
                    "blockNumber": "2657100",
                    "timeStamp": "1606646313",
                    "hash": "0x43485c443c235156777148dddcc1483a1c8f46cccf5ab185cfc4bd678f247b6b",
                    "nonce": "6",
                    "blockHash": "0x20b6e2e67e74badc19b225a0aa4febe2382569c99842e32bc9d5dc94631a349d",
                    "from": "0x0000000000000000000000000000000000000000",
                    "contractAddress": "0x5e74094cd416f55179dbd0e45b1a8ed030e396a1",
                    "to": "0xcd4ee0a77e09afa8d5a6518f7cf8539bef684e6c",
                    "tokenID": "384552",
                    "tokenName": "Pancake Lottery Ticket",
                    "tokenSymbol": "PLT",
                    "tokenDecimal": "0",
                    "transactionIndex": "2",
                    "gas": "27000000",
                    "gasPrice": "20000000000",
                    "gasUsed": "22547256",
                    "cumulativeGasUsed": "22947060",
                    "input": "deprecated",
                    "confirmations": "4927545"
                },

                ...
            ]
        """
        return (
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

    @staticmethod
    def get_validated_blocks_by_address(address: str):
        """Get a list of validated blocks by a specific address.

        Args:
            address (str): Target validator address.

        Returns:
            List[dict]: All validated blocks as a list of dictionaries.

        Example::

            from bscscan import AsyncBscScan

            async with AsyncBscScan(YOUR_API_KEY) as client:
                print(
                    await client.get_validated_blocks_by_address(
                        address="0x4396e28197653d0c244d95f8c1e57da902a72b4e"
                    )
                )

        Results::

            [
                {
                    "blockNumber": "5572207",
                    "timeStamp": "1615421320",
                    "blockReward": "82705403500220352"
                },
                {
                    "blockNumber": "5572186",
                    "timeStamp": "1615421257",
                    "blockReward": "86981148000000000"
                },

                ...
            ]

        """
        return (
            f"{fields.MODULE}"
            f"{modules.ACCOUNT}"
            f"{fields.ACTION}"
            f"{actions.GET_MINED_BLOCKS}"
            f"{fields.ADDRESS}"
            f"{address}"
            f"{fields.BLOCK_TYPE}"
            f"{fields.BLOCKS}"
        )

    @staticmethod
    def get_validated_blocks_by_address_paginated(address: str, page: int, offset: int):
        """Get a list of validated blocks by a specific address as numbered pages.

        Args:
            address (str): Target validator address.
            page (int): Page number to fetch.
            offset (int): Max records to return.

        Returns:
            List[dict]: All validated blocks as list of dictionaries per page.

        Example::

            from bscscan import AsyncBscScan

            async with AsyncBscScan(YOUR_API_KEY) as client:
                print(
                    await client.get_validated_blocks_by_address_paginated(
                        address="0x4396e28197653d0c244d95f8c1e57da902a72b4e",
                        page=1,
                        offset=100
                    )
                )

        Results::

            [
                {
                "blockNumber": "5572207",
                "timeStamp": "1615421320",
                "blockReward": "82705403500220352"
                },

                ...
            ]
        """
        return (
            f"{fields.MODULE}"
            f"{modules.ACCOUNT}"
            f"{fields.ACTION}"
            f"{actions.GET_MINED_BLOCKS}"
            f"{fields.ADDRESS}"
            f"{address}"
            f"{fields.BLOCK_TYPE}"
            f"{fields.BLOCKS}"
            f"{fields.PAGE}"
            f"{str(page)}"
            f"{fields.OFFSET}"
            f"{str(offset)}"
        )
