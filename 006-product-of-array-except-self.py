# https://leetcode.com/problems/product-of-array-except-self/

from typing import List

# dirty
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            pre[i] = prefix * nums[i]
            prefix *= nums[i]
        postfix = 1
        post = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            post[i] *= postfix
            postfix *= nums[i]
        res = [1] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                pr = 1
            else:
                pr = pre[i - 1]
            if i == len(nums) - 1:
                ps = 1
            else:
                ps = post[i]
            res[i] = pr * ps
        return res


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
