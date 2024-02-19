# Surprisingly difficult. Made me learn something new about bitwise operations. 

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        ''' 
        pow(2,n) & (pow(2,n) - 1) = 0
        e.g. 4 & (4-1)
             4 & 3
             0b100 & 0b011 = 0

             not (n & (n-1)) means n is a power of two
        '''
        if n == 0:
            return False

        return not (n & (n-1))

