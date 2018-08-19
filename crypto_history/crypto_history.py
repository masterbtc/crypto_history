import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime


class Coins:

    def __init__(self, url=None):
        """
        Create Coin object
        :param url: Url for list of all currencies
        """
        if url:
            self.url = url
        else:
            self.url = 'https://coinmarketcap.com/currencies/views/all/'
        self.coins = None
        self.coins_history = None

    def get_coin_history(self, coin=None, end_date=None, start_date=None):
        """
        Returns history for the coin in form of Pandas DataFrame starting from start_date and
        ending on end_date in form 'YYYYMMDD'
        :param coin:
        :param end_date:
        :param start_date:
        :return:
        """
        if coin:
            try:
                coin_url = self.coins[coin]
            except:
                print('Coin ' + str(coin) + ' does not exist in local database!')
            if start_date:
                start_date = start_date
            else:
                start_date = '20130428'
            if end_date:
                end_date = end_date
            else:
                now = str(datetime.now().date()).replace('-', '')
                end_date = now
            coin_url = coin_url + '/historical-data/?start=' + start_date + '&end=' + end_date
            content = urlopen(coin_url).read()
            soup = BeautifulSoup(content, 'html.parser')
            results = soup.find_all("tr", class_="text-right")
            infos = []
            for result in results:
                date = result.find_all('td')[0].text

                open_val = result.find_all('td')[1].text
                if open_val == '-':
                    open_val = None
                else:
                    open_val = float(result.find_all('td')[1].text.replace(',', ''))

                high_val = result.find_all('td')[2].textoc
                if high_val == '-':
                    high_val = None
                else:
                    high_val = float(result.find_all('td')[2].text.replace(',', ''))

                low_val = result.find_all('td')[3].text
                if low_val == '-':
                    low_val = None
                else:
                    low_val = float(result.find_all('td')[3].text.replace(',', ''))

                close_val = result.find_all('td')[4].text
                if close_val == '-':
                    close_val = None
                else:
                    close_val = float(result.find_all('td')[4].text.replace(',', ''))

                volume = result.find_all('td')[5].text
                if volume == '-':
                    volume = None
                else:
                    volume = float(result.find_all('td')[5].text.replace(',', ''))

                market_cap = result.find_all('td')[6].text
                if market_cap == '-':
                    market_cap = None
                else:
                    market_cap = float(result.find_all('td')[6].text.replace(',', ''))
                temp = {
                    "coin": soup.title.text.split()[0],
                    "date": date,
                    "symbol": soup.title.text.split()[1].replace('(', '').replace(')', ''),
                    "open_val": open_val,
                    "high_val": high_val,
                    "low_val": low_val,
                    "close_val": close_val,
                    "volume": volume,
                    "market_cap": market_cap
                }
                infos.append(temp)
            df_all = pd.DataFrame.from_dict(infos)
            df_all['middle_val'] = (df_all.high_val + df_all.low_val) / 2
            df_all['datetime'] = pd.to_datetime(df_all['date'])
            df_all = df_all.sort_values(by='datetime')
            return df_all
        else:
            return None

    def get_all_coins_history(self, end_date=None, start_date=None, verbose=True):
        """
        Returns history for all of the coins in form of the Pandas DataFrame starting from the start_date and
        ending on the end_date in form 'YYYYMMDD'
        :param end_date:
        :param start_date:
        :param verbose:
        :return:
        """
        infos = []
        for coin in self.get_coins():
            if verbose:
                print("Collecting data for >> " + coin)
            if start_date:
                start_date = start_date
            else:
                start_date = '20130428'
            if end_date:
                end_date = end_date
            else:
                now = str(datetime.now().date()).replace('-', '')
                end_date = now
            coin_url = self.coins[coin]
            coin_url = coin_url + '/historical-data/?start=' + start_date + '&end=' + end_date
            content = urlopen(coin_url).read()
            soup = BeautifulSoup(content, 'html.parser')
            results = soup.find_all("tr", class_="text-right")

            for result in results:
                date = result.find_all('td')[0].text

                open_val = result.find_all('td')[1].text
                if open_val == '-':
                    open_val = None
                else:
                    open_val = float(result.find_all('td')[1].text.replace(',', ''))

                high_val = result.find_all('td')[2].text
                if high_val == '-':
                    high_val = None
                else:
                    high_val = float(result.find_all('td')[2].text.replace(',', ''))

                low_val = result.find_all('td')[3].text
                if low_val == '-':
                    low_val = None
                else:
                    low_val = float(result.find_all('td')[3].text.replace(',', ''))

                close_val = result.find_all('td')[4].text
                if close_val == '-':
                    close_val = None
                else:
                    close_val = float(result.find_all('td')[4].text.replace(',', ''))

                volume = result.find_all('td')[5].text
                if volume == '-':
                    volume = None
                else:
                    volume = float(result.find_all('td')[5].text.replace(',', ''))

                market_cap = result.find_all('td')[6].text
                if market_cap == '-':
                    market_cap = None
                else:
                    market_cap = float(result.find_all('td')[6].text.replace(',', ''))
                temp = {
                    "coin": coin,  # soup.title.text.split()[0],
                    "date": date,
                    "symbol": soup.title.text.split()[1].replace('(', '').replace(')', ''),
                    "open_val": open_val,
                    "high_val": high_val,
                    "low_val": low_val,
                    "close_val": close_val,
                    "volume": volume,
                    "market_cap": market_cap
                }
                infos.append(temp)
        df_all = pd.DataFrame.from_dict(infos)
        df_all['middle_val'] = (df_all.high_val + df_all.low_val) / 2
        df_all['datetime'] = pd.to_datetime(df_all['date'])
        df_all = df_all.sort_values(by='datetime')
        self.coins_history = df_all

    def collect_coin_names(self, coins_url=None):
        """
        Collect names and urls for all of the available coins from the coinmarketcap.com
        :param coins_url: By default url is https://coinmarketcap.com/currencies/
        :return: stores dictionary to the self.coin_urls {coin_name: coin_url}
        """
        if coins_url:
            currency_url = coins_url
        else:
            currency_url = 'https://coinmarketcap.com/currencies/'
        try:
            content = urlopen(currency_url).read()
        except:
            print('Error reading coinmarketcap.com!')
            return 1
        soup = BeautifulSoup(content, 'html.parser')
        results = soup.find_all("tr")[1:]
        urls = {}
        for result in results:
            # Parsing Name
            name = result.find_all('td', class_='no-wrap currency-name')[0].find_all('a')[0]['href'].split('/')[-2]

            # Creating url
            now = str(datetime.now().date()).replace('-', '')
            url_tmp = 'https://coinmarketcap.com/currencies/' + name

            urls[name] = url_tmp
        self.coins = urls

    def get_coins(self):
        """
        Returns list of collected coins
        :return: list of coins
        """
        if self.coins:
            return self.coins.keys()
        else:
            return []

    def to_csv(self, filename='coins.csv', header=True):
        """
        Save Coins History to the csv file
        :param filename:
        :param header:
        :return:
        """
        if filename:
            self.coins_history.to_csv(path_or_buf=filename, index=False, header=header)
