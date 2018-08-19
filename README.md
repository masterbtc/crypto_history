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
$ pip install -r requirements.txt
```

### Basic Examples

#### Initial names collecting

```python
from crypto_history import Coins

coins = Coins()

# Collect all coin names
coins.collect_coin_names()

# Print collected coin names
print coins.get_coins()
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

#### Get Ripple data

```python
ripple_data = coins.get_coin_history(coin='ripple')

print ripple_data.head()
```

```cosole
close_val coin          date  high_val   low_val  market_cap  open_val  \
1840   0.005882  XRP  Aug 04, 2013  0.005927  0.005874  45921000.0  0.005874   
1839   0.005613  XRP  Aug 05, 2013  0.005980  0.005613  45928400.0  0.005875   
1838   0.004680  XRP  Aug 06, 2013  0.005661  0.004629  44067600.0  0.005637   
1837   0.004417  XRP  Aug 07, 2013  0.004682  0.004333  36503500.0  0.004669   
1836   0.004254  XRP  Aug 08, 2013  0.004424  0.004175  34372500.0  0.004397   
     symbol  volume  middle_val   datetime  
1840    XRP     NaN    0.005900 2013-08-04  
1839    XRP     NaN    0.005796 2013-08-05  
1838    XRP     NaN    0.005145 2013-08-06  
1837    XRP     NaN    0.004508 2013-08-07  
1836    XRP     NaN    0.004299 2013-08-08  
```

#### Get Full History

```python
coins.get_all_coins_history(verbose=True) # Time expensive!
```