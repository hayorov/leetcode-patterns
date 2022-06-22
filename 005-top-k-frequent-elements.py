# https://leetcode.com/problems/top-k-frequent-elements/

from collections import Counter
from heapq import nlargest

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counted = Counter(nums)  # O(n)
        # counted = sorted(counted, key=counted.get, reverse=True) # ~ nlog n
        heap = [(value, key) for key, value in counted.items()]  # ~ nlog k
        largest = nlargest(k, heap)
        largest = [key for value, key in largest]
        return largest


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counted = Counter(nums)  # O(n)
        resulted = []
        freq = [[] for _ in range(len(counted) + 1)]
        print(freq)
        for item, count in counted.items():
            print(count)
            freq[count - 1].append(item)
        for bucket in reversed(freq):
            for item in bucket:
                resulted.append(item)
            if len(resulted) == k:
                return resulted
