class Solution:
    def myPow(self, x: float, n: int) -> float:
        def powern(x, n):
            #base cause
            if x ==0: return 0
            if n ==0: return 1
            result= powern(x , n//2)
            result = result*result
            return x * result if n%2 else result
        result = powern(x ,abs(n))
        return result if n >= 0 else 1/result

        
        
        # res = 1
        # if n > 0:
        #     for i in range(n):
        #         if x != 0:
        #             res *= x
        #         else:
        #             return 0
        # elif n == 0:
        #     return 1
        # else:
        #     y = -1 * n
        #     for j in range(y):
        #         if x != 0:
        #             res /=x
        #         else:
        #             return 0
                
        # print(res) 
        # return res
        