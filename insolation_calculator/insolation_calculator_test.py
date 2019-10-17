import unittest
import xarray

from insolation_calculator import InsolationCalculator


class InsolationCalculatorTest(unittest.TestCase):

    def test_accepts_args(self):
        expected_latitude = 0.1
        calc = InsolationCalculator(latitude=expected_latitude)
        self.assertEqual(calc.latitude, expected_latitude)

    def test_calculate_days_average(self):
        expected_latitude = 0.1
        day = 1
        calc = InsolationCalculator(latitude=expected_latitude)
        returned_value = calc.calculate_days_average(day)
        self.assertTrue(isinstance(
            returned_value, xarray.core.dataarray.DataArray))
        self.assertTrue(len(returned_value.to_dict()['data']) > 0)


if __name__ == '__main__':
    unittest.main()
