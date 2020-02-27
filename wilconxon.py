"""
Problem: Implement Wilconxon Signed Rank Test without any third party library
Company: Algo
Author: Vishvaraj Dhanawade
Email: vishvarajdhnwd120@gmail.com
"""

class WilconxonSignedRankTest:
    def __init__(self, arr, first_col, sec_col):
        self.arr = arr
        self.first_col = first_col
        self.sec_col = sec_col
        self.difference = []
        self.abs_difference = []
        self.rank = []
        self.test_negative = 0
        self.test_positive = 0

    def calculate_diff(self):
        # calculating difference betweek two products
        for row in self.arr:
            dval = row[self.sec_col] - row[self.first_col]
            self.difference.append(dval)
            self.abs_difference.append(abs(dval))

    def calculate_diff_with_arr(self, col1index, col2index):
        # for this we calculating values from other two columns
        # It is used for permutation of two column values
        for row in self.arr:
            avg_val = (row[col1index] + row[col2index])/2
            dval = avg_val - row[self.first_col]
            self.difference.append(dval)
            self.abs_difference.append(abs(dval))

    def rank_col(self):
        # Ranking values from lowest to highest
        values_abd = set(self.abs_difference)

        values_abd = sorted(values_abd)
        ranks = dict()
        for index, val in enumerate(values_abd, 1):
            ranks[val] = index

        for val in self.abs_difference:
            self.rank.append(ranks[val])

    def test_statistics(self):
        # calculating test statistics values for negative and positive
        for index, val in enumerate(self.rank):
            if self.difference[index] < 0:
                self.test_negative += val
            else:
                self.test_positive += val
