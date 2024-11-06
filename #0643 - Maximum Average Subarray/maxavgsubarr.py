class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        window = k

        total = sum(nums[0:window])

        maximum = total

        for i in range(len(nums) - window):
            total = (total - nums[i]) + nums[window]
            window += 1
            maximum = max(maximum, total)

        return maximum / k
