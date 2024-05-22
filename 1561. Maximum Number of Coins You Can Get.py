class Solution:
    def maxCoins(self, piles: list[int]) -> int:
        piles.sort()
        r = len (piles)-2
        div = (r +2)/3
        data = []
        while div >0:
        
            data.append(piles[r])
            div -=1
            if r>2 :
               r -=2
            else:
                break
           
        summ = sum(data)

        return summ
        