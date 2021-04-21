# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/submissions/


from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return set(range(1, len(nums) + 1)) - set(nums)
