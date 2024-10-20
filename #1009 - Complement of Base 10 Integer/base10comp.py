class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type num: int
        :rtype: int
        """

        complement = ''

        binNum = bin(n)

        for i in range(2, len(binNum)):
            if(binNum[i] == '0'):
                complement = complement + '1'
            elif(binNum[i] == '1'):
                complement = complement + '0'

        return int(complement, 2)
        
