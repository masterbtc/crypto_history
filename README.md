# Crypto History Tool

## About

Crypto History is a tool for collecting day by day history for the most
popular crypto currencies. Day by day information contains next data

* Coin name
* Date
* Symbol
* Open Value
* High Value
* Low Value
* Close Value
* Volume
* Market Cap

User can provide some special date, or just collect the whole history.

## Usage

### Installation

```bash
$ git clone git@github.com:gavrilo91/crypto_history.git
$ cd crypto_history
$ virtualenv venv
$ source venv/bin/activate
$ pip install requirements.txt
```

### Basic Examples

##### Initial names collecting

```python
from crypto_history import Coins

coins = Coins()

# Collect all coin names
coins.collect_coin_names()

# Print collected coin names
print coins.get_coins()
```

#### Get Ripple data

```python
ripple_data = coins.get_coin_history(coin='ripple')

print ripple_data.head()
```