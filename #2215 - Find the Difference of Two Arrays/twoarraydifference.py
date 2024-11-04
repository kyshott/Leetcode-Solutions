class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer0 = []
        answer1 = []
        final = []

        for nums in set(nums1):
            if(nums not in nums2):
                answer0.append(nums)
        
        for nums in set(nums2):
            if(nums not in nums1):
                 answer1.append(nums)
        
        final.append(answer0)
        final.append(answer1)

        return final
