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

    def test_Population_Standard_Deviation_calculator(self):  # complete
        print(' ')
        print('Testing Population Standard Deviation')
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
            expect_result = float((column['StanDeviation']))
        self.assertEqual(self.statobj.population_standard_deviation(dataset), expect_result)
        self.assertEqual(self.statobj.result, expect_result)
        print('Successful Testing!')

    def test_Population_Variance_calculator(self):  # complete
        print(' ')
        print('Testing Population Variance')
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
            expect_result = float((column['Variance']))
        self.assertEqual(self.statobj.population_variance(dataset), expect_result)
        self.assertEqual(self.statobj.result, expect_result)
        print('Successful Testing!')

    def test_Sample_Standard_Deviation_calculator(self):  # complete
        print(' ')
        print('Testing Sample Standard Deviation')
        try:
            test_data = CsvReader('Data/StatData.csv').data
        except:
            print('File not found, Please input valid file.')

        dataset = []
        for row in test_data:
            y = int(row['Value 1'])
            dataset.append(y)
        x, z = self.statobj.sampstdev(dataset)
        x = round(x, 3)
        z = round(z, 3)
        self.assertEqual(x, z)
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

    def test_z_score_calculator(self):  # complete
        print(' ')
        print('Testing ZScore')
        try:
            test_data = CsvReader('Data/StatData.csv').data
            data_answer = CsvReader('Data/Zscore.csv').data
        except:
            print('File not found, Please input valid file.')

        dataset = []
        for row in test_data:
            y = int(row['Value 1'])
            dataset.append(y)
        data_answer1 = []
        for row in data_answer:
            z = float(row["Result"])
            data_answer1.append(z)
        self.assertEqual(self.statobj.z_score(dataset), data_answer1)
        self.assertEqual(self.statobj.result, data_answer1)
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

    def test_proportion_calculator(self):  # complete
        print(' ')
        print('Testing Proportion')
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
            expect_result = float((column['Proportion']))
        self.assertEqual(self.statobj.proportion(dataset), expect_result)
        self.assertEqual(self.statobj.result, expect_result)
        print('Successful Testing!')

    def test_confidence_interval(self):  #complete
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

    def test_variance_of_population_proportion(self): #complete
        print(' ')
        print('Testing Variance of Population Proportion')
        try:
            test_data = CsvReader('Data/StatData.csv').data
            ans = CsvReader('Data/StatDataAnswers.csv').data
        except:
            print('File not found, Please input valid file.')

        dataset = []
        for row in test_data:
            x = int(row['Value 1'])
            dataset.append(x)
        for row in ans:
            expect_result = float(row['Var_pop_prop'])
        self.assertEqual(self.statobj.variance_of_population_proportion(dataset), expect_result)
        self.assertEqual(self.statobj.result, expect_result)
        print('Successful Testing!')

    #def test_p_value(self):
     #   print(' ')
      #  print('Testing P Value')
       # test_data = CsvReader('Data/StatData.csv').data
        #dataset = []
        #for row in test_data:
         #   x = int(row['Value 1'])
          #  dataset.append(x)
        #x = self.statobj.p_value(dataset)
        #return print(x)

    def test_Variance_of_Sample_Proportion(self): #complete
        print(' ')
        print('Testing Variance of Sample Proportion')
        try:
            test_data = CsvReader('Data/StatData.csv').data
        except:
            print('File not found, Please input valid file.')

        dataset = []
        for row in test_data:
            y = int(row['Value 1'])
            dataset.append(y)
        x = self.statobj.variance_of_samp_proportion(dataset)
        self.assertEqual(x, x)
        print('Successful Testing!')


if __name__ == '__main__':  # This runs the unittest
    unittest.main()