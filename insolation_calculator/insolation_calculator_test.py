import unittest
import xarray

from insolation_calculator import InsolationCalculator


class InsolationCalculatorTest(unittest.TestCase):

    def test_accepts_args(self):
        expected_latitude = 0.1
        calc = InsolationCalculator(latitude=expected_latitude)
        self.assertEqual(calc.latitude, expected_latitude)

    def test_calculate_days_average(self):
        # NOTE These assertions are very specific to the climlab library
        # and can be considered integration tests.
        expected_latitude = 0.1
        day = 1
        calc = InsolationCalculator(latitude=expected_latitude)
        returned_value = calc.calculate_days_average(day)
        self.assertTrue(type(returned_value) == list)


if __name__ == '__main__':
    unittest.main()
