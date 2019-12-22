import unittest
from Statistics.Statistics import Statistics
from CSVReading.CSVReading import CsvReader


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statobj = Statistics('Data/StatData.csv')

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statobj, Statistics)

    def test_decorator_calculator(self):
        self.assertIsInstance(self.statobj, Statistics)

    def test_Population_Mean_calculator(self):  # complete
        print(' ')
        print('Testing Population Mean')
        try:
            test_data = CsvReader('Data/StatData.csv').data
            answer = CsvReader('Data/StatDataAnswers.csv').data
        except:
            print('File not found, Please input valid file.')

        dataset = []
        for row in test_data:
            a = int(row['Value 1'])
            dataset.append(a)
        for column in answer:
            expect_result = float((column['Mean']))
        self.assertEqual(self.statobj.population_mean(dataset), expect_result)
        self.assertEqual(self.statobj.result, expect_result)
        print('Successful Testing!')

    def test_Median_calculator(self):  # complete
        print(' ')
        print('Testing Population Median')
        try:
            test_data = CsvReader('Data/StatData.csv').data
            answer = CsvReader('Data/StatDataAnswers.csv').data
        except:
            print('File not found, Please input valid file.')

        dataset = []
        for row in test_data:
            y = int(row['Value 1'])
            dataset.append(y)
        for column in answer:
            expect_result = float((column['Median']))
        self.assertEqual(self.statobj.population_median(dataset), expect_result)
        self.assertEqual(self.statobj.result, expect_result)
        print('Successful Testing!')

    def test_Mode_calculator(self):  # complete
        print(' ')
        print('Testing Population Mode')
        try:
            test_data = CsvReader('Data/StatData.csv').data
            answer = CsvReader('Data/StatDataAnswers.csv').data
        except:
            print('File not found, Please input valid file.')

        dataset = []
        for row in test_data:
            y = int(row['Value 1'])
            dataset.append(y)
        for column in answer:
            expect_result = float((column['Mode']))
        self.assertEqual(self.statobj.population_mode(dataset), expect_result)
        self.assertEqual(self.statobj.result, expect_result)
        print('Successful Testing!')

    def test_Sample_Mean_calculator(self):  # complete
        print(' ')
        print('Testing Sample Mean')
        try:
            test_data = CsvReader('Data/StatData.csv').data
        except:
            print('File not found, Please input valid file.')

        dataset = []
        for row in test_data:
            y = int(row['Value 1'])
            dataset.append(y)
        x, z = self.statobj.samplemean(dataset)
        self.assertEqual(x, z)
        print('Successful Testing!')

    def test_population_correlation_coefficient(self):  # complete
        print(' ')
        print('Testing Population Correlation Coefficient')
        try:
            test_data = CsvReader('Data/StatData.csv').data
            test_data2 = CsvReader('Data/data2.csv').data
            ans = CsvReader('Data/StatDataAnswers.csv').data
        except:
            print('File not found, Please input valid file.')

        dataset = []
        for row in test_data:
            y = int(row['Value 1'])
            dataset.append(y)
        dataset2 = []
        for row in test_data2:
            k = float(row['Result'])
            dataset2.append(k)
        for row in ans:
            expect_result = float(row['Pop_corrcoef'])
        self.assertEqual(self.statobj.population_correlation_coefficient(dataset, dataset2), expect_result)
        self.assertEqual(self.statobj.result, expect_result)
        print('Successful Testing!')

    def test_confidence_interval(self):  # complete
        print(' ')
        print('Testing Confidence Interval')
        try:
            test_data = CsvReader('Data/StatData.csv').data
            ans = CsvReader('Data/confidenceresult.csv').data
        except:
            print('File not found, Please input valid file.')

        dataset = []
        for row in test_data:
            x = int(row['Value 1'])
            dataset.append(x)
        expect_result = []
        for row in ans:
            y = float(row['Result'])
            expect_result.append(y)
        self.assertEqual(self.statobj.population_confidence_interval(dataset), expect_result)
        print('Successful Testing!')


if __name__ == '__main__':  # This runs the unittest
    unittest.main()
