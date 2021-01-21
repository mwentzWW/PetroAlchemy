import unittest

from requests import api
from eia_data import commodity_prices

dev_api_key = commodity_prices.get_api_key(file_path=r"eia_data/eia_api_key.json")


class Prices_Exist(unittest.TestCase):
    def test_spot_prices(self):
        self.assertIsNotNone(commodity_prices.spot_prices(api_key=dev_api_key))

    def test_futures_prices(self):
        self.assertIsNotNone(commodity_prices.futures_prices(api_key=dev_api_key))


if __name__ == "__main__":
    unittest.main()
