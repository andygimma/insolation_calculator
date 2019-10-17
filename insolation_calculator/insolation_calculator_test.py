import unittest
import insolation_calculator


class InsolationCalculatorTest(unittest.TestCase):

    def test_accepts_args(self):
        expected_latitude = 0.1
        calc = insolation_calculator.InsolationCalculator(
            latitude=expected_latitude)
        self.assertEqual(calc.latitude, expected_latitude)


if __name__ == '__main__':
    unittest.main()
