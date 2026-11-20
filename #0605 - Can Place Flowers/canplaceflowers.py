class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                if i == 0:
                    if len(flowerbed) == 1:
                        count += 1
                        flowerbed[i] = 1
                    elif flowerbed[i + 1] == 0:
                        flowerbed[i] = 1
                        count += 1
                elif i == len(flowerbed) - 1:
                    if flowerbed[i - 1] == 0:
                        flowerbed[i] = 1
                        count += 1
                elif flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    count += 1
        
        return count >= n
