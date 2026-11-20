class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            stack.append(s[i])
            if s[i] == '*':
                stack.pop()
                stack.pop()
        
        return "".join(stack)

#push character onto stack as we iterate through str
#if the character is a star, do not push and instead pop off the stack
