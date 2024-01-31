class Solution:
    def addDigits(self, num: int) -> int:
        '''
        1. The key to this solution is that only numbers 9 or smaller 
        are one digit. If it's one digit, we just return it.

        2. If the number is divisible by 9, we just want to always return 9.
        This is because the single digit it can be is 9. 

        3. Also we want to use remainder of division to 9: %9.

        This is because e.g. we have 10, 10 % 9 = 1, which is the answer we want.
        23 = 5. Also 23 % 9 = 5. 100 = 1. Also 100 % 9 = 1. 

        Every digit addition is the same as the remainder (the number % 9). 
        Very interesting!
        '''
        if num <= 9:
            return num

        if num % 9 == 0:
            return 9

        
        return num % 9
        
        
