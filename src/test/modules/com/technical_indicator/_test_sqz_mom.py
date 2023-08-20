import unittest

from modules.com.technical_indicator.sqz_mom import SqzMomConfig, SqzMom
import json
import os

cur_path = os.path.dirname(__file__)
string_to_remove = 'modules/com/technical_indicator'
index = cur_path.find(string_to_remove)
new_cur_path = cur_path[:index] + cur_path[index + len(string_to_remove):]
f = open(new_cur_path + 'mock_data/bfc_history_small.json')
data = json.load(f)


class TestSqzMom(unittest.TestCase):
    def setUp(self):
        """
        Set up the test environment by preparing data for each test case.
        """
        sqz_config = SqzMomConfig()
        self.sqz = SqzMom(data)
        self.sqz.set_config(sqz_config)

    def test_get_value(self):
        sqzs = []
        for i in range(3):
            date = data[i]['date']
            value, sqzOn, sqzOff, noSqz = self.sqz.set_date(date).get_data()
            sqzs.append(value)

        expected = [-422, -207, -150]
        self.assertEqual(sqzs, expected)
