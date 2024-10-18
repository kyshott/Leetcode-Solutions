class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numMap = {}

        for i in range(0, len(nums)):

            targNum = target - nums[i]

            if(targNum in numMap):
                return[i, numMap[targNum]]

            numMap[nums[i]] = i
