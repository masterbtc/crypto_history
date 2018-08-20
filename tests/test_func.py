"""
Test script for the crypto history tool
"""
import unittest
from crypto_history.crypto_history import Coins


class CoinTest(unittest.TestCase):
    """
    Execute test
    """
    _multiprocess_shared_ = True

    @classmethod
    def setUpClass(cls):
        """
        Collect coin names
        :return:
        """
        cls.coins = Coins()
        cls.coins.collect_coin_names()

    def tearDown(self):
        pass

    def test_get_coins(self):
        """
        Test coin names collection
        :return:
        """
        names = self.coins.get_coins()

        self.assertGreater(len(names), 1)

    def test_get_coin_history(self):
        """
        Test get_coin_history
        :return:
        """
        ripple_data = self.coins.get_coin_history(coin='ripple')
        self.assertGreater(ripple_data.shape[0], 100)

    def test_get_coin_history_date(self):
        """
        Test get_coin_history using date
        :return:
        """
        ripple_data = self.coins.get_coin_history(coin='ripple',
                                                  start_date='20180101',
                                                  end_date='20180105')
        self.assertEqual(ripple_data.shape[0], 5)
        self.assertEqual(ripple_data.close_val[0], 3.05)


if __name__ == "__main__":
    unittest.main()
