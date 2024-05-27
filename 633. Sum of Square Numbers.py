class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        right = c-1
        left = 0
        if c == 1 or c ==0 :
            return True 
        if c < 0:
            return False
        while left <= right:
            if left*left + right*right == c:
                return True 
            elif left*left + right*right > c:
                if (right//2)**2 > c:
                    right = right//2
                else:
                    right -=1 
            elif left*left + right*right < c:
                left +=1
            else:
                return False
        
        return 

            
        