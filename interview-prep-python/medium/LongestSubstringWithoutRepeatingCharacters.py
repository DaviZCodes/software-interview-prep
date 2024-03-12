class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set() # to keep track of characters (no duplicates)
        left = 0 # left pointer for sliding window algo
        result = 0

        for right in range(len(s)):
            while s[right] in charSet: # if duplicated, we slide the left pointer
                charSet.remove(s[left]) 
                '''
                We need to remove s[left] 
                e.g. if abbxyz, then when we reach b,
                we want to move the left pointer to the new b
                remove a, inc left, remove b inc left, then we start a new
                sliding window.
                '''
                left += 1

            charSet.add(s[right])
            result = max(result, right - left + 1) # + 1 at the end because index starts at 0

        return result
        
