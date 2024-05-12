
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode( 0 , head)
        left, right  = dummy, head
        for _ in range(n-1 ):
            right = right.next

        while right and right.next:
            left  = left.next
            right= right.next
        
        left.next= left.next.next

        return dummy.next



