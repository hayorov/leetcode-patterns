# https://leetcode.com/problems/two-sum/

from typing import List
from collections import Counter


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        acc = {}
        for pos, value in enumerate(nums):
            if target - value in acc:
                return [acc[target - value], pos]
            acc[value] = pos


# less elegant
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        inv = Counter(nums)
        for pos_f, num in enumerate(nums):
            candid = target - num
            if candid in inv:
                if candid != num or inv[candid] > 1:
                    break
        for pos_s, num in enumerate(nums):
            if pos_s != pos_f and num == candid:
                return (pos_f, pos_s)
