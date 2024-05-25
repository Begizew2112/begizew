class Solution:
    def pancakeSort(self, arr: list[int]) -> list[int]:
        res = []
        n = len(arr)
        
        def flip(k):
            left = 0
            right = k
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
        
        for size in range(n, 1, -1):
            max_idx = arr.index(max(arr[:size]))
            if max_idx != size - 1:
                if max_idx != 0:
                    flip(max_idx)
                    res.append(max_idx + 1)
                flip(size - 1)
                res.append(size)
        
        return res
