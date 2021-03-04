# bscscan-python

[![Build Status](https://github.com/pcko1/bscscan-python/workflows/build/badge.svg)](https://github.com/pcko1/bscscan-python) 
[![codecov](https://codecov.io/gh/pcko1/bscscan-python/branch/master/graph/badge.svg)](https://codecov.io/gh/pcko1/bscscan-python)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/a39faec4c53e45cda03c92d216278c65)](https://app.codacy.com/gh/pcko1/bscscan-python?utm_source=github.com&utm_medium=referral&utm_content=pcko1/bscscan-python&utm_campaign=Badge_Grade)
[![](https://img.shields.io/codeclimate/tech-debt/pcko1/bscscan-python)](https://codeclimate.com/github/pcko1/bscscan-python)
[![Maintainability](https://api.codeclimate.com/v1/badges/b9fefb77fed228a664d2/maintainability)](https://codeclimate.com/github/pcko1/bscscan-python/maintainability)
[![CodeFactor](https://www.codefactor.io/repository/github/pcko1/bscscan-python/badge)](https://www.codefactor.io/repository/github/pcko1/bscscan-python)

[![PyPI](https://badge.fury.io/py/bscscan-python.svg)](https://badge.fury.io/py/bscscan-python)
![PyPI - Downloads](https://img.shields.io/pypi/dm/bscscan-python)
![GitHub](https://img.shields.io/github/license/pcko1/bscscan-python)
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-385/)
[![DOI](https://zenodo.org/badge/340319392.svg)](https://zenodo.org/badge/latestdoi/340319392) 


A complete Python API for [BscScan.com](https://bscscan.com/), available on [PyPI](https://pypi.org/project/bscscan-python/). Powered by [BscScan.com APIs](https://bscscan.com/apis).

*This is a gently modified fork of the [etherscan-python](https://github.com/pcko1/etherscan-python) package.*

___


## Endpoints

The following endpoints are provided:

<details><summary>Accounts <a href="https://bscscan.com/apis#accounts">(source)</a></summary>
<p>

* `get_bnb_balance`
* `get_bnb_balance_multiple`
* `get_normal_txs_by_address`
* `get_normal_txs_by_address_paginated`
* `get_internal_txs_by_address`
* `get_internal_txs_by_address_paginated`
* `get_internal_txs_by_txhash`
* `get_internal_txs_by_block_range_paginated`
* `get_bep20_token_transfer_events_by_address`
* `get_bep20_token_transfer_events_by_contract_address_paginated`
* `get_bep20_token_transfer_events_by_address_and_contract_paginated`
* `get_validated_blocks_by_address`
* `get_validated_blocks_by_address_paginated`

</details>

<details><summary>Contracts <a href="https://bscscan.com/apis#contracts">(source)</a></summary>
<p>
  
* `get_contract_abi`
* `get_contract_source_code`

</details>

<details><summary>Transactions <a href="https://bscscan.com/apis#transactions">(source)</a></summary>
<p>
  
* `get_tx_receipt_status`

</details>

<details><summary>Blocks <a href="https://bscscan.com/apis#blocks">(source)</a></summary>
<p>
  
* `get_block_reward_by_block_number`
* `get_est_block_countdown_time_by_block_number`
* `get_block_number_by_timestamp`

</details>

<details><summary>GETH/Parity Proxy <a href="https://bscscan.com/apis#proxy">(source)</a></summary>
<p>

* `get_proxy_block_number`
* `get_proxy_block_by_number`
* `get_proxy_block_transaction_count_by_number`
* `get_proxy_transaction_by_hash`
* `get_proxy_transaction_by_block_number_and_index`
* `get_proxy_transaction_count`
* `get_proxy_transaction_receipt`
* `get_proxy_call`
* `get_proxy_code_at`
* `get_proxy_storage_position_at`
* `get_proxy_gas_price`
* `get_proxy_est_gas`

</details>

<details><summary>Tokens <a href="https://bscscan.com/apis#tokens">(source)</a></summary>
<p>
  
* `get_total_supply_by_contract_address`
* `get_circulating_supply_by_contract_address`
* `get_acc_balance_by_token_contract_address`

</details>


<details><summary>Stats <a href="https://bscscan.com/apis#stats">(source)</a></summary>
<p>
  
* `get_total_bnb_supply`
* `get_validators_list`

</details>

*If you think that a newly-added method is missing, kindly open an [issue](https://github.com/pcko1/bscscan-python/issues) as a feature request and I will do my best to add it.*

## Installation

Before proceeding, you should register an account on [BscScan.com](https://bscscan.com/) and [generate a personal API key](https://bscscan.com/myapikey) to use. 

Install from source:

``` bash
pip install git+https://github.com/pcko1/bscscan-python.git
```

Alternatively, install from [PyPI](https://pypi.org/project/bscscan-python/):

```bash
pip install bscscan-python
```

## Unit tests

In `bash`, test that everything looks OK on your end using your `YOUR_API_KEY` (without quotation marks) before proceeding:

``` bash
bash run_tests.sh YOUR_API_KEY
````

This will regenerate the logs under `logs/` with the most recent results and the timestamp of the execution.

## Usage

In `python`, create a client with your personal [BscScan.com](https://bscscan.com/) API key:

``` python
from bscscan import BscScan
bsc = BscScan(YOUR_API_KEY) # key in quotation marks
```

Then you can call all available methods, e.g.:

``` python
bsc.get_bnb_balance(address="0x0000000000000000000000000000000000001004")

> '167195709084498025431541166'
```

## Examples

Examples (arguments and results) for all methods may be found as JSON files [here](https://github.com/pcko1/bscscan-python/tree/master/logs).  For example, if you want to use the method `get_circulating_supply_by_contract_address`, you can find the supported arguments and the format of its output in its respective [JSON file](logs/standard/get_circulating_supply_by_contract_address.json):

``` json
{
  "method": "get_circulating_supply_by_contract_address",
  "module": "tokens",
  "kwargs": {
    "contract_address": "0xe9e7cea3dedca5984780bafc599bd69add087d56"
  },
  "log_timestamp": "2021-02-19-12:34:14",
  "res": "422504134592569820000000000"
}
```

where `kwargs` refer to the required named arguments and `res` refers to the expected result if you were to run:

``` python
bsc.get_circulating_supply_by_contract_address(contract_address="0xe9e7cea3dedca5984780bafc599bd69add087d56")

> '422504134592569820000000000'
```

**Disclaimer**: Those examples blindly use argument values (addresses, contracts, etc.) that were randomly chosen and do not reflect any personal preference.

## Issues

For problems regarding installing or using the package please open an [issue](https://github.com/pcko1/bscscan-python/issues). Kindly avoid disclosing potentially sensitive information such as your API keys or your wallet addresses.

## Cite

Kotsias, P. C., pcko1/bscscan-python: v1.0.0. *https://github.com/pcko1/bscscan-python (2021)*. doi:10.5281/zenodo.4580473

or in ```bibtex```:

```bibtex
@misc{Kotsias2020,
  author = {Kotsias, P.C.},
  title = {pcko1/bscscan-python},
  year = {2021},
  publisher = {Zenodo},
  url = {https://github.com/pcko1/bscscan-python},
  doi = {10.5281/zenodo.4580473}
}
```

Feel free to leave a :star: if you found this package useful.

___

 Powered by [Bscscan.com APIs](https://bscscan.com/apis).
