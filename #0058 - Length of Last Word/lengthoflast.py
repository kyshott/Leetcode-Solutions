class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        lastword = ""
        whiteSpace = False

        for i in range(0, len(s)):
            if(s[i] == " "):
                whiteSpace = True
                continue
            elif(whiteSpace == True):
                lastword = ""
                lastword += s[i]
                whiteSpace = False
            else:
                lastword += s[i]
            
        return len(lastword)
