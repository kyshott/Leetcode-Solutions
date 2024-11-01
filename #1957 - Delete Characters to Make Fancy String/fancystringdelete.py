class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        built = s[0]
        currentletter = 0

        for i in range(1, len(s)):
            if(s[i] != s[currentletter]):
                built = built + s[i]
                currentletter = i
            elif(s[i] == s[currentletter]):
                if(i - currentletter >= 2):
                    continue
                else:
                    built = built + s[i]

        return built
