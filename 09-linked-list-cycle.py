# https://leetcode.com/problems/linked-list-cycle/submissions/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        seen_items = set()
        while head:
            if head in seen_items:
                return True
            seen_items.add(head)
            head = head.next
        return False
