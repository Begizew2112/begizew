class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        skill.sort()
        n = len(skill)-1
        l = 0
        mean_sum =[]
        
        while n > l:
            mean_sum.append(skill[l] +  skill[n])
            n -= 1
            l += 1
        summ = set(mean_sum)
        
        if len(summ) == 1:
            l = 0
            n = len(skill)-1
            result = 0
            while n > l:
                mult = (skill[l] * skill[n])
                result += mult
                n -= 1
                l += 1
                
        else:
            return -1

        return result
        