import unittest

from Calculator.Calculator import Calculator

from CSVReading.CSVReading import CsvReader


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_results(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add_method_calculator(self):
        print("Testing Addition")
        test_data = CsvReader('./Data/Unit Test Addition.csv').data
        for row in test_data:
            x = row['Value 1']
            y = row['Value 2']
            result = int(row['Result'])
            self.assertEqual(self.calculator.add(x, y), result)
            self.assertEqual(self.calculator.result, result)
        print("Successful Testing")

    def test_subtract_method_calculator(self):
        print(' ')
        print('Testing Subtraction')
        test_data = CsvReader('./Data/Unit Test Subtraction.csv').data
        for row in test_data:
            x = row['Value 1']
            y = row['Value 2']
            result = int(row['Result'])
            self.assertEqual(self.calculator.subtract(x, y), result)
            self.assertEqual(self.calculator.result, result)
        print("Successful Testing")

    def test_multiply_method_calculator(self):
        print(' ')
        print('Testing Multiplication')
        test_data = CsvReader('./Data/Unit Test Multiplication.csv').data
        for row in test_data:
            x = row['Value 1']
            y = row['Value 2']
            result = int(row['Result'])
            self.assertEqual(self.calculator.multiply(x, y), result)
            self.assertEqual(self.calculator.result, result)
        print("Successful Testing")

    def test_divide_method_calculator(self):
        print(' ')
        print('Testing Division')
        test_data = CsvReader('./Data/Unit Test Division.csv').data
        for row in test_data:
            x = row['Value 1']
            y = row['Value 2']
            result = float(row['Result'])
            self.assertEqual(self.calculator.divide(x, y), round(result, 7))
            self.assertEqual(self.calculator.result, round(result, 7))
        print("Successful Testing")

    def test_sqr_method_calculator(self):
        print(' ')
        print('Testing Squares')
        test_data = CsvReader('./Data/Unit Test Square.csv').data
        for row in test_data:
            x = row['Value 1']
            result = int(row['Result'])
            self.assertEqual(self.calculator.square(x), result)
            self.assertEqual(self.calculator.result, result)
        print("Successful Testing")

    def test_sqrrt_method_calculator(self):
        print(' ')
        print('Testing Square Roots')
        test_data = CsvReader('./Data/Unit Test Square Root.csv').data
        for row in test_data:
            x = row['Value 1']
            result = float(row['Result'])
            self.assertEqual(self.calculator.square_root(x), round(result, 8))
            self.assertEqual(self.calculator.result, round(result, 8))
        print('Successful Testing!')


if __name__ == '__main__':  # This runs the unittest
    unittest.main()