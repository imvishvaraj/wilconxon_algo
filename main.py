"""
Problem: Implement Wilconxon Signed Rank Test without any third party library
Company: Algo
Author: Vishvaraj Dhanawade
Email: vishvarajdhnwd120@gmail.com
"""
import pyexcel as pe
from itertools import permutations
import warnings

from wilconxon import WilconxonSignedRankTest

warnings.filterwarnings("ignore", category=UserWarning)
# importing data form xlsx file
data = pe.get_array(file_name='AlgoTest.xlsx')

# Question 1:
# test_names, test statistics negative values, test statistics positive values
# col_names = ['Customer', 48806, 47106, 47287, 48020, 48863, 50546]
result = [[], [], []]

for column in data[0][2:]:
    temp = WilconxonSignedRankTest(data[1:], first_col=data[0].index(48806), sec_col=data[0].index(column))
    temp.calculate_diff()
    temp.rank_col()
    temp.test_statistics()
    result[0].append('test_48806_'+str(column))
    result[1].append(temp.test_negative)
    result[2].append(temp.test_positive)

print("\nQuestion 1:")
for index, val in enumerate(result[0]):
    colval = val.split('_')
    print("For {} and {} test statistic for negative is {} and positive is {}"
          .format(colval[1], colval[2], result[1][index], result[2][index]))


# Question 2
perm = permutations(data[0][2:], 2)
result_non_key_perm = [[], [], []]
for val in perm:
    temp = WilconxonSignedRankTest(data[1:], first_col=data[0].index(48806), sec_col=None)
    temp.calculate_diff_with_arr(col1index=data[0].index(val[0]), col2index=data[0].index(val[1]))
    temp.rank_col()
    temp.test_statistics()
    result_non_key_perm[0].append('test_48806_' + str(val[0]) + '_' + str(val[1]))
    result_non_key_perm[1].append(temp.test_negative)
    result_non_key_perm[2].append(temp.test_positive)

print("\nQuestion 2:")
for index, val in enumerate(result_non_key_perm[0]):
    colval = val.split('_')
    print("For {} and permutation of ({}, {}) test statistic for negative is {} and positive is {}"
          .format(colval[1], colval[2], colval[3], result_non_key_perm[1][index], result_non_key_perm[2][index]))


# Question 3
print("\nQuestion 3")
non_key = min(result[1])
non_key_index = result[1].index(non_key)
test_name_non_key = result[0][non_key_index]
non_key_cols = test_name_non_key.split('_')
print("Best Non-key column with {} is: {}".format(non_key_cols[1], non_key_cols[2]))


# Question 4
print("\nQuestion 4")
non_key_perm = min(result_non_key_perm[1])
non_key_index_perm = result_non_key_perm[1].index(non_key_perm)
test_name_non_key_perm = result_non_key_perm[0][non_key_index_perm]
non_key_cols_perm = test_name_non_key_perm.split('_')
print("Best Non-key column 48806 with permutation of ({}, {}). ".format(non_key_cols_perm[2], non_key_cols_perm[3]))
