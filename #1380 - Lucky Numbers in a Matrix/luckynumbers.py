class Solution(object):
    def luckyNumbers(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        maxCols = {}
        listCols = []
        minRows = []
        lucky = []

        for i in range(0, len(matrix)):
            minRows.append(min(matrix[i]))
            for j in range(0, len(matrix[i])):
                maxCols.setdefault(j, []).append(matrix[i][j])

        for nums in maxCols.values():
            listCols.append(max(nums))

        for nums in listCols:
            if(nums in minRows):
                lucky.append(nums)
        
        return lucky
