
from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if  k > len(nums):
            return ''
       # nums = [1,12,-5,-6,50,3], k = 4
        first_sum  = sum(nums[ : k])
        avarage = first_sum/ k
        for i in range(k , len(nums)):
            first_sum += nums[i] - nums[i -k]
            avarage = max(first_sum /k , avarage)

        #print(avarage)
        return avarage
    