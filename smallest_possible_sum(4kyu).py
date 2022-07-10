# https://www.codewars.com/kata/52f677797c461daaf7000740/train/python
# Description
# Given an array X of positive integers, its elements are to be transformed by running the following operation
# on them as many times as required:
#
# if X[i] > X[j] then X[i] = X[i] - X[j]
#
# When no more transformations are possible, return its sum ("smallest possible sum").
#
# For instance, the successive transformation of the elements of input X = [6, 9, 21] is detailed below:
#
# X_1 = [6, 9, 12] # -> X_1[2] = X[2] - X[1] = 21 - 9
# X_2 = [6, 9, 6]  # -> X_2[2] = X_1[2] - X_1[0] = 12 - 6
# X_3 = [6, 3, 6]  # -> X_3[1] = X_2[1] - X_2[0] = 9 - 6
# X_4 = [6, 3, 3]  # -> X_4[2] = X_3[2] - X_3[1] = 6 - 3
# X_5 = [3, 3, 3]  # -> X_5[1] = X_4[0] - X_4[1] = 6 - 3
# The returning output is the sum of the final transformation (here 9).
#
# Example
# solution([6, 9, 21]) #-> 9
# Solution steps:
# [6, 9, 12] #-> X[2] = 21 - 9
# [6, 9, 6] #-> X[2] = 12 - 6
# [6, 3, 6] #-> X[1] = 9 - 6
# [6, 3, 3] #-> X[2] = 6 - 3
# [3, 3, 3] #-> X[1] = 6 - 3
# Additional notes:
# There are performance tests consisted of very big numbers and arrays of size at least 30000. Please write
# an efficient algorithm to prevent timeout.
from random import randint, randrange
from math import gcd
from functools import reduce


def solution(a):
    # a_set_list = sorted(list(set(a)), reverse=True)
    # while len(set(a_set_list)) != 1:
    #     a_set_list[0] -= a_set_list[1]
    #     a_set_list = sorted(list(set(a_set_list)), reverse=True)
    # return a_set_list[0] * len(a)
    # a_set_list = list(set(a))
    return reduce(gcd, a) * len(a)




# print(solution([9]))
# print(solution([6, 9, 21]))
# print(solution([1, 21, 55]))
arr_list = [randint(50, 50000)*2 for x in range(40000)]
# print(arr_list)
print(solution(arr_list))
# print(solution([94, 90, 96, 95, 82, 97, 85, 94, 82, 89, 94, 82, 95, 95, 98, 84, 97, 81, 98, 99, 80, 97, 82, 95, 87, 85, 84, 96, 81, 90]))
# arr = list(map(lambda n: n*max(floor(n/2),1), [n * 2 for n in randint(50, 500, size=randrange(30000, 50000))]))
