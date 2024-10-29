class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        letterCount = {}
        palincount = 0
        odd_exists = False

        for letter in s:
            if letter in letterCount:
                letterCount[letter] += 1
            else:
                letterCount[letter] = 1

        for count in letterCount:
            if letterCount.get(count) % 2 == 0:
                palincount += letterCount.get(count)
            else:
                palincount += letterCount.get(count) - 1
                odd_exists = True
                
        if(odd_exists == True):
            return palincount + 1
        else:
            return palincount
