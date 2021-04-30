# https://leetcode.com/problems/remove-linked-list-elements/submissions/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        new_head = None
        prev_item = None
        while head:
            if head.val == val:
                if prev_item:
                    prev_item.next = head.next
            else:
                prev_item = head
                if not new_head:
                    new_head = head
            head = head.next
        return new_head
