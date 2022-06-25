# https://leetcode.com/problems/last-stone-weight/

import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # invert
        stones = list(map(lambda x: x * -1, stones))
        heapq.heapify(stones)
        while stones:
            x = heapq.heappop(stones)
            try:
                y = heapq.heappop(stones)
            except IndexError:
                return x * -1
            if x != y:
                heapq.heappush(stones, abs(x - y) * -1)
        return 0
