# https://leetcode.com/problems/missing-number/


from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()  # O(n) space
        # borders
        if nums[0] != 0:
            return 0
        if nums[-1] != len(nums):
            return len(nums)
        for index in range(1, len(nums)):  # O(n) time
            expected_value = nums[index - 1] + 1
            if nums[index] != expected_value:
                return expected_value