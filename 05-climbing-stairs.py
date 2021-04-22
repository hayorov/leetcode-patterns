# https://leetcode.com/problems/climbing-stairs/solution/


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        steps = {}
        steps[1] = 1
        steps[2] = 2

        for step in range(3, n + 1):
            steps[step] = steps[step - 1] + steps[step - 2]
        return steps[n]