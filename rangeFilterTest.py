import numpy as np
import unittest
from filters import RangeFilter


class TestRangeFilter(unittest.TestCase):

    def setUp(self):
        self.filter = RangeFilter(0.03, 50.0)

    def test_min_max_range_replacement_for_filled_numpy_array(self):
        scan_array = np.array([-1.0,0.0,30.0,50.0,100.0])
        expected_result = [0.03,0.03,30.0,50.0,50.0]
        actual_result = self.filter.update(scan_array)
        self.assertEqual(expected_result, actual_result)

    def test_min_max_range_replacement_for_empty_numpy_array(self):
        scan_array = np.array([])
        expected_result = []
        actual_result = self.filter.update(scan_array)
        self.assertEqual(expected_result, actual_result)

    def test_min_max_range_replacement_for_filled_list(self):
        scan_list = [-1.0,0.0,30.0,50.0,100.0]
        expected_result = [0.03,0.03,30.0,50.0,50.0]
        actual_result = self.filter.update(scan_list)
        self.assertEqual(expected_result, actual_result)

    def test_min_max_range_replacement_for_empty_list(self):
        scan_list = []
        expected_result = []
        actual_result = self.filter.update(scan_list)
        self.assertEqual(expected_result, actual_result)

    def test_negative_min_range(self):
        with self.assertRaises(ValueError):
            self.test_filter = RangeFilter(min_range=-0.03)

    def test_negative_max_range(self):
        with self.assertRaises(ValueError):
            self.test_filter = RangeFilter(max_range=-50.0)

    def test_min_range_greater_than_max_range(self):
        with self.assertRaises(ValueError):
            self.test_filter = RangeFilter(min_range=10.0, max_range=5.0)

    def test_equal_min_max_range_for_filled_numpy_array(self):
        self.test_filter = RangeFilter(min_range=50.0,max_range=50.0)
        scan_array = np.array([-1.0,0.0,30.0,50.0,100.0])
        expected_result = [50.0,50.0,50.0,50.0,50.0]
        actual_result = self.test_filter.update(scan_array)
        self.assertEqual(expected_result, actual_result)

    def test_equal_min_max_range_for_empty_numpy_array(self):
        self.test_filter = RangeFilter(min_range=50.0,max_range=50.0)
        scan_array = np.array([])
        expected_result = []
        actual_result = self.test_filter.update(scan_array)
        self.assertEqual(expected_result, actual_result)

    def test_equal_min_max_range_for_filled_list(self):
        self.test_filter = RangeFilter(min_range=50.0,max_range=50.0)
        scan_list= [-1.0,0.0,30.0,50.0,100.0]
        expected_result = [50.0,50.0,50.0,50.0,50.0]
        actual_result = self.test_filter.update(scan_list)
        self.assertEqual(expected_result, actual_result)

    def test_equal_min_max_range_for_empty_list(self):
        self.test_filter = RangeFilter(min_range=50.0,max_range=50.0)
        scan_list= []
        expected_result = []
        actual_result = self.test_filter.update(scan_list)
        self.assertEqual(expected_result, actual_result)

    def test_argument_as_one_row_n_columns_numpy_array(self):
        scan_array = np.array([[-1.0,0.0,30.0,50.0,97.5,-0.5]])
        expected_result = [0.03,0.03,30.0,50,50.0,0.03]
        actual_result = self.filter.update(scan_array)
        self.assertEqual(expected_result,actual_result)

    def test_argument_as_n_rows_one_column_numpy_array(self):
        scan_array = np.array([[-1.0],[0.0],[30.0],[50.0],[97.5],[-0.5]])
        expected_result = [0.03,0.03,30.0,50,50.0,0.03]
        actual_result = self.filter.update(scan_array)
        self.assertEqual(expected_result,actual_result)

    def test_argument_as_m_rows_n_column_numpy_array(self):
        scan_array = np.array([[-1.0,0.0],[30.0,50.0],[97.5,-0.025]])
        expected_result = [0.03,0.03,30.0,50,50.0,0.03]
        actual_result = self.filter.update(scan_array)
        self.assertEqual(expected_result,actual_result)

    def test_argument_as_one_row_n_columns_list(self):
        scan_list = [[-1.0,0.0,30.0,50.0,97.5,-0.5]]
        expected_result = [0.03,0.03,30.0,50,50.0,0.03]
        actual_result = self.filter.update(scan_list)
        self.assertEqual(expected_result,actual_result)

    def test_argument_as_n_rows_one_column_list(self):
        scan_list = [[-1.0],[0.0],[30.0],[50.0],[97.5],[-0.5]]
        expected_result = [0.03,0.03,30.0,50,50.0,0.03]
        actual_result = self.filter.update(scan_list)
        self.assertEqual(expected_result,actual_result)

    def test_argument_as_m_rows_n_column_list(self):
        scan_list = [[-1.0,0.0],[30.0,50.0],[97.5,-0.025]]
        expected_result = [0.03,0.03,30.0,50,50.0,0.03]
        actual_result = self.filter.update(scan_list)
        self.assertEqual(expected_result,actual_result)


    def test_wrong_min_range_type_char(self):
        with self.assertRaises(TypeError):
            self.test_filter = RangeFilter(min_range='a')
    def test_wrong_min_range_type_string(self):
        with self.assertRaises(TypeError):
            self.test_filter = RangeFilter(min_range="Hello World")
    def test_wrong_min_range_type_complex(self):
        with self.assertRaises(TypeError):
            self.test_filter = RangeFilter(min_range=5+4j)
    def test_wrong_min_range_type_bool(self):
        with self.assertRaises(TypeError):
            self.test_filter = RangeFilter(min_range=True)
    def test_wrong_min_range_type_None(self):
        with self.assertRaises(TypeError):
            self.test_filter = RangeFilter(min_range=None)

    def test_wrong_max_range_type_char(self):
        with self.assertRaises(TypeError):
            self.test_filter = RangeFilter(max_range='a')
    def test_wrong_max_range_type_string(self):
        with self.assertRaises(TypeError):
            self.test_filter = RangeFilter(max_range="Hello World")
    def test_wrong_max_range_type_complex(self):
        with self.assertRaises(TypeError):
            self.test_filter = RangeFilter(max_range=5+4j)
    def test_wrong_max_range_type_bool(self):
        with self.assertRaises(TypeError):
            self.test_filter = RangeFilter(max_range=True)
    def test_wrong_max_range_type_None(self):
        with self.assertRaises(TypeError):
            self.test_filter = RangeFilter(max_range=None)



if __name__ == '__main__':
    unittest.main(verbosity=2)
