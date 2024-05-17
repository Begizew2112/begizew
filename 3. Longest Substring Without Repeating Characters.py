class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        length = 0 
        char = set()
        for r in range(l ,len(s)):
            while s[r] in char:
                char.remove(s[l])
                l +=1

            
            char.add(s[r])
            length = max( length , r -l +1)
        return length

       