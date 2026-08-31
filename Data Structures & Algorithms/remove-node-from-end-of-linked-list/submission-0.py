# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rec(self, head, n):
        if not head:
            return None, 0
        node, count = self.rec(head.next, n)
        count += 1
        if count == n:
            return node, count
        head.next = node
        return head, count

    def removeNthFromEnd(self, head, n):
        return self.rec(head,n)[0]