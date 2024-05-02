class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        nums2 = set (nums2)
        for n in nums1:
            if n in nums2:
               return n
               break

        return -1
                
        