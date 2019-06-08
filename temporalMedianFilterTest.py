import numpy as np
import unittest
from filters import TemporalMedianFilter


class TestTemporalMedianFilter(unittest.TestCase):

    def test_median_filter_zero_previous_scans_with_numpy_array(self):
        self.filter = TemporalMedianFilter(0)
        scan_array  = np.array([[0.0,1.0,2.0,1.0,3.0],
                                [1.0,5.0,7.0,1.0,3.0],
                                [2.0,3.0,4.0,1.0,0.0],
                                [3.0,3.0,3.0,1.0,3.0],
                                [10.0,2.0,4.0,0.0,0.0]])
        expected_result = scan_array.tolist()
        num_scans = scan_array.shape[0]
        for idx in range(num_scans):
            actual_result = self.filter.update(scan_array[idx])
            self.assertEqual(expected_result[idx],actual_result)

    def test_median_filter_zero_previous_scans_with_list(self):
        self.filter = TemporalMedianFilter(0)
        scan_list = [[0.0,1.0,2.0,1.0,3.0],
                    [1.0,5.0,7.0,1.0,3.0],
                    [2.0,3.0,4.0,1.0,0.0],
                    [3.0,3.0,3.0,1.0,3.0],
                    [10.0,2.0,4.0,0.0,0.0]]
        expected_result = scan_list
        num_scans = len(scan_list)
        for idx in range(num_scans):
            actual_result = self.filter.update(scan_list[idx])
            self.assertEqual(expected_result[idx],actual_result)

    def test_median_filter_three_previous_scans_with_numpy_array(self):
        self.filter = TemporalMedianFilter(3)
        scan_array = np.array([[0.0,1.0,2.0,1.0,3.0],
                                [1.0,5.0,7.0,1.0,3.0],
                                [2.0,3.0,4.0,1.0,0.0],
                                [3.0,3.0,3.0,1.0,3.0],
                                [10.0,2.0,4.0,0.0,0.0]])

        expected_result = [[0.0,1.0,2.0,1.0,3.0],
                            [0.5,3.0,4.5,1.0,3.0],
                            [1.0,3.0,4.0,1.0,3.0],
                            [1.5,3.0,3.5,1.0,3.0],
                            [2.5,3.0,4.0,1.0,1.5]]
        num_scans = scan_array.shape[0]
        for idx in range(num_scans):
            actual_result = self.filter.update(scan_array[idx])
            self.assertEqual(expected_result[idx],actual_result)

    def test_median_filter_three_previous_scans_with_list(self):
        self.filter = TemporalMedianFilter(3)
        scan_list = [[0.0,1.0,2.0,1.0,3.0],
                    [1.0,5.0,7.0,1.0,3.0],
                    [2.0,3.0,4.0,1.0,0.0],
                    [3.0,3.0,3.0,1.0,3.0],
                    [10.0,2.0,4.0,0.0,0.0]]

        expected_result = [[0.0,1.0,2.0,1.0,3.0],
                            [0.5,3.0,4.5,1.0,3.0],
                            [1.0,3.0,4.0,1.0,3.0],
                            [1.5,3.0,3.5,1.0,3.0],
                            [2.5,3.0,4.0,1.0,1.5]]
        num_scans = len(scan_list)
        for idx in range(num_scans):
            actual_result = self.filter.update(scan_list[idx])
            self.assertEqual(expected_result[idx],actual_result)

    def test_median_filter_five_previous_scans_with_numpy_array(self):
        self.filter = TemporalMedianFilter(5)
        scan_array = np.array([[0.0,1.0,2.0,1.0,3.0],
                                [1.0,5.0,7.0,1.0,3.0],
                                [2.0,3.0,4.0,1.0,0.0],
                                [3.0,3.0,3.0,1.0,3.0],
                                [10.0,2.0,4.0,0.0,0.0]])

        expected_result = [[0.0,1.0,2.0,1.0,3.0],
                            [0.5,3.0,4.5,1.0,3.0],
                            [1.0,3.0,4.0,1.0,3.0],
                            [1.5,3.0,3.5,1.0,3.0],
                            [2.0,3.0,4.0,1.0,3.0]]
        num_scans = scan_array.shape[0]
        for idx in range(num_scans):
            actual_result = self.filter.update(scan_array[idx])
            self.assertEqual(expected_result[idx],actual_result)


    def test_median_filter_inconsistent_num_measurement_numpy_array(self):
        self.filter = TemporalMedianFilter(3)
        scan_array = np.array([[0.0,1.0],
                                [1.0,5.0,7.0,1.0,3.0],
                                [2.0,3.0,4.0,1.0,0.0],
                                [3.0,3.0,3.0,1.0,3.0],
                                [10.0,2.0,4.0,0.0,0.0]])

        num_scans = scan_array.shape[0]
        for idx in range(num_scans):
            try:
                actual_result = self.filter.update(scan_array[idx])
            except ValueError:
                with self.assertRaises(ValueError):
                        actual_result = self.filter.update(scan_array[idx])

    def test_median_filter_inconsistent_num_measurement_list(self):
        self.filter = TemporalMedianFilter(3)
        scan_list = [[0.0,1.0],
                    [1.0,5.0,7.0,1.0,3.0],
                    [2.0,3.0,4.0,1.0,0.0],
                    [3.0,3.0,3.0,1.0,3.0],
                    [10.0,2.0,4.0,0.0,0.0]]

        num_scans = len(scan_list)
        for idx in range(num_scans):
            try:
                actual_result = self.filter.update(scan_list[idx])
            except ValueError:
                with self.assertRaises(ValueError):
                        actual_result = self.filter.update(scan_list[idx])

    def test_median_filter_five_previous_scans_with_numpy_list(self):
        self.filter = TemporalMedianFilter(5)
        scan_list = [[0.0,1.0,2.0,1.0,3.0],
                        [1.0,5.0,7.0,1.0,3.0],
                        [2.0,3.0,4.0,1.0,0.0],
                        [3.0,3.0,3.0,1.0,3.0],
                        [10.0,2.0,4.0,0.0,0.0]]

        expected_result = [[0.0,1.0,2.0,1.0,3.0],
                            [0.5,3.0,4.5,1.0,3.0],
                            [1.0,3.0,4.0,1.0,3.0],
                            [1.5,3.0,3.5,1.0,3.0],
                            [2.0,3.0,4.0,1.0,3.0]]
        num_scans = len(scan_list)
        for idx in range(num_scans):
            actual_result = self.filter.update(scan_list[idx])
            self.assertEqual(expected_result[idx],actual_result)

    def test_negative_num_previous_scan(self):
        with self.assertRaises(ValueError):
            self.test_filter = TemporalMedianFilter(-1)

    def test_float_zero_point_three_num_previous_scan(self):
        with self.assertRaises(TypeError):
            self.test_filter = TemporalMedianFilter(0.5)

    def test_float_three_point_zero_num_previous_scan(self):
        with self.assertRaises(TypeError):
            self.test_filter = TemporalMedianFilter(3.0)

    def test_char_num_previous_scan(self):
        with self.assertRaises(TypeError):
            self.test_filter = TemporalMedianFilter('a')

    def test_string_num_previous_scan(self):
        with self.assertRaises(TypeError):
            self.test_filter = TemporalMedianFilter("Hello World")

    def test_bool_num_previous_scan(self):
        with self.assertRaises(TypeError):
            self.test_filter = TemporalMedianFilter(True)

    def test_complex_num_previous_scan(self):
        with self.assertRaises(TypeError):
            self.test_filter = TemporalMedianFilter(2+3j)

if __name__ == '__main__':
    unittest.main(verbosity=2)
