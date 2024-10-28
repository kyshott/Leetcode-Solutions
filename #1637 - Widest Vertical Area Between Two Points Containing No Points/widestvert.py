class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        arr = sorted(points)

        gaps = []

        for i in range(len(arr) - 1):
            gaps.append(arr[i][0] - arr[i - 1][0])

        return max(gaps)
