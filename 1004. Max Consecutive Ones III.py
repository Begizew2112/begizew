class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        l , r = 0 ,0
        count_zeros = 0 
        max_one = 0
        while r < len(nums):
            if nums[r] == 0:
                count_zeros +=1

            while count_zeros >k :
                max_one = max( max_one , r -l )
                if nums[l] ==0:
                    count_zeros -=1
                l +=1
            max_one = max( max_one , r -l+1 )
            r +=1
        print(max_one)
        return max_one 


        

        # l = max_cons = 0
        # for r, num in enumerate(nums):
        #     if num == 0:
        #         k -= 1
        #     while k < 0:
        #         if nums[l] == 0:
        #             k += 1
        #         l += 1
        #     max_cons = max(max_cons, r - l + 1)
        # return max_cons
