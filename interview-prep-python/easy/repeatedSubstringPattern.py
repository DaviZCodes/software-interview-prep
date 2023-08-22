class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        #e.g abcabc
        transformed = (s + s)[1:-1]
        #transformed = bcabcabcab
        # abcabc is in, so return True
        if s in transformed:
            return True
        
        return False

        
