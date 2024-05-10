# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        nums =[]
        while head:
            nums.append (head.val)
            head = head.next
        l,r, = 0 , len(nums)-1
        while l<=r :
            if nums[l] != nums[r]:
                return False
            l +=1
            r -=1
        return True

        
        # # Find the middle of the linked list
        # slow = fast = head
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next

        # # Reverse the second half of the linked list
        # pre, curr = None, slow
        # while curr:
        #     nxt = curr.next
        #     curr.next = pre
        #     pre = curr
        #     curr = nxt

        # # Compare the first half with the reversed second half
        # left, right = head, pre
        # while right:
        #     if left.val != right.val:
        #         return False
        #     left, right = left.next, right.next

        # return True
