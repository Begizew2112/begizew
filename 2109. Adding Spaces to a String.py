class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        index = 0
        result = []
        for space in spaces: # space  = 8,13,15
            result.append(s[index : space]) #Leetcode , Leetcode Helps , Leetcode Helps Me Learn
            result.append( ' ')
            index =  space 

        result.append(s[index : ]) # append the current index to the last word

        return ''.join(result)