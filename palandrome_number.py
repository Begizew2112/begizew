class Solution:
    def isPalindrome(self, x: int) -> bool:
        pal = str(x)[:: -1]
        if pal ==str(x) :
            return True
        else:
            return False
        return
        