class Solution(object):
    def longestSquareStreak(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numSet = set(nums)

        maxStreak = 0

        for n in nums:
            currentStreak = 0
            currentNum = n

            while(currentNum in numSet):
                currentStreak += 1
                currentNum = currentNum * currentNum
            
            if(currentStreak >= 2):
                maxStreak = max(currentStreak, maxStreak)
        
        if(maxStreak < 2):
            return -1
        
        return maxStreak
