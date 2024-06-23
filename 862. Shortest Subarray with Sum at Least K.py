from collections import deque
class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:
        n = len(nums)
        pre_sum = [0] * (n + 1)
        for i in range(n):
            pre_sum[i + 1] = pre_sum[i] + nums[i]
        
        dq = deque()
        min_len = float('inf')
        
        for i in range(n + 1):
            while dq and pre_sum[i] - pre_sum[dq[0]] >= k:
                min_len= min(min_len, i - dq.popleft())
            while dq and pre_sum[i] <= pre_sum[dq[-1]]:
                print()
            dq.append(i)
    
        return min_len if min_len != float('inf') else -1


