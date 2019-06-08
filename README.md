# 1. Purpose

filters.py implements two classes, RangeFilter and TemporalMedianFilter.

```python
range_filter = RangeFilter(min_range=0.03, max_range=50.0)
median_filter = TemporalMedianFilter(num_prev_scans=3)
```

# 2. Dependencies

Python version 2.7.x and Numpy v1.16.x required



# 3. Usage

To learn more about the class and the update method that is used which implements the filter for each class, the following python script will aid in this process:

```python
from filters import RangeFilter
from filters import TemporalMedianFilter

print RangeFilter.__doc__
print TemporalMedianFilter.__doc__
print RangeFilter.update.__doc__
print TemporalMedianFilter.__doc__
```

## 3.1 RangeFilter

The RangeFitlter class expects two attrbitures:

1. min_range: default value of 0.03 if value not provided
2. max_range: default value of 50.0 if value not provided

The attributes are expected to be int or float data types, another data type will result in a TypeError being raised. Futhermore the min_range and max_range must be values postive values greater than or equal to zero and the max_range must be greater than or equal to the min_range. Any other values will result in a ValueError being raised.



### 3.1.1 RangeFilter.update

The update method will apply the RangeFilter logic (example usage will be shown further down). The input of the method is either a list or numpy.ndarray, any other datatype will result in a TypeError being raised. The return type of the method is always a single row list.



## 3.2 TemporalMedianFilter

The TemporalMedianFilter class has one attribute:

1. num_prev_scans: number of previous data streams that will be stored in an array, If no value is provided default value is 3 

If a negative value is provided a ValueError is raised, furthermore the data type is expected to be an int ONLY. Any other value (even 3.0) will result in a TypeError being raised.



### 3.2.1 TemporalMedianFilter.update

The update method will apply the TemporalMedianFilter logic (example usage will be shown further down).  The input of the method is either a list or numpy.ndarray, any other datatype will result in a TypeError being raised. The return type of the method is always a single row list. 

The method can accpet either a list or numpy.ndarray becuase internally all data is converted to numpy.ndarray



# 3.3 Example

```python
import numpy as np
from filters import RangeFilter
from filters import TemporalRangeFilter

def testing_range_filer():
	# Sample data as either an numpy.ndarray or list
	scan_array = np.array([0.01,-3,4.5,55.0])
	scan_list = [0.01,-3,4.5,55.0]

	# Expected results from calling update:
	# result_array == result_list == [0.03,0.03,4.5,50.0]
	range_filter = RangeFilter(min_range=0.03, max_range=50.0)
	result_array = range_filter.update(scan_array)
	result_list = range_filter.update(scan_list)

	# Sample data, this time a multi-dimensional numpy.ndarray or list
	scan_array = np.array([[0.01,-3,4.5,55.0],[0.01,-3,4.5,55.0]])
	scan_list = [[0.01,-3,4.5,55.0],[0.01,-3,4.5,55.0]]

	# Expected results from calling update:
	# result_array == result_list == [0.03,0.03,4.5,50.0,0.03,0.03,4.5,50.0]
	result_array = range_filter.update(scan_array)
	result_list = range_filter.update(scan_list)

def testing_temporal_median_filter():
    # Simulated data set
    scan_array = np.array([[0.0,1.0,2.0,1.0,3.0],\
                           [1.0,5.0,7.0,1.0,3.0],\
                           [2.0,3.0,4.0,1.0,0.0],\
                           [3.0,3.0,3.0,1.0,3.0],\
                           [10.0,2.0,4.0,0.0,0.0]])
    scan_list = [[0.0,1.0,2.0,1.0,3.0],\
                 [1.0,5.0,7.0,1.0,3.0],\
                 [2.0,3.0,4.0,1.0,0.0],\
                 [3.0,3.0,3.0,1.0,3.0],\
                 [10.0,2.0,4.0,0.0,0.0]]
    
    # Expected results from calling update:
    #	idx == 0, result_array == result_list == [0.0,1.0,2.0,1.0,3.0]
    #	idx == 1, result_array == result_list == [0.5,3.0,4.5,1.0,3.0]
    # 	idx == 2, result_array == result_list == [1.0,3.0,4.0,1.0,3.0]
    #	idx == 3, result_array == result_list == [1.5,3.0,3.5,1.0,3.0]
    #	idx == 4, result_array == result_list == [2.5,3.0,4.0,1.0,1.5]
    median_filter = TemporalMedianFilter(3)
    for idx in range(len(scan_list)):
        result_array = median_filter.update(scan_array[idx])
        result_list = median_filter.update(scan_list[idx])
    
    # An important note:
    # if .update has an input that is an m x n list or numpy.ndarray
    # it will be converted to a single column vector which contains
    # m x n number of values, and as such a column vector with m x n
    # values is returned.
    # an example is shown below:
    median_filter = TemporalMedianFilter(0)
    result_array = median_filter.update(scan_array)
    
    # the result array will be the following:
    #	result_array = [0.0,1.0,2.0,1.0,3.0,1.0,5.0,7.0,1.0,3.0,2.0,3.0,4.0,1.0,0.0,\
    #					3.0,3.0,3.0,1.0,3.0,10.0,2.0,4.0,0.0,0.0]
    



```

