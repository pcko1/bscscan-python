import requests


class ResponseParser:
    @staticmethod
    def parse(response: requests.Response):
        content = response.json()
        result = content["result"]
        status = bool(int(content["status"]))
        message = content["message"]
        assert status, f"{result} -- {message}"
        return result
