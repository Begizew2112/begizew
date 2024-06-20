class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        result = [1]
        for i in range(rowIndex):
            next_row = [0]*(len(result)+1)
            for j in range(len(result)):
                next_row[j] += result[j]
                next_row[j+1] += result[j]
                #print(next_row)
            result = next_row

        #print(result)
        return result
        