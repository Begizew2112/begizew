
from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        # Convert each number to string
        nums_str = list(map(str, nums))
        
        # Custom comparator to sort by the largest concatenated result
        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0
        
        # Sort the list with the custom comparator
        nums_str.sort(key=cmp_to_key(compare))
        
        # Join the sorted strings
        largest_num = ''.join(nums_str)
        
        # Handle the edge case where the largest number is "0"
        if largest_num[0] == '0':
            return '0'
        else:
            return largest_num
