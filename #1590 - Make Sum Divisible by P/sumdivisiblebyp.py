class Solution(object):
    def minSubarray(self, nums, p):
        total = sum(nums)
        remainder = total % p

        if remainder == 0:
            return 0

        shortest = len(nums)
        prefixSum = 0
        prefixSums = {0: -1}

        for i in range(0, len(nums)):
            prefixSum = (prefixSum + nums[i]) % p
            target = (prefixSum - remainder + p) % p

            if target in prefixSums:
                shortest = min(shortest, i - prefixSums[target])

            prefixSums[prefixSum] = i

        if(shortest >= len(nums)):
            return -1
        else:
            return shortest
