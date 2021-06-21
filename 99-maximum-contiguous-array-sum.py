"""
You are given an array of integers (both positive and negative). Find the continuous sequence with the largest sum. Return the sum.
        a. Input: 2, -8, 3, -2, 4, -10
        b. 5 (3, -2, 4)

or https://leetcode.com/problems/maximum-subarray/
"""

from sys import maxsize


def solution_bf(seq):
    max_sum = -maxsize - 1
    for pos, i in enumerate(seq):
        max_sum = max(i, max_sum)
        suma = i
        for y in seq[pos + 1 :]:
            suma += y
            max_sum = max(max_sum, suma)
    return max_sum


solution_bf((2, -8, 3, -2, 4, -10))
# 5
# Time Complexity: O(N) n^2


def solution_optimized(seq):
    '''
    optimization: use positive integers as boundaries
    '''

    max_sum = -maxsize - 1
    max_current = 0

    for i in range(0, len(seq)):
        max_current = max_current + seq[i]
        if max_sum < max_current:
            max_sum = max_current

        if max_current < 0:
            max_current = 0
    return max_sum


solution_optimized((2, -8, 3, -2, 4, -10))
# 5
# Time Complexity: O(N) n
