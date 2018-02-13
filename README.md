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

```console
>>> [u'zcash', u'siacoin', u'factom', u'hshare', u'achain', u'eccoin',
u'bitcore', u'ardor', u'namecoin', u'rise', u'bridgecoin', u'metaverse',
u'salus', u'emercoin', u'litecoin', u'dimecoin', u'diamond', u'pivx',
u'bitbay', u'lisk', u'zcoin', u'peercoin', u'burst', u'crown',
u'digibyte', u'gamecredits', u'ripple', u'ark', u'lykke', u'particl',
u'neo', u'nem', u'bitcoin-gold', u'experience-points', u'potcoin',
u'bitcoin-cash', u'ethereum-classic', u'html-coin', u'nav-coin',
u'stellar', u'deeponion', u'aeon', u'gxshares', u'groestlcoin',
u'shift', u'ethereum', u'dogecoin', u'byteball', u'paccoin',
u'digitalnote', u'verge', u'bitcoindark', u'cloakcoin', u'gulden',
u'decent', u'vertcoin', u'bitcoin', u'zclassic', u'nexus',
u'bytecoin-bcn', u'iota', u'smartcash', u'whitecoin', u'minexcoin',
u'neblio', u'hempcoin', u'asch', u'komodo', u'viacoin', u'steem',
u'ubiq', u'syscoin', u'bitshares', u'stratis', u'cardano', u'monacoin',
u'library-credit', u'dash', u'steem-dollars', u'feathercoin',
u'zencash', u'pura', u'electra', u'cryptonex', u'reddcoin',
u'xtrabytes', u'electroneum', u'monero', u'counterparty', u'raiblocks',
u'ion', u'decred', u'blocknet', u'waves', u'spectrecoin',
u'einsteinium', u'nxt', u'qtum', u'skycoin', u'iocoin']
```

#### Get Full History

```python
coins.get_all_coins_history(verbose=True) # Time expensive!
```