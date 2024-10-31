class Solution(object):
    def lastVisitedIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        seen = []
        ans = []
        k = 0

        for i in range(0, len(nums)):
            if(nums[i] != -1):
                seen.insert(0, nums[i])
                k = 0
            if(nums[i] == -1):
                k += 1
                if(k <= len(seen)):
                    ans.append(seen[k - 1])
                else:
                    ans.append(-1)

        return ans
