class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[left], nums[r] = nums[r], nums[left]
                left +=1

        return nums