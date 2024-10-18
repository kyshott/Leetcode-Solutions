class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        openParen = 0
        unmatched = 0
        
        for i in range(0, len(s)):
            if(s[i] == "("):
                openParen += 1
            if(s[i] == ")"):
                openParen -= 1
            if(openParen < 0):
                unmatched += 1
                openParen = 0
        
        return abs(unmatched + openParen)
