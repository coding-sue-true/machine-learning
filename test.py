import pandas as pd
import numpy as np

# Create series from NumPy array
my_simple_series = pd.Series(np.random.randn(
    7), index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])
# print(my_simple_series)
# print(my_simple_series.index)


# Create series from NumPy array, without explicit index
my_simple_series = pd.Series(np.random.randn(5))
# print(my_simple_series)
# print(my_simple_series[:3])

# Create series from Python dictionary
my_dictionary = {'a': 45., 'b': -19.5, 'c': 4444}
my_second_series = pd.Series(my_dictionary)
# print(my_second_series)
# print(my_second_series['b'])

# Order of display is the same as order in index [b,c,d,a]
my_second_series = pd.Series(my_dictionary, index=['b', 'c', 'd', 'a'])
# print(my_second_series)
# print(my_second_series.get('a'))

# Check type
unknown = my_second_series.get('f')
# print(type(unknown))

# Create series from scalar
my_third_series = pd.Series(5., index=['a', 'b', 'c', 'd', 'e'])
# print(my_third_series)


# Vectorized operations
my_dictionary = {'a': 45., 'b': -19.5, 'c': 4444}
my_series = pd.Series(my_dictionary)
# print(my_series + my_series)


# Apply Python functions on an element-by-element basis
def multiply_by_ten(input_element):
    return input_element * 10.0


# print(multiply_by_ten(20))
# print(my_series.map(multiply_by_ten))


# Vectorized string methods
series_of_strings = pd.Series(
    ['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])

print(series_of_strings.str.lower())
