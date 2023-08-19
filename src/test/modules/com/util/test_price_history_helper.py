import unittest
import pandas as pd
from modules.com.util.price_history_helper import PriceHistoryHelper
from modules.core.util.get_json_data import get_json_data


class TestPriceHistoryHelper(unittest.TestCase):
    """
    Unit test class for PriceHistoryHelper.
    """

    def setUp(self):
        """
        Set up the test environment by preparing data for each test case.
        """
        data = {
            "date": ["2023-08-18", "2023-08-17", "2023-08-16"],
            "close": [18300, 19450, 19500]
        }
        self.df = pd.DataFrame(data)
        self.helper = PriceHistoryHelper(self.df)

    def test_sma(self):
        """
        Test the SMA (Simple Moving Average) calculation.

        - Check the SMA value when there is enough data.
        - Check the SMA value when there is not enough data.
        """
        self.helper.set_date("2023-08-18")
        self.assertEqual(self.helper.sma(2), (18300 + 19450) / 2)

        self.helper.set_date("2023-08-17")
        self.assertIsNone(self.helper.sma(3))

    def test_get_current_price(self):
        """
        Test the retrieval of the current price.

        - Check if the retrieved current price matches the expected row.
        """
        self.helper.set_date("2023-08-18")
        expected_row = self.df[self.df["date"] == "2023-08-18"].iloc[0]
        current_price = self.helper.get_current_price()
        pd.testing.assert_series_equal(current_price, expected_row)

    def test_set_date(self):
        """
        Test the setting of the date.

        - Check if the date is set correctly.
        """
        new_date = "2023-08-16"
        self.helper.set_date(new_date)
        self.assertEqual(self.helper._date, new_date)


class TestPriceHistoryHelperStdev(unittest.TestCase):
    """
    Unit test class for PriceHistoryHelper's stdev function.
    """

    def setUp(self):
        """
        Set up the test environment by creating a sample DataFrame.
        """
        data = {
            'date': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04'],
            'close': [10, 15, 20, 25],
            'high': [15, 20, 25, 30],
            'low': [5, 10, 15, 20],
        }
        self.df = pd.DataFrame(data)
        self.helper = PriceHistoryHelper(self.df)

    def test_stdev(self):
        """
        Test the standard deviation calculation.

        - Check the standard deviation value with valid length and default source function.
        - Check the standard deviation value with valid length and custom source function.
        - Check the standard deviation value with invalid length.
        """
        self.helper.set_date('2022-01-04')
        stdev = self.helper.stdev(3)
        self.assertAlmostEqual(stdev, 5)

        def custom_source_func(row):
            return row['high'] - row['low']

        self.helper.set_date('2022-01-03')
        stdev = self.helper.stdev(2, cal_source_func=custom_source_func)
        self.assertAlmostEqual(stdev, 0)

        self.helper.set_date('2022-01-01')
        self.assertIsNone(self.helper.stdev(5))


class TestPriceHistoryHelperRealData(unittest.TestCase):
    """
    Unit test class for PriceHistoryHelper using real data.
    """

    def test_init_data(self):
        """
        Test the initialization of data from a real source.

        - Check if the data is retrieved successfully.
        - Check if the standard deviation can be calculated with the retrieved data.
        """
        data = get_json_data("http://localhost:3000/stock-price/history?code=BFC&from=2023-07-01")

        if data is not None:
            helper = PriceHistoryHelper(data)
            helper.set_date("2023-08-18")
            stdev = helper.stdev(7)
            self.assertIsNot(stdev, None)


if __name__ == "__main__":
    unittest.main()
