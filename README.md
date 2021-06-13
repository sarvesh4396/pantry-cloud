# pantry-cloud

![PyPI version](https://img.shields.io/pypi/v/pantry-cloud?color=orange&logo=pypi&logoColor=orange&style=flat-square)
![Language](https://img.shields.io/badge/python-3.7%2B-blue?logo=python&style=flat-square)
[![GitHub issues](https://img.shields.io/github/issues/sarvesh4396/pantry-cloud)](https://github.com/sarvesh4396/pantry-cloud/issues)
[![GitHub forks](https://img.shields.io/github/forks/sarvesh4396/pantry-cloud)](https://github.com/sarvesh4396/pantry-cloud/network)
[![GitHub stars](https://img.shields.io/github/stars/sarvesh4396/pantry-cloud)](https://github.com/sarvesh4396/pantry-cloud/stargazers)
[![GitHub license](https://img.shields.io/github/license/sarvesh4396/pantry-cloud)](https://github.com/sarvesh4396/pantry-cloud/blob/main/LICENSE)
![GitHub last commit (branch)](https://img.shields.io/github/last-commit/sarvesh4396/pantry-cloud/main?label=updated)
![Pull Requests](https://img.shields.io/badge/PRs-welcome-organge.svg?logo=git&logoColor=organge&style=flat-square)

This lightweight [package](https://github.com/sarvesh4396/pantry-cloud) is a python implementation of Free JSON Storage API [pantry](https://getpantry.cloud/).


## Features

- Creates a basket.
- Deletes a basket.
- Updates a basket.
- Shows account details.
- Writes basket data in json file.


> The aim of this package is to make `pantry` api usage simple.
## Installation

pantry-cloud requires [python3.7+](https://www.python.org/downloads/) to run.

#### Windows

```sh
pip install pantry-cloud
or
pip install --upgrade pantry-cloud
```

#### Linux

```sh
pip3 install pantry-cloud
or 
pip3 install --upgrade pantry-cloud
```

## Module Usage

#### Creating basket
```sh
from pantry_cloud import Pantry

pantry = Pantry(api_key='your api key')
res = pantry.create(basket='hello', inputfile='path to json file') # Use inputfile if you want to upload data
print(res)
```

#### Basket detail
```sh
from pantry_cloud import Pantry

pantry = Pantry(api_key='your api key')
res = pantry.basket(basket='hello', outputfile='path to json file') # Use outputfile if you want to write data data
print(res)
```
## CLI Usage
```sh
usage: pantry [-h] -a API [-o OUTPUT_FILE] [-i INPUT_FILE] [-s] [-b BASKET] [-u UPDATE] [-c CREATE] [-d DELETE]

optional arguments:
  -h, --help            show this help message and exit
  -a API, --api API     api key.
  -o OUTPUT_FILE, --output OUTPUT_FILE
                        output file.
  -i INPUT_FILE, --input INPUT_FILE
                        input file.
  -s, --show            Shows account details.
  -b BASKET, --basket BASKET
                        Shows data of a basket.
  -u UPDATE, --update UPDATE
                        Updates a basket.
  -c CREATE, --create CREATE
                        Creates a new basket , or replace an existing one.
  -d DELETE, --delete DELETE
                        Deletes the entire basket.
```