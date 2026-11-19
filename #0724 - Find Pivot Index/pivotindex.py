class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total = sum(nums)
        lsum = 0
        prefix = [0]

        for i in range(len(nums)):
            lsum = nums[i] + lsum
            prefix.append(lsum)
            rsum = total - prefix[i]

            if (lsum == rsum):
                return i
        
        return -1
