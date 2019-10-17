import unittest
import xarray

from insolation_calculator import InsolationCalculator


class InsolationCalculatorTest(unittest.TestCase):

    def test_accepts_args(self):
        expected_latitude = 0.1
        calc = InsolationCalculator(latitude=expected_latitude)
        self.assertEqual(calc.latitude, expected_latitude)

    def test_daily_insolation(self):
        # NOTE These assertions are very specific to the climlab library
        # and can be considered integration tests.
        expected_latitude = 0.1
        day = 1
        calc = InsolationCalculator(latitude=expected_latitude)
        returned_value = calc._daily_insolation(day=day)
        self.assertTrue(type(returned_value) == list)
        self.assertTrue(len(returned_value) > 0)

    def test_daily_average(self):
        expected_latitude = 0.1
        day = 1
        calc = InsolationCalculator(latitude=expected_latitude)
        returned_value = calc.daily_average(day=day)
        self.assertTrue(type(returned_value) == float)
        self.assertTrue(returned_value > 0)


if __name__ == '__main__':
    unittest.main()
