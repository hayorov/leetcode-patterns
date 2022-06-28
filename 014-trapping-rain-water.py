# https://leetcode.com/problems/trapping-rain-water/

from collections import Counter
from typing import List

# O(N) memory with 2 left/right tables
class Solution:
    def trap(self, height: List[int]) -> int:
        left = []
        right = []

        prev = 0
        for pos, i in enumerate(height):
            cur = prev
            left.append(cur)
            prev = max(i, prev)
        prev = 0
        for pos, i in enumerate(reversed(height)):
            cur = prev
            right.append(cur)
            prev = max(i, cur)
        res = 0
        for pos, i in enumerate(left):
            res += max(0, min(i, right[len(right) - pos - 1]) - height[pos])
        return res


# O(1) memory with 2 pointers (l, r)
class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        lp, rp = 0, len(height) - 1
        max_l, max_r = height[lp], height[rp]

        while lp < rp:
            if max_l < max_r:
                lp += 1
                max_l = max(max_l, height[lp])
                res += max_l - height[lp]
            else:
                rp -= 1
                max_r = max(max_r, height[rp])
                res += max_r - height[rp]
        return res
