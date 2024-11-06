class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        map = {}
        vals = []

        for i in range(0, len(arr)):
            if(arr[i] in map):
                map[arr[i]] += 1
            else:
                 map.setdefault(arr[i], 1)

        for val in map.values():
            if(val in vals):
                return False
            
            vals.append(val)
        
        return True
