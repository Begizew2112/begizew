
class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        nums.sort() 
        count = 0
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] + nums[right] < k:
                left += 1
            elif nums[left] + nums[right] > k:
                right -= 1
            else:
                left += 1
                right -= 1
                count += 1
        return count

 
        # nums = sorted(nums)
        # r = len(nums)-1
        # l = 0
       
        # if len(nums) == 2 and sum(nums) ==k:
        #     return 1
        # elif len(nums)<= 2 and sum(nums) !=k: 
            
        #     return 0
        # else:
        #     r = len(nums)-1
        #     count =0
        #     while l < r  :
        #         if nums[l] + nums[r] == k:
        #             nums.pop()
        #             nums.pop(0)
        #             count +=1
        #             r -= 2
        #         elif nums[l] + nums[r] < k:
        #             l +=1
        #         else:
        #             nums[l] + nums[r] > k
        #             r -=1
        # #print(nums)
        # return count
        
            















