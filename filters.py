import numpy as np
import copy

class RangeFilter:
    """
    The range_filter object

    Attributes:

        min_range (int): used to determine if a measurement is below this value,
        default value is set to 0.03
        max_range (int): used to determine if a measurement is above this value,
        default value is set to 50.0
    """
    def __init__(self,min_range=0.03,max_range=50.0):
        self.__min_range = min_range
        self.__max_range = max_range
        self.__check_args()

    def __check_args(self):
        self.__check_args_type()
        self.__check_args_val()

    def __check_args_type(self):
        """Checks that min_range and max_range are int or float types

        Raises:

            TypeError: Invalid type
        """
        if not isinstance(self.__min_range, (float, int)):
            error_msg = "min_range must of type int or float, but given: "
            error_msg += str(type(self.__min_range))
            raise TypeError(error_msg)
        elif not isinstance(self.__max_range, (float, int)):
            error_msg = "max_range must of type int or float, but given: "
            error_msg += str(type(self.__max_range))
            raise TypeError(error_msg)

        if isinstance(self.__min_range, bool):
            error_msg = "min_range must of type int or float, but given: "
            error_msg += str(type(self.__min_range))
            raise TypeError(error_msg)
        elif isinstance(self.__max_range, bool):
            error_msg = "max_range must of type int or float, but given: "
            error_msg += str(type(self.__max_range))
            raise TypeError(error_msg)

    def __check_args_val(self):
        """Checks that min_range and max_range are valid and logical values

        Raises:

            ValueError: Invalid value
        """
        if self.__min_range < 0:
            error_msg = "min_range must be greater than or equal to zero"
            raise ValueError(error_msg)
        elif self.__max_range < 0:
            error_msg = "max_range must be greater than or equal to zero"
            raise ValueError(error_msg)
        elif self.__max_range < self.__min_range:
            error_msg = "max_range must be greater than or equal to min_range"
            raise ValueError(error_msg)

    def change_min_range(self, min_range):
        self.__check_args()
        self.__min_range = min_range

    def change_max_range(self, max_range):
        self.__checkArgs()
        self.__max_range = max_range

    def update(self,scan):
        """Replaces measurements in scan by min_range or max_range if
        measurement below or above them respectively

        Args:

            scan (list or numpy.ndarray): list or numpy.ndarray of values

        Raises:

            TypeError: scan is the wrong type
            ValueError: scan is a multidimensional list or numpy.ndarray not a
            single vector

        Returns:

            scan_list (list): a list of updated measurements
        """

        # Convert the data to an numpy.ndarray and reszie to ensure it
        # is a 1D vector
        if not isinstance(scan, (list, np.ndarray)):
            error_msg = "Arg wrong type, expected 'list' or 'numpy.ndarray'"
            raise TypeError(error_msg)
        else:
            scan_array = np.asarray(scan)
            element_count = scan_array.size
            scan_array.shape = (element_count)

        for index in range(scan_array.size):
            if scan_array[index] < self.__min_range:
                scan_array[index] = self.__min_range
            elif scan_array[index] > self.__max_range:
                scan_array[index] = self.__max_range

        scan_list = scan_array.tolist()
        return scan_list

class TemporalMedianFilter:
    """
    The temporal_median_filter object

    Attributes:
        num_prev_scans (int): used to store that many previous scans, default
        value is 3
    """
    def __init__(self, num_prev_scans=3):
        self.__N = 0;   # num of data points in scan
        self.__num_prev_scans = num_prev_scans
        self.__ordered_data = np.array([[]])
        self.__unordered_data = np.array([[]])
        self.__check_args()

    def __check_args(self):
        """Checks that num_prev_scans is the correct data type and value
        """
        self.__check_args_type()
        self.__check_args_val()

    def __check_args_type(self):
        """Checks that num_prev_scans is int

        Raises:
            TypeError: Invalid type
        """
        if not isinstance(self.__num_prev_scans, int):
            error_msg = "num_prev_scans must of type 'int', but given '"
            error_msg += str(type(self.__num_prev_scans))+ "'"
            raise TypeError(error_msg)

        if isinstance(self.__num_prev_scans, bool):
            error_msg = "num_prev_scans must of type 'int', but given '"
            error_msg += str(type(self.__num_prev_scans))+ "'"
            raise TypeError(error_msg)

    def __check_args_val(self):
        """Checks that num_prev_scans is positive

        Raises:

            ValueError: Invalid value
        """
        if self.__num_prev_scans < 0:
            error_msg = "num_prev_scans must be greater than or equal to zero"
            raise ValueError(error_msg)

    def update(self, scan):
        """Determines the median of the current scan with num_prev_scans

        Args:

            scan (list or numpy.ndarray): a set of measurements

        Raises:

            TypeError: scan is the wrong type
            ValueError: the number of datapoints in scan not consistent with
            previous scans

        Returns:

            median_val (list): scan with median values determined from
            current and num_prev_scans

        """

        # Check the input type and convert to ndarray if a list
        # and ensure that the input is a 1D vector
        if not isinstance(scan, (list, np.ndarray)):
            error_msg = "argument wrong type, expected list or numpy.ndarray"
            raise TypeError(error_msg)
        else:
            scan_array = np.asarray(scan)
            element_count = scan_array.size
            scan_array.shape = (element_count)

        # Remove the last entry in the array to maintain num_prev_scans
        # most recent scans
        num_scans = self.__unordered_data.shape[0]
        if num_scans > self.__num_prev_scans:
            num_scans-=1
            self.__unordered_data = \
                np.delete(self.__unordered_data, num_scans,axis=0)

        # Return the scan if it is the very first input into the array
        if self.__unordered_data.size == 0:
            self.__N = scan_array.size;
            self.__unordered_data = np.vstack([scan_array])
            return self.__unordered_data[0].tolist()
        else:
            # Check every scan has same number of measurements as first scan
            if scan_array.size != self.__N:
                raise ValueError("number of data points not consistent")
            else:
                self.__unordered_data = \
                    np.vstack([scan_array, self.__unordered_data])
                self.__ordered_data = copy.deepcopy(self.__unordered_data)
                num_scans+=1

        # sort by column
        self.__ordered_data.sort(axis=0)

        # determine the median val for each column
        if num_scans%2:
            median_val = self.__ordered_data[(num_scans + 1) / 2 - 1, :]
        else:
            median_val_1 = self.__ordered_data[num_scans / 2 - 1, :]
            median_val_2 = self.__ordered_data[(num_scans + 2) / 2 - 1, :]
            median_val = (median_val_1 + median_val_2) / 2.0

        median_val = median_val.tolist()
        return median_val
