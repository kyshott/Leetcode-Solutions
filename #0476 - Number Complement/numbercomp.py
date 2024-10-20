class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """

        complement = ''

        binNum = bin(num)

        for i in range(2, len(binNum)):
            if(binNum[i] == '0'):
                complement = complement + '1'
            elif(binNum[i] == '1'):
                complement = complement + '0'

        return int(complement, 2)
