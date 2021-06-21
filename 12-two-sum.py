# https://leetcode.com/problems/two-sum/

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        acc = {}
        for pos, value in enumerate(nums):
            if target - value in acc:
                return [acc[target - value], pos]
            acc[value] = pos
