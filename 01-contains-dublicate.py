# https://leetcode.com/problems/contains-duplicate/


from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return not len(set(nums)) == len(nums)


# less elegant with any
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        inv = {}
        for num in nums:
            if not num in inv:
                inv.update({num: False})
            else:
                inv.update({num: True})
        if any(inv.values()):
            return True
        if not any(inv.values()):
            return False
