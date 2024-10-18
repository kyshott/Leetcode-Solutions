class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        stringNum = str(x)
        
        for i in range(0, len(stringNum)):
            if(stringNum[i] != stringNum[(len(stringNum) - 1) - i]):
                return False
        
        return True
