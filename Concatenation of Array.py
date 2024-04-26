class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        ans = nums.copy()
        ans.extend(nums)
        return ans
        