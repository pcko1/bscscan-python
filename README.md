# bscscan-python

<p align="center">
  <a href="https://github.com/pcko1/bscscan-python" alt="build">
        <img src="https://github.com/pcko1/bscscan-python/workflows/build/badge.svg" /></a>
  
  <a href="https://codecov.io/gh/pcko1/bscscan-python" alt="codecov">
        <img src="https://codecov.io/gh/pcko1/bscscan-python/branch/master/graph/badge.svg" /></a>
  
  <a href="https://app.codacy.com/gh/pcko1/bscscan-python?utm_source=github.com&utm_medium=referral&utm_content=pcko1/bscscan-python&utm_campaign=Badge_Grade" alt="code-quality">
        <img src="https://api.codacy.com/project/badge/Grade/a39faec4c53e45cda03c92d216278c65" /></a>
  
  <a href="https://codeclimate.com/github/pcko1/bscscan-python" alt="tech-debt">
        <img src="https://img.shields.io/codeclimate/tech-debt/pcko1/bscscan-python" /></a>

  <a href="https://codeclimate.com/github/pcko1/bscscan-python/maintainability" alt="maintainability">
        <img src="https://api.codeclimate.com/v1/badges/b9fefb77fed228a664d2/maintainability" /></a>
  
  <a href="https://www.codefactor.io/repository/github/pcko1/bscscan-python" alt="code-factor">
        <img src="https://www.codefactor.io/repository/github/pcko1/bscscan-python/badge" /></a>
</p>

<p align="center">
  <a href="https://badge.fury.io/py/bscscan-python" alt="pypi">
        <img src="https://badge.fury.io/py/bscscan-python.svg" /></a>
  
  <a href="" alt="pypi-downloads">
        <img src="https://img.shields.io/pypi/dm/bscscan-python" /></a>
  
  <a href="" alt="license">
        <img src="https://img.shields.io/github/license/pcko1/bscscan-python" /></a>
  
  <a href="https://www.python.org/downloads/release/python-385/" alt="python-version">
        <img src="https://img.shields.io/badge/python-3.8-blue.svg" /></a>
  
  <a href="https://zenodo.org/badge/latestdoi/340319392" alt="DOI">
        <img src="https://zenodo.org/badge/340319392.svg" /></a>  
</p>

<p align="center">
  A complete Python API for <a href="https://bscscan.com/">BscScan.com</a>
</p>

<p align="center">
  Powered by <a href="https://bscscan.com/apis">BscScan.com APIs</a>
</p>

<p align="center">
  Available on <a href="https://pypi.org/project/bscscan-python/">PyPI</a> 
</p>

<p align="center">
  :book: Read the official documentation here :book:
</p>

<p align="center">
  👇
</p>

<p align="center">
  <a href="https://bscscan-python.pankotsias.com/" alt="docs">
        <img src="https://img.shields.io/badge/docs-passing-brightgreen" /></a> 
</p>

<p align="center">
  <i>A fork of the <a href="https://github.com/pcko1/etherscan-python">etherscan-python</a> package.</i>
</p>



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
* `get_erc721_token_transfer_events_by_address`
* `get_erc721_token_transfer_events_by_contract_address_paginated`
* `get_erc721_token_transfer_events_by_address_and_contract_paginated`
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

</details>

<details><summary>Logs <a href="https://bscscan.com/apis#logs">(source)</a></summary>
<p>
  
* `get_logs`

</details>

*If you think that a newly-added method is missing, kindly open an [issue](https://github.com/pcko1/bscscan-python/issues) as a feature request and I will do my best to add it.*

## Installation

Before proceeding, you should register an account on [BscScan.com](https://bscscan.com/) and [generate a personal API key](https://bscscan.com/myapikey) to use. 

Install from source:

``` bash
pip install git+https://github.com/pcko1/bscscan-python.git@stable
```

Alternatively, install from [PyPI](https://pypi.org/project/bscscan-python/):

```bash
pip install bscscan-python
```

## Unit tests

In `bash`, test that everything looks OK on your end using your `YOUR_API_KEY` (without quotation marks):

``` bash
bash run_tests.sh YOUR_API_KEY
````

Note: This will install the `coverage` package in your activated `python` environment.

## Usage
In `python`, create a client with your personal [BscScan.com](https://bscscan.com/) API key:

``` python
import asyncio
from bscscan import BscScan

YOUR_API_KEY = "..."

async def main():
  async with BscScan(YOUR_API_KEY) as bsc:
    print(await bsc.get_bnb_balance(address="0x0000000000000000000000000000000000001004"))

if __name__ == "__main__":
  asyncio.run(main())

> '167195709084498025431541166'
```

## Examples

Detailed examples (arguments and results) for all methods may be found in the [official documentation](https://bscscan-python.pankotsias.com/bscscan.modules.html). [![Documentation Status](https://img.shields.io/badge/docs-passing-brightgreen)](https://bscscan-python.pankotsias.com/)


## Issues

For problems regarding installing or using the package please open an [issue](https://github.com/pcko1/bscscan-python/issues). Kindly avoid disclosing potentially sensitive information such as your API keys or your wallet addresses.

## Cite

Kotsias, P. C., pcko1/bscscan-python: v1.0.0. *https://github.com/pcko1/bscscan-python (2021)*. doi:10.5281/zenodo.4781726

or in ```bibtex```:

```bibtex
@misc{Kotsias2020,
  author = {Kotsias, P.C.},
  title = {pcko1/bscscan-python},
  year = {2021},
  publisher = {Zenodo},
  url = {https://github.com/pcko1/bscscan-python},
  doi = {10.5281/zenodo.4781726}
}
```

Feel free to leave a :star: if you found this package useful.

___

Powered by [Bscscan.com APIs](https://bscscan.com/apis).
