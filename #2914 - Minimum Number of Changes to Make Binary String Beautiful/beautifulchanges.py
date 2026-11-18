class Solution:
    def minChanges(self, s: str) -> int:
        step = 0
        last = ""
        changes = 0
        for i in range(len(s)):
            if (step == 1):
                if last != s[i]:
                    changes += 1
                step = 0
            else: 
                step += 1
            last = s[i]
        
        return changes
