class Solution:
    def reverseString(self, s: list[str]) -> None:
        # recurstion method
        def reverse(l,r):
            if l <r:
                s[l] ,s[r] =s[r] ,s[l]  
                reverse(l+1 , r-1)
        reverse (0 , len(s)-1)
    #normal method 

        # l =0 
        # r =len(s)-1
        # while l < r:
        #     s[l] , s[r] = s[r] , s[l] 
        #     l += 1
        #     r -= 1
        # print(s)
        # return s
    # o(n) space complexity
        # stack =[]
        # for i in s:
        #     stack.append(i)
        # i =0 
        # while stack:
        #     s[i] = stack.pop()
        #     i +=1
        # return s
       # method iii

