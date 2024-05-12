from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode( 0 , head) # creat fake dummy node
        #part 2
        leftprev , curr = dummy , head
        for i in range(left -1):
            leftprev , curr = curr , curr.next
        #reverse in the given range
        #part 3
        prev = None
        for  i in range( right - left + 1):
            temp = curr.next
            curr.next = prev
            prev = curr 
            curr = temp
        #update the pointer  part 4
        leftprev.next.next = curr
        leftprev.next= prev
        return dummy.next




 
        