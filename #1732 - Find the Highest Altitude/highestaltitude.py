class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alts = []
        alts.append(0)
        current = 0

        for altitudes in gain:
            current += altitudes
            alts.append(current)

        return max(alts)
