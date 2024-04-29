class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        answer =[]
        for num in nums:
            count = sum(1 for x in nums if x < num)
            answer.append(count)
        return answer
          