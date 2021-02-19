import json
import os
import time
from datetime import datetime
from unittest import TestCase

from bscscan import BscScan

CONFIG_PATH = "bscscan/configs/stable.json"
API_KEY = os.environ["API_KEY"]


def load(fname):
    with open(fname, "r") as f:
        return json.load(f)


def dump(data, fname):
    with open(fname, "w") as f:
        json.dump(data, f, indent=2)


class Case(TestCase):
    _MODULE = ""

    def test_methods(self):
        print(f"\nMODULE: {self._MODULE}")
        config = load(CONFIG_PATH)
        bscscan = BscScan(API_KEY)
        for fun, v in config.items():
            if not fun.startswith("_"):  # disabled if _
                if v["module"] == self._MODULE:
                    res = getattr(bscscan, fun)(**v["kwargs"])
                    print(f"METHOD: {fun}, RTYPE: {type(res)}")
                    fname = f"logs/standard/{fun}.json"
                    log = {
                        "method": fun,
                        "module": v["module"],
                        "kwargs": v["kwargs"],
                        "log_timestamp": datetime.now().strftime("%Y-%m-%d-%H:%M:%S"),
                        "res": res,
                    }
                    dump(log, fname)
                    time.sleep(0.5)


class TestAccounts(Case):
    _MODULE = "accounts"


class TestContracts(Case):
    _MODULE = "contracts"


class TestStats(Case):
    _MODULE = "stats"


class TestTokens(Case):
    _MODULE = "tokens"
