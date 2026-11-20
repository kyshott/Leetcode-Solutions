class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        for asteroid in asteroids:
            while stack and asteroid < 0 and stack[-1] > 0:
                if stack[-1] < abs(asteroid):
                    stack.pop()
                elif stack[-1] == abs(asteroid):
                    stack.pop()
                    asteroid = 0
                else:
                    asteroid = 0
        
            if asteroid != 0:
                stack.append(asteroid)
        
        return stack
