import requests


class ResponseParser:
    @staticmethod
    def parse(response: requests.Response):
        content = response.json()
        result = content["result"]
        status = bool(int(content["status"]))
        message = content["message"]
        if not status:
            raise AssertionError(f"{result} -- {message}")
        return result
