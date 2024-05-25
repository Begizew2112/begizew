class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        n = len(grid)
        maxLocal = [[0] * (n - 2) for _ in range(n - 2)]

        for i in range(1, n - 1):
            for j in range(1, n - 1):
                max_val = max(grid[i-1][j-1], grid[i-1][j], grid[i-1][j+1],
                              grid[i][j-1], grid[i][j], grid[i][j+1],
                              grid[i+1][j-1], grid[i+1][j], grid[i+1][j+1])
                maxLocal[i-1][j-1] = max_val

        return maxLocal

# # Example usage
# grid = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16]
# ]

# sol = Solution()
# print(sol.largestLocal(grid))
