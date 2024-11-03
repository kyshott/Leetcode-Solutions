class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        table = {}

        for i in range(0, len(nums)):
            if(nums[i] not in table):
                table.setdefault(nums[i], 1)
            else:
                table[nums[i]] += 1

        for key, val in table.items():
            if(val > (len(nums) /2)):
                return key
