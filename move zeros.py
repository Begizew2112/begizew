from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        write_ptr = 0
        
        for read_ptr in range(len(nums)):
            if nums[read_ptr] != 0:
                nums[write_ptr], nums[read_ptr] = nums[read_ptr], nums[write_ptr]
                write_ptr += 1
