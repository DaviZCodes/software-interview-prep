class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0: # base case
            return []
        
        result = [[1]]

        for i in range(numRows - 1): # numRows - 1 since we included the first row [1]
            previousRow = result[-1]
            currRowTemplate = [0] + previousRow + [0] # all rows have 0 on the left and right

            currRow = [] # currentRow

            for j in range(len(result[-1]) + 1): # new row has length of previous row + 1
                currRow.append(currRowTemplate[j] + currRowTemplate[j + 1]) # sum of two values above

            result.append(currRow)

        return result
        
