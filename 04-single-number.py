# https://leetcode.com/problems/single-number/

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for number in nums:
            result = result ^ number  # XOR
        return result