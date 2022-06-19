# https://leetcode.com/problems/valid-parentheses/


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matcher = {
            ")": "(",
            "}": "{",
            "]": "[",
        }
        for parenth in s:
            if parenth in matcher.values():
                stack.append(parenth)
            else:
                if not stack or matcher[parenth] != stack.pop():
                    return False
        return not stack
