import requests


class ResponseParser:
    @staticmethod
    def parse(response: dict):
        result = response["result"]
        if "status" in response.keys():
            status = bool(int(response["status"]))
            message = response["message"]
            assert status, f"{result} -- {message}"
        else:
            # GETH or Parity proxy msg format
            # TODO: see if we need those values
            jsonrpc = response["jsonrpc"]
            cid = int(response["id"])
        return result
