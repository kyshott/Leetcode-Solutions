class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        map = dict()

        for i in range(len(arr)):
            if str(arr[i]) not in map:
                map[str(arr[i])] = 0
                map[str(arr[i])] += 1
            else:
                map[str(arr[i])] += 1

        if len(set(map.values())) < len(map):
            return False
        else:
            return True
