class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        fives = 0
        tens = 0

        for i in range(0, len(bills)):
            if(bills[i] == 5):
                fives += 1
            elif(bills[i] == 10):
                if(fives < 1):
                    return False
                else:
                    fives -= 1
                    tens += 1
            elif(bills[i] == 20):
                if(fives >= 1 and tens >= 1):
                    fives -= 1
                    tens -= 1
                elif(fives >= 3):
                    fives -= 3
                else:
                    return False
        
        return True
