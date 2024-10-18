class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lastUnique = 1
        for i in range(1, len(nums)):
            if(nums[i-1] != nums[i]):
                nums[lastUnique] = nums[i]
                lastUnique += 1
        return lastUnique
