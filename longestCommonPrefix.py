class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        res = ''
        for i in range(len(strs[0])):
            for n in strs:
                if i == len(n) or n[i] != strs[0][i]:
                    return res
            res +=strs[0][i]
        return res
