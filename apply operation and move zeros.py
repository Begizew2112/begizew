class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        n = len(nums)
        for i in range(n - 1):
            if nums[i] == nums[i+1]:
                nums[i]*=2
                nums [i +1] = 0
        # to move zeros to the right        
        result = [num for num in nums if num!=0]
        result = result + [0]* (n-len(result))
        return result