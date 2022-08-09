# How many ways can you make the sum of a number?
# From wikipedia: https://en.wikipedia.org/wiki/Partition_(number_theory)#
#
# In number theory and combinatorics, a partition of a positive integer n,
# also called an integer partition, is a way of writing n as a sum of positive integers. T
# wo sums that differ only in the order of their summands are considered the same partition.
# If order matters, the sum becomes a composition.
# For example, 4 can be partitioned in five distinct ways:
# 4
# 3 + 1
# 2 + 2
# 2 + 1 + 1
# 1 + 1 + 1 + 1

# def exp_sum(n):
#     variant = [1 for i in range(n)]
#     i = 1
#     # min_index = 0
#     while len(variant) != 1:
#         # if min_index == len(variant)-1 or len(variant) == 2:
#         #     min_index = 0
#         # else:
#         #     min_index += 1
#         min_index = 0
#         for j in range(len(variant)-1):
#             if variant[j]<variant[min_index]:
#                 min_index = j
#         # min_index = variant.index(min(variant[:len(variant)-1]))
#         variant[min_index] += 1
#         variant[-1] -= 1
#         variant = variant[:min_index+1] + [1 for i in range(sum(variant[min_index+1:]))]
#         i += 1
#     return i
# Круто, но это не я (
def exp_sum(n):
    if n < 0:
        return 0
    dp = [1] + [0] * n
    for num in range(1, n + 1):
        for i in range(num, n + 1):
            dp[i] += dp[i - num]
    return dp[-1]


print(exp_sum(5))
