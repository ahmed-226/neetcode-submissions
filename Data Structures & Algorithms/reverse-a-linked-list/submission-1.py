# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1. move to the last element with saved head info in call stack for each element
        # once reach last element return to the prevous one from the call stack where the head.next refer to this last element and make its next ( last element ) refer to it 
        # then break its link to last element and make it refer to None
        if not head:
            return None

        new_head=head
        
        if head.next: # reach the last element
            new_head=self.reverseList(head.next)
            # when return to the call stack, we refer start form the element before the last one so this expersion si valid
            head.next.next=head
        # cut the link 
        head.next=None

        return new_head