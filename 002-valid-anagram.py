# https://leetcode.com/problems/valid-anagram/

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_coun = Counter(s)
        t_coun = Counter(t)

        for item, value in s_coun.items():
            if t_coun.get(item) != value:
                return False
        return True


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
