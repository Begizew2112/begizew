#Container With Most Water
class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right  = len(height) - 1
        area = []
        while left < right:
            current_area = min(height[left], height[right]) * ( right - left)
            area.append(current_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -=1
        return max(area)
solution = Solution()
height = [ 2,4,8,4,6,7,5,9,7]
print(solution.maxArea(height))
