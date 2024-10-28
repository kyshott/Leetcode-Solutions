class Solution(object):
    def checkZeroOnes(self, s):
        """
        :type s: str
        :rtype: bool
        """
        oneSplit = s.split('0')
        zeroSplit = s.split('1')
        oneMax = max([len(i) for i in oneSplit])
        zeroMax = max([len(i) for i in zeroSplit])
        
        if(oneMax > zeroMax):
            return True
        else:
            return False
