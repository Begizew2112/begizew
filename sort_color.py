class Solution:
    def sortColors(self, nums: list[int]) -> None:
 
        m , l = 0 , 0
        r = len(nums)-1
        while m <= r:
            if nums[m] == 2:
                nums[m], nums[r] = nums[r], nums[m]
                r -= 1
            elif nums[m] == 0 :
                nums[m], nums[l] = nums[l], nums[m]
                l+=1
                m+=1
            else:
                m+=1
        return 





        
    
    

    
#print(count)