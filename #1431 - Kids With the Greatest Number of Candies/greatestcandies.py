class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        largest = []
        for i in range(len(candies)):
            if (candies[i] + extraCandies >= max(candies)):
                largest.insert(i, True)
            else:
                largest.insert(i, False)
        
        return largest
