from bscscan.enums.actions_enum import ActionsEnum as actions
from bscscan.enums.fields_enum import FieldsEnum as fields
from bscscan.enums.modules_enum import ModulesEnum as modules
from bscscan.enums.tags_enum import TagsEnum as tags


class Proxy:
    @staticmethod
    def get_proxy_block_number():
        """Get the number of the most recent block.

        Returns:
            str: The block number.

        Example::

            from bscscan import BscScan

            async with BscScan(YOUR_API_KEY) as client:
                print(await client.get_proxy_block_number())

        Results::

            "0x73fe1b"

        """
        return (
            f"{fields.MODULE}"
            f"{modules.PROXY}"
            f"{fields.ACTION}"
            f"{actions.ETH_BLOCK_NUMBER}"
        )

    @staticmethod
    def get_proxy_block_by_number(tag: str):
        """Get information about a block by its block number.

        Args:
            tag (str): The target block tag.

        Returns:
            dict: Information about target block, including its transactions.


        Example::

            from bscscan import BscScan

            async with BscScan(YOUR_API_KEY) as client:
                print(
                    await client.get_proxy_block_by_number(
                        tag="0x3d0900"
                    )
                )

        Results::

            {
                "difficulty": "0x2",
                "extraData": "0xd883010004846765746888676f312e31352e35856c696e7578000000000000000bac492386862ad3df4b666bc096b0505bb694da22b81f8e175ffde54d797fe11eb03f9e3bf75f1d2d4c407bbe49438ed859fe965b140dcf1aab71a935e7a025f4da968de7e4d7e4004197917f4070f14430b3230294d12c6ab2aac5c2cd68e80b16b5816488aa4d1955ee33403f8ccb1d4de5fb97c7ade2685b1ded8013785d6623cc18d214320b6bb6475968bf0b8b6fb4e317a0f9d6f03eaf8ce6675bc60d6bbad7cf34b5fa511d8e963dbba288b1960e75d672b61c6014342d914470ec7ac2975be345796c2b7ae2f5b9e386cd1b50a4550696d957cb4900f03a82012708dafc9e1b880fd083b32182b869be8e098c4d90829ce8f72d0163c1d5cf348a862d550630a34efe6222e33adb84307f41b218d1823afb6f6da6f79b60359f141df90a0c745125b131caaffd12ada8c942f31098482748fcf2b9d3dc1d8de7b0e4b218c5d6af1f979ac42bc68d98a5a0d796c6ab01b8f7166496996a7da21cf1f1b04d9b3e26a3d077ce2fd7544e0b2cc94692d4a704debef7bcb61328d6caa02bbebaebb5d7e581e4b66559e635f805ffea0a6e3c511bbd10f4519ece37dc24887e11b55deee8583c06155b4bcae968b057a7b9fc104d05245ea6768867bb02fc189e81391de2c3e7f8b9a9f48a4a0c562ab81f4b2221f9c761d3dff0f17f08f1e0259e5f00",
                "gasLimit": "0x1c9c380",
                "gasUsed": "0x119964",
                "hash": "0x3a21da1d1f88577771f1e94b554294d699f696487a3554c1618521d68b48a493",
                "logsBloom": "0x0520040200006004000100008400402080000840048000000000000088a0010000080000000000100000020000080000080000200008000000000000002420000010008000004002000000080010102120100000101400024a04000000100080000000240242000002000040008008000000001201880200000000100020000800400010000000040030000000000000000c0c010000800930040040000008300600000000400004004000020004000000004000000000009000000000000004000100020000002000000002041208000000000000000012380002010000e0002810040000000000012000000001000000040008400808000000000000000000",
                "miner": "0x4430b3230294d12c6ab2aac5c2cd68e80b16b581",
                "mixHash": "0x0000000000000000000000000000000000000000000000000000000000000000",
                "nonce": "0x0000000000000000",
                "number": "0x3d0900",
                "parentHash": "0x911a33c1adbba5b5af70aa3d6adcc76edb23ba0da1b38948b2ca0de4a8ac770c",
                "receiptsRoot": "0xfc2c03091df8019b78ef2c6eb6c0013c9ccd635aa8a5bccb33022c18b15b6c08",
                "sha3Uncles": "0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347",
                "size": "0x8c4",
                "stateRoot": "0xad1d6884d20fca931c9ba5d1a62cd65aaf1bceeb56c30180cee218be18e42393",
                "timestamp": "0x60010570",
                "totalDifficulty": "0x7a0149",
                "transactions": [
                    {
                        "blockHash": "0x3a21da1d1f88577771f1e94b554294d699f696487a3554c1618521d68b48a493",
                        "blockNumber": "0x3d0900",
                        "from": "0xc524faaed591471a0b5fc93288fd8fe6f45d7b64",
                        "gas": "0xf4240",
                        "gasPrice": "0x4a817c800",
                        "hash": "0x7d3a58fe7c29bd30b64928b3f05c14f42086abe78ed51420a3a11fb4253f3ab5",
                        "input": "0x19efa3b90000000000000000000000008e78c72b37ce47811901ac99ded5c62277d2e18758275c2ad36555c03255212657dfae202219de57225d31c60be54b3c05717c41",
                        "nonce": "0x31206",
                        "to": "0x3900afd6613022d8e37a9ba945e02ee920bc48dc",
                        "transactionIndex": "0x0",
                        "value": "0x0",
                        "v": "0x94",
                        "r": "0xd6a7a7eef0023721c580cb05802293433fb9c08614a9606d2a2139943bc4498",
                        "s": "0x625f62272dfb849c08cd47f5f008421502caf87c508885c7d6c853f73989253f"
                    },

                    ...
                ]
                "transactionsRoot": "0x8ad23ac4ccf6e9335e7801c5ebbd5f4546413cca56ab2ace02beaa022415c236",
                "uncles": []
            }
        """
        return (
            f"{fields.MODULE}"
            f"{modules.PROXY}"
            f"{fields.ACTION}"
            f"{actions.ETH_GET_BLOCK_BY_NUMBER}"
            f"{fields.TAG}"
            f"{tag}"
            f"{fields.BOOLEAN}"
            f"true"
        )

    @staticmethod
    def get_proxy_block_transaction_count_by_number(tag: str):
        """Get the number of transactions in a specific block.

        Args:
            tag (str): The target block tag.

        Returns:
            str: The number of txs in the block using hex base format.

        Example::

            from bscscan import BscScan

            async with BscScan(YOUR_API_KEY) as client:
                print(
                    await client.get_proxy_block_transaction_count_by_number(
                        tag="0x3d0900"
                    )
                )

        Results::

            "0x7"
        """
        return (
            f"{fields.MODULE}"
            f"{modules.PROXY}"
            f"{fields.ACTION}"
            f"{actions.ETH_GET_BLOCK_TRANSACTION_COUNT_BY_NUMBER}"
            f"{fields.TAG}"
            f"{tag}"
        )

    @staticmethod
    def get_proxy_transaction_by_hash(txhash: str):
        """Get tx information given its hash.

        Args:
            txhash (str): Target transaction hash.

        Returns:
            dict: Standard tx data, including v,r,s values.

        Example::

            from bscscan import BscScan

            async with BscScan(YOUR_API_KEY) as client:
                print(
                    await client.get_proxy_transaction_by_hash(
                        txhash="0xa0f2e87dfb75e3ebb8b23eff7b490442ff74cf8921eb61217dfc48918fe4020f"
                    )
                )

        Results::

            {
                "blockHash": "0x3a21da1d1f88577771f1e94b554294d699f696487a3554c1618521d68b48a493",
                "blockNumber": "0x3d0900",
                "from": "0x4430b3230294d12c6ab2aac5c2cd68e80b16b581",
                "gas": "0x7fffffffffffffff",
                "gasPrice": "0x0",
                "hash": "0xa0f2e87dfb75e3ebb8b23eff7b490442ff74cf8921eb61217dfc48918fe4020f",
                "input": "0xf340fa010000000000000000000000004430b3230294d12c6ab2aac5c2cd68e80b16b581",
                "nonce": "0x278d1",
                "to": "0x0000000000000000000000000000000000001000",
                "transactionIndex": "0x6",
                "value": "0x50bbe73ea9b000",
                "v": "0x93",
                "r": "0x4e63792b339521b74cdb3cad2d8fdf0f5fc3dbb2e169a5a536692dd89eca4da1",
                "s": "0x40f8ccd64337d6cfb15f1d40932068356da34138b8c9f6a818a68d20607451dc"
            }
        """
        return (
            f"{fields.MODULE}"
            f"{modules.PROXY}"
            f"{fields.ACTION}"
            f"{actions.ETH_GET_TRANSACTION_BY_HASH}"
            f"{fields.TXHASH}"
            f"{txhash}"
        )

    @staticmethod
    def get_proxy_transaction_by_block_number_and_index(tag: str, index: str):
        """Get transaction by block number and tx index.

        Args:
            tag (str): Target block tag.
            index (str): Target tx index.

        Returns:
            dict: Standard tx data, including v,r,s values.

        Example::

            from bscscan import BscScan

            async with BscScan(YOUR_API_KEY) as client:
                print(
                    await client.get_proxy_transaction_by_block_number_and_index(
                        tag="0x3d0900",
                        index"="0x0"
                    )
                )

        Results::

            {
                "blockHash": "0x3a21da1d1f88577771f1e94b554294d699f696487a3554c1618521d68b48a493",
                "blockNumber": "0x3d0900",
                "from": "0xc524faaed591471a0b5fc93288fd8fe6f45d7b64",
                "gas": "0xf4240",
                "gasPrice": "0x4a817c800",
                "hash": "0x7d3a58fe7c29bd30b64928b3f05c14f42086abe78ed51420a3a11fb4253f3ab5",
                "input": "0x19efa3b90000000000000000000000008e78c72b37ce47811901ac99ded5c62277d2e18758275c2ad36555c03255212657dfae202219de57225d31c60be54b3c05717c41",
                "nonce": "0x31206",
                "to": "0x3900afd6613022d8e37a9ba945e02ee920bc48dc",
                "transactionIndex": "0x0",
                "value": "0x0",
                "v": "0x94",
                "r": "0xd6a7a7eef0023721c580cb05802293433fb9c08614a9606d2a2139943bc4498",
                "s": "0x625f62272dfb849c08cd47f5f008421502caf87c508885c7d6c853f73989253f"
            }
        """
        return (
            f"{fields.MODULE}"
            f"{modules.PROXY}"
            f"{fields.ACTION}"
            f"{actions.ETH_GET_TRANSACTION_BY_BLOCK_NUMBER_AND_INDEX}"
            f"{fields.TAG}"
            f"{tag}"
            f"{fields.INDEX}"
            f"{index}"
        )

    @staticmethod
    def get_proxy_transaction_count(address: str):
        """Get number of transactions sent from an address.

        Args:
            address (str): Target address.

        Returns:
            str: Number of txs using hex base format.

        Example::

            from bscscan import BscScan

            async with BscScan(YOUR_API_KEY) as client:
                print(
                    await client.get_proxy_transaction_count(
                        address="0x4430b3230294D12c6AB2aAC5C2cd68E80B16b581"
                    )
                )

        Results::

            "0x56adb"
        """
        return (
            f"{fields.MODULE}"
            f"{modules.PROXY}"
            f"{fields.ACTION}"
            f"{actions.ETH_GET_TRANSACTION_COUNT}"
            f"{fields.ADDRESS}"
            f"{address}"
            f"{fields.TAG}"
            f"{tags.LATEST}"
        )

    @staticmethod
    def send_proxy_raw_transaction(hexs: str):
        """Submits a pre-signed transaction for broadcast to the Binance Smart Chain network.

        Args:
            hexs (str): the string representing the signed raw transaction data to broadcast..

        Returns:
            str: the transaction hash of the submitted raw transaction.Use get_proxy_transaction_receipt to retrieve full details.

        Example::

            from bscscan import BscScan

            async with BscScan(YOUR_API_KEY) as client:
                print(
                    await client.send_proxy_raw_transaction(hex="0xf904808000831cfde080")
                )

        Results::

            0xe670ec64341771606e55d6b4ca35a1a6b75ee3d5145a99d05921026d1527331

        """
        return (
            f"{fields.MODULE}"
            f"{modules.PROXY}"
            f"{fields.ACTION}"
            f"{actions.ETH_SEND_RAW_TRANSACTION}"
            f"{fields.HEX}"
            f"{hex}"
        )

    @staticmethod
    def get_proxy_transaction_receipt(txhash: str):
        """Get receipt of transaction from its hash.

        Args:
            txhash (str): Target transaction hash.

        Returns:
            dict: Transaction receipt including logs.

        Example::

            from bscscan import BscScan

            async with BscScan(YOUR_API_KEY) as client:
                print(
                    await client.get_proxy_transaction_receipt(
                        txhash="0xa0f2e87dfb75e3ebb8b23eff7b490442ff74cf8921eb61217dfc48918fe4020f"
                    )
                )

        Results::

            {
                "blockHash": "0x3a21da1d1f88577771f1e94b554294d699f696487a3554c1618521d68b48a493",
                "blockNumber": "0x3d0900",
                "contractAddress": null,
                "cumulativeGasUsed": "0x119964",
                "from": "0x4430b3230294d12c6ab2aac5c2cd68e80b16b581",
                "gasUsed": "0x42fe",
                "logs": [
                {
                    "address": "0x0000000000000000000000000000000000001000",
                    "topics": [
                    "0x93a090ecc682c002995fad3c85b30c5651d7fd29b0be5da9d784a3302aedc055",
                    "0x0000000000000000000000004430b3230294d12c6ab2aac5c2cd68e80b16b581"
                    ],
                    "data": "0x0000000000000000000000000000000000000000000000000050bbe73ea9b000",
                    "blockNumber": "0x3d0900",
                    "transactionHash": "0xa0f2e87dfb75e3ebb8b23eff7b490442ff74cf8921eb61217dfc48918fe4020f",
                    "transactionIndex": "0x6",
                    "blockHash": "0x3a21da1d1f88577771f1e94b554294d699f696487a3554c1618521d68b48a493",
                    "logIndex": "0x1f",
                    "removed": false
                }
                ],
                "logsBloom": "0x00000002000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002010000000000000000000000000000000000020000200000000000000800000000000000000000000000000000000000000000000000000000000000000000000000400000000000000000000000000000000000000000000000000000000000000400000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000",
                "status": "0x1",
                "to": "0x0000000000000000000000000000000000001000",
                "transactionHash": "0xa0f2e87dfb75e3ebb8b23eff7b490442ff74cf8921eb61217dfc48918fe4020f",
                "transactionIndex": "0x6"
            }
        """
        return (
            f"{fields.MODULE}"
            f"{modules.PROXY}"
            f"{fields.ACTION}"
            f"{actions.ETH_GET_TRANSACTION_RECEIPT}"
            f"{fields.TXHASH}"
            f"{txhash}"
        )

    @staticmethod
    def get_proxy_call(to: str, data: str):
        """Executes a new message call immediately without creating a transaction on the block chain.

        Args:
            to (str): Contract address to send message to.
            data (str): Message data in bytecode.

        Returns:
            str: The response to the message in hex base format.

        Example::

            from bscscan import BscScan

            async with BscScan(YOUR_API_KEY) as client:
                print(
                    await client.get_proxy_call(
                        to="0xAEEF46DB4855E25702F8237E8f403FddcaF931C0",
                        data="0x70a08231000000000000000000000000e16359506c028e51f16be38986ec5746251e9724"
                    )
                )

        Results::

            "0x"
        """
        return (
            f"{fields.MODULE}"
            f"{modules.PROXY}"
            f"{fields.ACTION}"
            f"{actions.ETH_CALL}"
            f"{fields.TO}"
            f"{to}"
            f"{fields.DATA}"
            f"{data}"
            f"{fields.TAG}"
            f"{tags.LATEST}"
        )

    @staticmethod
    def get_proxy_code_at(address: str):
        """Get contract bytecode at target address, if any.

        Args:
            address (str): Address to query for bytecode.

        Returns:
            str: The bytecode in hex base format.

        Example::

            from bscscan import BscScan

            async with BscScan(YOUR_API_KEY) as client:
                print(
                    await client.get_proxy_code_at(
                        address="0x0000000000000000000000000000000000001000"
                    )
                )

        Results::

            "0x60806040526004361061027d5760003560e01c80639dc092621161014f578..."
        """
        return (
            f"{fields.MODULE}"
            f"{modules.PROXY}"
            f"{fields.ACTION}"
            f"{actions.ETH_GET_CODE}"
            f"{fields.ADDRESS}"
            f"{address}"
            f"{fields.TAG}"
            f"{tags.LATEST}"
        )

    @staticmethod
    def get_proxy_storage_position_at(position: str, address: str):
        """Get the value from a storage position at a given address.

        Args:
            position (str): Target position in hex base format.
            address (str): Target address.

        Returns:
            str: Value in hex base format.

        Example::

            from bscscan import BscScan

            async with BscScan(YOUR_API_KEY) as client:
                print(
                    await client.get_proxy_storage_position_at(
                        position="0x0",
                        address="0x0000000000000000000000000000000000001004"
                    )
                )

        Results::

            "0x0000000000000000000000000000000000000000000000000000000000000001"
        """
        return (
            f"{fields.MODULE}"
            f"{modules.PROXY}"
            f"{fields.ACTION}"
            f"{actions.ETH_GET_STORAGE_AT}"
            f"{fields.ADDRESS}"
            f"{address}"
            f"{fields.POSITION}"
            f"{position}"
            f"{fields.TAG}"
            f"{tags.LATEST}"
        )

    @staticmethod
    def get_proxy_gas_price():
        """Get current gas price in wei.

        Returns:
            str: Gas price in wei and hex base format.

        Example::

            from bscscan import BscScan

            async with BscScan(YOUR_API_KEY) as client:
                print(await client.get_proxy_gas_price())

        Results::

            "0x12a05f200"
        """
        return (
            f"{fields.MODULE}"
            f"{modules.PROXY}"
            f"{fields.ACTION}"
            f"{actions.ETH_GAS_PRICE}"
        )

    @staticmethod
    def get_proxy_est_gas(
            from_addr: str, to_addr: str, data: str, value: str, gas_price: str, gas: str
    ):
        """Get gas estimate by making a dummy call/transaction that is not added to
        the blockchain and returns the hypothetically used gas.

        Args:
            from_addr (str): Sender of transaction.
            to_addr (str): Receiver of transaction.
            data (str): Data of transaction.
            value (str): Value of transaction.
            gas_price (str): Gas price of transaction.
            gas (str): Gas of transaction.

        Returns:
            str: Estimated used gas for transaction.

        Example::

            from bscscan import BscScan

            async with BscScan(YOUR_API_KEY) as client:
                print(
                    await client.get_proxy_est_gas(
                        data="0x4e71d92d",
                        from_addr="0xbe0eb53f46cd790cd13851d5eff43d12404d33e8",
                        to_addr="0xf0160428a8552ac9bb7e050d90eeade4ddd52843",
                        value="0xff22",
                        gas_price="0x51da038cc",
                        gas="0x5f5e0ff"
                    )
                )

        Results::

            "0x5248"
        """
        return (
            f"{fields.MODULE}"
            f"{modules.PROXY}"
            f"{fields.ACTION}"
            f"{actions.ETH_ESTIMATE_GAS}"
            f"{fields.DATA}"
            f"{data}"
            f"{fields.FROM}"
            f"{from_addr}"
            f"{fields.TO}"
            f"{to_addr}"
            f"{fields.VALUE}"
            f"{value}"
            f"{fields.GAS_PRICE}"
            f"{gas_price}"
            f"{fields.GAS}"
            f"{gas}"
        )
