class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = {}
        numtohit = len(nums) / 2

        for i in nums:
            if(i not in counts):
                counts.setdefault(i, 1)
            else:
                counts[i] += 1
        
        for nums in counts:
            if(counts.get(nums) == numtohit):
                return nums
