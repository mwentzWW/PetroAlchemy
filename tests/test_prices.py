import unittest
from eia_data import commodity_prices


class Prices_Exist(unittest.TestCase):
    def test_spot_prices(self):
        self.assertIsNotNone(commodity_prices.spot_prices())

    def test_futures_prices(self):
        self.assertIsNotNone(commodity_prices.futures_prices())


if __name__ == "__main__":
    unittest.main()
