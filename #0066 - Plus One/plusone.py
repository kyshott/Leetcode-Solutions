class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        strNumber = ""
        intNumber = 0
        output = []

        for i in range(0, len(digits)):
            strNumber = strNumber + str(digits[i])
        
        intNumber = int(strNumber) + 1

        strNumber = str(intNumber)

        for i in range(0, len(strNumber)):
            output.append(int(strNumber[i]))

        return output
