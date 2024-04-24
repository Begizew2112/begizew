class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        def diagonal_value(row, column):
            value = matrix[row][column]
            while row < len(matrix) and column < len(matrix[0]):
                if matrix[row][column] != value:
                    return False
                row += 1
                column += 1
            return True

        for column in range(len(matrix[0])):
            if not diagonal_value(0, column):
                return False
        for row in range(1, len(matrix)):
            if not diagonal_value(row, 0):
                return False
        return True
