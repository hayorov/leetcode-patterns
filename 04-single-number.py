# https://leetcode.com/problems/single-number/

from typing import List

from functools import reduce


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda result, num: result ^ num, nums)  # XOR bitwise