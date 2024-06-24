class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pair = [[p,s] for p ,s in zip (position , speed)]
        pair.sort()
        stack =[]
        #[[0, 1], [3, 3], [5, 1], [8, 4], [10, 2]]
        for p , s  in pair[::-1]:
            stack.append((target - p)/s) 
            if len(stack) >=2 and  stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)