# https://leetcode.com/problems/middle-of-the-linked-list/solution/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        resulted_list = []
        while head:
            resulted_list.append(head)
            head = head.next
        return resulted_list[len(resulted_list) // 2]


class SolutionPointers:
    def middleNode(self, head: ListNode) -> ListNode:
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow