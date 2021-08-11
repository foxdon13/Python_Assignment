import itertools


class sumtozero:
    def __init__(self, numbers):
        self._numbers = numbers

    def calculations(self):
        three_combination_list = list(itertools.combinations(self._numbers, 3))
        sum_to_zero = [
            num_list for num_list in three_combination_list if sum(num_list) == 0
        ]
        # print
        print(sum_to_zero)
        # return if neccesary
        return sum_to_zero


s1 = sumtozero([-25, -10, -7, -3, 2, 4, 8, 10])
s1.calculations()
